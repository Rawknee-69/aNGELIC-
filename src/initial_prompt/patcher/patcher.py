import os
import time

from jinja2 import Environment, BaseLoader
from typing import List, Dict, Union

from src.config import Config
from src.llm import LLM
from src.state import AgentState

PROMPT = open("src/initial_prompt/patcher/patcher.jinja2", "r", encoding="utf-8").read().strip()

class Patcher:
    def __init__(self, base_model: str):
        config = Config()
        self.project_dir = config.get_projects_dir()
        
        self.llm = LLM(model_id=base_model)

    def render(
        self,
        conversation: list,
        code_markdown: str,
        commands: list,
        error :str,
        system_os: str
    ) -> str:
        env = Environment(loader=BaseLoader())
        template = env.from_string(PROMPT)
        return template.render(
            conversation=conversation,
            code_markdown=code_markdown,
            commands=commands,
            error=error,
            system_os=system_os
        )

    def validate_response(self, response: str) -> Union[List[Dict[str, str]], bool]:
        response = response.strip()

        response = response.split("~~~", 1)[1]
        response = response[:response.rfind("~~~")]
        response = response.strip()

        result = []
        current_file = None
        current_code = []
        code_block = False

        for line in response.split("\n"):
            if line.startswith("File: "):
                if current_file and current_code:
                    result.append({"file": current_file, "code": "\n".join(current_code)})
                current_file = line.split("`")[1].strip()
                current_code = []
                code_block = False
            elif line.startswith("```"):
                code_block = not code_block
            else:
                current_code.append(line)

        if current_file and current_code:
            result.append({"file": current_file, "code": "\n".join(current_code)})

        return result

    def save_code_to_project(self, response: List[Dict[str, str]], project_name: str):
        project_name = project_name.lower().replace(" ", "-")
        project_path = os.path.join(self.project_dir, project_name)
        
        # Check if the project directory already exists
        if not os.path.exists(project_path):
            # If not, create the directory
            os.makedirs(project_path, exist_ok=True)
        
        for file in response:
            file_path = os.path.join(project_path, file['file'])
            file_path_dir = os.path.dirname(file_path)
            
            # Check if the directory for the file exists
            if not os.path.exists(file_path_dir):
                # If not, create the directory
                os.makedirs(file_path_dir, exist_ok=True)
            
            # Check if the file exists
            if os.path.exists(file_path):
                # If the file exists, append to it instead of overwriting
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(file["code"])
            else:
                # If the file does not exist, create it
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(file["code"])
        
        return project_path

    def get_project_path(self, project_name: str):
        project_name = project_name.lower().replace(" ", "-")
        return os.path.join(self.project_dir, project_name)

    def response_to_markdown_prompt(self, response: List[Dict[str, str]]) -> str:
        response = "\n".join([f"File: `{file['file']}`:\n```\n{file['code']}\n```" for file in response])
        return f"~~~\n{response}\n~~~"

    def emulate_code_writing(self, code_set: list, project_name: str):
        for current_file in code_set:
            file = current_file["file"]
            code = current_file["code"]

            new_state = AgentState().new_state()
            new_state["internal_monologue"] = "Writing code..."
            new_state["terminal_session"]["title"] = f"Editing {file}"
            new_state["terminal_session"]["command"] = f"vim {file}"
            new_state["terminal_session"]["output"] = code
            AgentState().add_to_current_state(project_name, new_state)
            time.sleep(1)

    def execute(
        self,
        conversation: str,
        code_markdown: str,
        commands: list,
        error: str,
        system_os: dict,
        project_name: str
    ) -> str:
        prompt = self.render(
            conversation,
            code_markdown,
            commands,
            error,
            system_os
        )
        response = self.llm.inference(prompt, project_name)
        
        valid_response = self.validate_response(response)
        
        while not valid_response:
            print("Invalid response from the model, trying again...")
            return self.execute(
                conversation,
                code_markdown,
                commands,
                error,
                system_os,
                project_name
            )
        
        self.emulate_code_writing(valid_response, project_name)

        return valid_response

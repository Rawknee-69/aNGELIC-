import os
import time

from jinja2 import Environment, BaseLoader
from typing import List, Dict, Union

from src.config import Config
from src.llm import LLM
from src.state import AgentState
from src.logger import Logger

PROMPT = open("src/initial_prompt/coding_system/coder.jinja2", "r", encoding="utf-8").read().strip()

class Coding_System:
    def __init__(self, base_model: str):
        config = Config()
        self.project_dir = config.get_projects_dir()
        self.logger = Logger()
        self.llm = LLM(model_id=base_model)

    def render(
        self, step_by_step_plan: str, user_context: str, search_results: dict
    ) -> str:
        env = Environment(loader=BaseLoader())
        template = env.from_string(PROMPT)
        return template.render(
            step_by_step_plan=step_by_step_plan,
            user_context=user_context,
            search_results=search_results,
        )

    def validate_response(self, response: str) -> Union[List[Dict[str, str]], bool]:
        response = response.strip()

        self.logger.debug(f"Response from the model: {response}")

        if "~~~" not in response:
            return False

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
        file_path_dir = None
        project_name = project_name.lower().replace(" ", "-")

        for file in response:
            file_path = f"{self.project_dir}/{project_name}/{file['file']}"
            file_path_dir = file_path[:file_path.rfind("/")]
            os.makedirs(file_path_dir, exist_ok=True)

            with open(file_path, "w") as f:
                f.write(file["code"])
    
        return file_path_dir

    def get_project_path(self, project_name: str):
        project_name = project_name.lower().replace(" ", "-")
        return f"{self.project_dir}/{project_name}"

    def response_to_markdown_prompt(self, response: List[Dict[str, str]]) -> str:
        response = "\n".join([f"File: `{file['file']}`:\n```\n{file['code']}\n```" for file in response])
        return f"~~~\n{response}\n~~~"

    def emulate_code_writing(self, code_set: list, project_name: str):
        for current_file in code_set:
            file = current_file["file"]
            code = current_file["code"]

            current_state = AgentState().get_latest_state(project_name)
            new_state = AgentState().new_state()
            new_state["browser_session"] = current_state["browser_session"] # keep the browser session
            new_state["internal_monologue"] = "Writing code..."
            new_state["terminal_session"]["title"] = f"Editing {file}"
            new_state["terminal_session"]["command"] = f"vim {file}"
            new_state["terminal_session"]["output"] = code
            AgentState().add_to_current_state(project_name, new_state)
            time.sleep(2)

    def execute(
        self,
        step_by_step_plan: str,
        user_context: str,
        search_results: dict,
        project_name: str
    ) -> str:
        prompt = self.render(step_by_step_plan, user_context, search_results)
        response = self.llm.inference(prompt, project_name)
        
        valid_response = self.validate_response(response)
        
        while not valid_response:
            print("Invalid response from the model, trying again...")
            return self.execute(step_by_step_plan, user_context, search_results, project_name)
        
        print(valid_response)
        
        self.emulate_code_writing(valid_response, project_name)

        return valid_response

import json

from jinja2 import Environment, BaseLoader

from src.llm import LLM

PROMPT = open("src/initial_prompt/reporter/reporter.jinja2", encoding="utf-8").read().strip()

class Reporter:
    def __init__(self, base_model: str):
        self.llm = LLM(model_id=base_model)

    def render(self, conversation: list, code_markdown: str) -> str:
        env = Environment(loader=BaseLoader())
        template = env.from_string(PROMPT)
        return template.render(
            conversation=conversation,
            code_markdown=code_markdown
        )

    def validate_response(self, response: str):
        response = response.strip().replace("```md", "```")
        
        if response.startswith("```") and response.endswith("```"):
            response = response[3:-3].strip()
 
        return response

    def execute(self,
        conversation: list,
        code_markdown: str,
        project_name: str
    ) -> str:
        prompt = self.render(conversation, code_markdown)
        response = self.llm.inference(prompt, project_name)
        
        valid_response = self.validate_response(response)
        
        while not valid_response:
            print("Invalid response from the model, trying again...")
            return self.execute(conversation, code_markdown, project_name)

        return valid_response


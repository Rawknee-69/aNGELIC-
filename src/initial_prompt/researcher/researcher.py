import json
from typing import List

from jinja2 import Environment, BaseLoader

from src.llm import LLM
from src.browser.search import BingSearch

PROMPT = open("src/initial_prompt/researcher/researcher.jinja2", encoding="utf-8").read().strip()


class Researcher:
    def __init__(self, base_model: str):
        self.bing_search = BingSearch()
        self.llm = LLM(model_id=base_model)

    def render(self, step_by_step_plan: str, contextual_keywords: str) -> str:
        env = Environment(loader=BaseLoader())
        template = env.from_string(PROMPT)
        return template.render(
            step_by_step_plan=step_by_step_plan,
            contextual_keywords=contextual_keywords
        )

    def validate_response(self, response: str) -> dict | bool:
        response = response.strip().replace("```json", "```")

        try:
            response = response.split("```")[1].split("```")[0]
            response = json.loads(response)
        except Exception as _:
            return False

        response = {k.replace("\\", ""): v for k, v in response.items()}

        if "queries" not in response and "ask_user" not in response:
            return False
        else:
            return {
                "queries": response["queries"],
                "ask_user": response["ask_user"]
            }

    def execute(self, step_by_step_plan: str, contextual_keywords: List[str], project_name: str) -> dict | bool:
        contextual_keywords_str = ", ".join(map(lambda k: k.capitalize(), contextual_keywords))
        prompt = self.render(step_by_step_plan, contextual_keywords_str)
        
        response = self.llm.inference(prompt, project_name)
        
        valid_response = self.validate_response(response)

        while not valid_response:
            print("Invalid response from the model, trying again...")
            return self.execute(step_by_step_plan, contextual_keywords, project_name)

        return valid_response

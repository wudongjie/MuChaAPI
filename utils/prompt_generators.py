from models import Prompt, MidJourneyPrompt
from pydantic import ValidationError
import json


class PromptGenerator():
    def __init__(self, prompt: str,  **mj_param):
        self.prompt_model = self.validate_prompt(prompt, **mj_param)

    def validate_prompt(self, prompt: str, **mj_param):
        return Prompt(prompt=prompt, **mj_param)

    def generate_prompt(self, prompt_model: Prompt):
        pass


class MidJourneyPromptGenerator(PromptGenerator):
    def __init__(self, prompt: str,  **mj_param):
        self.prompt_model = self.validate_prompt(
            prompt, **mj_param)
        self.prompt = self.generate_prompt(self.prompt_model)

    def validate_prompt(self, prompt: str, **mj_param):
        if "version" in mj_param:
            mj_param["version"] = str(mj_param["version"])
        try:
            prompt_model = MidJourneyPrompt(prompt=prompt, **mj_param)
        except ValidationError as e:
            print(e)
            raise e
        return prompt_model

    def generate_prompt(self, mj_prompt: MidJourneyPrompt) -> str:
        prompt_dict = json.loads(mj_prompt.model_dump_json())
        print(prompt_dict)
        prompt = prompt_dict["prompt"]
        for k, v in prompt_dict.items():
            if (k != "prompt") and (v):
                if (type(v) != bool):
                    prompt = prompt + " --" + str(k) + " " + str(v)
                else:
                    prompt = prompt + " --" + str(k)
        return prompt

    def dump_prompt(self) -> str:
        return self.prompt

    def __str__(self):
        return self.prompt

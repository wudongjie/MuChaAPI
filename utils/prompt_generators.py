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


def prompt_to_dict(prompts: str) -> dict:
    """
    Given a prompt with arguments, return a dict
    Example:
    "generate a cat name --fast --iw 1.0 --quality 1.0"
    return:
    {
    "prompt": "generate a cat name"
    "fast": True
    "iw": "1.0"
    "quality": "1.0"
    }
    """
    if " --" not in prompts:
        return {"prompt": prompts}
    prompt_list = prompts.split(" --")
    prompt_dict = {"prompt": prompt_list[0]}
    for i in range(1, len(prompt_list)):
        if (" " in prompt_list[i]):
            arg_list = prompt_list[i].split(" ")
            prompt_dict[arg_list[0]] = arg_list[1]
        else:
            prompt_dict[prompt_list[i]] = True
    return prompt_dict


def dict_to_prompt(prompt_dict: dict) -> str:
    """
    Given a prompt dict return a prompt with arguments
    Example:
    {
    "prompt": "generate a cat name"
    "fast": True
    "iw": "1.0"
    "quality": "1.0"
    }
    return:
        "generate a cat name --fast --iw 1.0 --quality 1.0"
    """
    if "prompt" not in prompt_dict:
        raise Exception("Prompt is not in the prompt dict")
    prompts = prompt_dict.pop("prompt")
    for key, item in prompt_dict.items():
        prompts = prompts + " --" + key
        if item == True:
            continue
        prompts = prompts + " " + item
    return prompts


def validate_prompt(**mj_param) -> list:
    if "version" in mj_param:
        mj_param["version"] = str(mj_param["version"])
    try:
        prompt_model = MidJourneyPrompt(**mj_param)
    except ValidationError as e:
        return convert_errors(e)
    return []


def convert_errors(e: ValidationError) -> list[str]:
    """
    Generate a list of errors messages in the following form:
    'Invalid Prompts: Your input [input] on the argument [arg] is invalid: [msg]'
    """
    error_msgs = []
    for error in e.errors():
        print(error)
        msg = "Invalid Prompts: Your input '" + \
            error["input"] + "' on the argument '" + \
            error["loc"][0] + "' is invalid: " + error["msg"]
        error_msgs.append(msg)
    return error_msgs


def gen_multiple_prompts(text: str) -> list[dict]:
    """
    Given a long text with multiple paragraphs, generate prompts per paragraphs
    Example:
    Input: 
    "Paragraph A

    Paragraph B

    Parapraph C

    --fast --version 4 --style 4a"
    Output:
    [{
    "prompt": "Paragraph A",
    "fast": True,
    "version": "4",
    "style": "4a"
    },
    {
    "prompt": "Paragraph B",
    "fast": True,
    "version": "4",
    "style": "4a"
    },
    {
    "prompt": "Paragraph C",
    "fast": True,
    "version": "4",
    "style": "4a"   
    }
    ]
    """
    text_list = text.splitlines()
    text_list = [x for x in text_list if x.strip() != ""]
    prompt_list = []
    args_dict = {}
    out_list = []
    for l in text_list:
        if "--" not in l:
            prompt_list.append(l)
            continue
        args = [i.strip() for i in l.split("--")]
        if args[0] != "":
            prompt_list.append(args[0])
        for i in range(1, len(args)):
            if (" " in args[i]):
                arg_list = args[i].split(" ")
                args_dict[arg_list[0]] = arg_list[1]
            else:
                args_dict[args[i]] = True
    # Generate a list of dict
    for prompt in prompt_list:
        args_dict["prompt"] = prompt
        out_list.append(args_dict.copy())
    print(out_list)
    return out_list

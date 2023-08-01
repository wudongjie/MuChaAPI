from fastapi import APIRouter, Depends
from config import Settings, get_settings
from typing_extensions import Annotated
import openai
from models.prompts import Prompt

gpt_api = APIRouter()


def sliding_windows(s: str, window_size):
    step_size = window_size // 2  # We want to overlap the windows

    strings = []
    for i in range(0, len(s) - window_size + 1, step_size):
        start = i
        end = min(i + window_size, len(s))
        strings.append(s[start:end])

    # Fix the last string to include the last characters
    if len(strings) > 1:
        last_start = len(s) - window_size
        last_end = len(s)
        strings[-1] = s[last_start:last_end]
    return strings


@gpt_api.post("/")
async def talk_to_chatgpt(prompt: Prompt,
                          settings: Annotated[Settings, Depends(get_settings)],
                          model: str = "text-davinci-003",
                          max_tokens: int = 300
                          ):
    openai.api_key = settings.openai_api_key
    response = openai.Completion.create(
        model=model,
        prompt=prompt.prompts,
        max_tokens=max_tokens)
    return response


@gpt_api.post("/summarize")
async def talk_to_chatgpt(prompt: Prompt,
                          settings: Annotated[Settings, Depends(get_settings)],
                          model: str = "text-davinci-003",
                          max_tokens: int = 300,
                          window_size: int = 1200
                          ):
    onests = "Summarize the following text in one short sentence \n"
    merged_content = onests + prompt.prompts
    openai.api_key = settings.openai_api_key
    while (len(merged_content) > window_size):
        texts = sliding_windows(merged_content, window_size)
        response_list = []
        for i in texts:
            merged = onests + i
            response = openai.Completion.create(
                model=model, prompt=merged)
            response_list.append(response.choices[0].text)
        # print(response_list)
        merged_content = '.'.join(response_list)
    to_sum = onests + merged_content
    response = openai.Completion.create(
        model=model, prompt=to_sum, max_tokens=max_tokens)
    return response

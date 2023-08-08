import pytest
from utils import MidJourneyPromptGenerator, prompt_to_dict, dict_to_prompt, validate_prompt
from pydantic import ValidationError


def test_generate_mjprompts():
    pg1 = MidJourneyPromptGenerator("hello world", version=4, style="4a")
    assert (pg1.dump_prompt() ==
            "hello world --iw 1.0 --quality 1.0 --style 4a --version 4")
    pg2 = MidJourneyPromptGenerator("hello world", fast=True)
    assert (pg2.dump_prompt() ==
            "hello world --fast --iw 1.0 --quality 1.0")
    pg3 = MidJourneyPromptGenerator(
        "hello world", chaos=20, iw=1.2, quality=0.75, repeat=28, seed=12378, stop=20)
    assert (pg3.dump_prompt() ==
            "hello world --chaos 20 --iw 1.2 --quality 0.75 --repeat 28 --seed 12378 --stop 20")
    with pytest.raises(ValidationError):
        pg4 = MidJourneyPromptGenerator(
            "hello world", chaos=1000
        )


def test_prompt_to_dict():
    prompts1 = "generate a cat name --iw 1.0 --quality 1.0 --style 4a --version 4 --fast"
    pmt_dict1 = {"prompt": "generate a cat name", "iw": "1.0",
                 "quality": "1.0", "style": "4a", "version": "4", "fast": True}
    assert prompt_to_dict(prompts1) == pmt_dict1
    assert validate_prompt(**pmt_dict1) == []
    assert dict_to_prompt(pmt_dict1) == prompts1
    prompts2 = "generate a cat name --fast --style 4a --version 4"
    pmt_dict2 = {"prompt": "generate a cat name",
                 "fast": True, "style": "4a", "version": "4"}
    assert prompt_to_dict(prompts2) == pmt_dict2
    assert validate_prompt(**pmt_dict2) == []
    assert dict_to_prompt(pmt_dict2) == prompts2
    pmt_dict2 = {"prompt": "hello world", "chaos": "1000"}
    assert validate_prompt(
        **pmt_dict2) == ["Invalid Prompts: Your input '1000' on the argument 'chaos' is invalid: Input should be less than or equal to 100"]

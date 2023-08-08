import pytest
from utils import MidJourneyPromptGenerator, prompt_to_dict, dict_to_prompt, validate_prompt, gen_multiple_prompts
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


def test_generate_multiple_prompts():
    prompts1 = """Paragraph A\n\nParagraph B\n\nParagraph C\n\n--fast --version 4 --style 4a"""
    pmt_list1 = [{"prompt": "Paragraph A", "fast": True, "version": "4", "style": "4a"},
                 {"prompt": "Paragraph B", "fast": True,
                     "version": "4", "style": "4a"},
                 {"prompt": "Paragraph C", "fast": True, "version": "4", "style": "4a"}]
    pmt_list_ex = gen_multiple_prompts(prompts1)
    assert pmt_list1[0] == pmt_list_ex[0]
    assert pmt_list1[1] == pmt_list_ex[1]
    assert pmt_list1[2] == pmt_list_ex[2]

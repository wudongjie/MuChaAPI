import pytest
from utils import MidJourneyPromptGenerator
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

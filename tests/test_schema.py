from models.schema import PromptOptions, ImagineRequest, ImagineData
from fastapi import testclient
import pytest


def test_promptoptions():
    pmtopt = PromptOptions(type=3, name="prompt", value="a man with a cat")
    assert pmtopt.type == 3
    assert pmtopt.name == "prompt"
    assert pmtopt.value == "a man with a cat"


def test_imaginedata():
    pmtopt = PromptOptions(type=3, name="prompt", value="a man with a cat")
    imgdata = ImagineData(version="1.0", id=2,
                          name="imagine", type=3, options=[pmtopt])
    assert imgdata.version == "1.0"
    assert imgdata.id == 2
    assert imgdata.name == "imagine"
    assert imgdata.type == 3
    assert imgdata.options == [pmtopt]
    assert type(imgdata.options) == list

import pytest
from payloads import ImaginePayload, ChatGPTPayload
from models import InteractionRequest
from config import Settings, get_settings


setting = get_settings()


def test_imagine_payload():
    img_payload = ImaginePayload(setting, "good")
    print(img_payload.model_dump())
    assert type(img_payload.to_pydantic()) == InteractionRequest


def test_chatgpt_payload():
    img_payload = ChatGPTPayload(setting, "good")
    print(img_payload.model_dump())
    assert type(img_payload.to_pydantic()) == InteractionRequest


def test_chatgpt_payload():
    img_payload = ImaginePayload(setting, "good")
    print(img_payload.model_dump())
    assert type(img_payload.to_pydantic()) == InteractionRequest

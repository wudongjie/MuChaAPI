from config import Settings, get_settings
from typing_extensions import Annotated
from fastapi import Depends
import random
from models import InteractionRequest


class Payload:
    def __init__(self, settings: Annotated[Settings, Depends(get_settings)]):
        self.application_id = settings.application_id
        self.guild_id = settings.guild_id
        self.channel_id = settings.channel_id
        self.session_id = settings.session_id

    def model_dump(self):
        return {
            "application_id": self.application_id,
            "guild_id": self.guild_id,
            "channel_id": self.channel_id,
            "session_id": self.session_id
        }


class ImaginePayload(Payload):
    def __init__(self, settings: Annotated[Settings, Depends(get_settings)], prompt: str):
        super().__init__(settings)
        self.prompt = prompt

    def model_dump(self) -> dict:
        return {
            "id": random.randint(100000000, 900000000),
            "type": 2,
            "application_id": self.application_id,
            "guild_id": self.guild_id,
            "channel_id": self.channel_id,
            "session_id": self.session_id,
            "data": {
                "version": "1118961510123847772",
                "id": "938956540159881230",
                "name": "imagine",
                "type": 1,
                "options": [
                    {"type": 3,
                     "name": "prompt",
                     "value": self.prompt}
                ]
            }
        }

    def to_pydantic(self) -> InteractionRequest:
        payload = self.model_dump()
        pyd = InteractionRequest(**payload)
        return pyd


class ChatGPTPayload(Payload):
    def __init__(self, settings: Annotated[Settings, Depends(get_settings)], prompt: str):
        super().__init__(settings)
        self.prompt = prompt

    def model_dump(self) -> dict:
        return {
            "id": random.randint(100000000, 900000000),
            "type": 2,
            "application_id": self.application_id,
            "guild_id": self.guild_id,
            "channel_id": self.channel_id,
            "session_id": self.session_id,
            "data": {
                "version": "1136467100832124998",
                "id": "1133969668399452192",
                "name": "chatgpt",
                "type": 1,
                "options": [
                    {"type": 3,
                     "name": "prompt",
                     "value": self.prompt}
                ]
            }
        }

    def to_pydantic(self) -> InteractionRequest:
        payload = self.model_dump()
        pyd = InteractionRequest(**payload)
        return pyd


class SummarizePayload(Payload):
    def __init__(self, settings: Annotated[Settings, Depends(get_settings)], prompt: str):
        super().__init__(settings)
        self.prompt = prompt

    def model_dump(self) -> dict:
        return {
            "id": random.randint(100000000, 900000000),
            "type": 2,
            "application_id": self.application_id,
            "guild_id": self.guild_id,
            "channel_id": self.channel_id,
            "session_id": self.session_id,
            "data": {
                "version": "1136468928219070536",
                "id": "1136468928219070535",
                "guild_id": self.guild_id,
                "name": "summarize",
                "type": 1,
                "options": [
                    {"type": 3,
                     "name": "prompt",
                     "value": self.prompt}
                ]
            }
        }

    def to_pydantic(self) -> InteractionRequest:
        payload = self.model_dump()
        pyd = InteractionRequest(**payload)
        return pyd


class TestPayload(Payload):
    def __init__(self, settings: Annotated[Settings, Depends(get_settings)], arg: str):
        super().__init__(settings)
        self.arg = arg

    def model_dump(self) -> dict:
        return {
            "id": random.randint(100000000, 900000000),
            "type": 2,
            "application_id": self.application_id,
            "guild_id": self.guild_id,
            "channel_id": self.channel_id,
            "session_id": self.session_id,
            "data": {
                "version": "1135434235382079509",
                "id": "1135434235382079508",
                "guild_id": self.guild_id,
                "name": "test",
                "type": 1,
                "options": [
                    {"type": 3,
                     "name": "prompt",
                     "value": self.arg}
                ]
            }
        }

    def to_pydantic(self) -> InteractionRequest:
        payload = self.model_dump()
        pyd = InteractionRequest(**payload)
        return pyd

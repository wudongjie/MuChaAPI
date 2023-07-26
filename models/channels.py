from __future__ import annotations
from pydantic import BaseModel


class Channel(BaseModel):
    id: int
    type: int
    guild_id: int | None = None
    position:  int
    name: str | None = None


class ChannelMention(BaseModel):
    id: int
    guild_id: int
    type: int
    name: str

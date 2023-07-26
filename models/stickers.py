from __future__ import annotations
from pydantic import BaseModel
from enum import IntEnum
from .users import User


class StickerType(IntEnum):
    STANDARD = 1
    GUILD = 2


class StickerFormatType(IntEnum):
    PNG = 1
    APNG = 2
    LOTTIE = 3
    GIF = 4


class Sticker(BaseModel):
    id: int
    pack_id: int | None = None
    name: str
    description: str = ""
    tags: str
    asset: str | None = None
    type: StickerType
    format_type: StickerFormatType
    available: bool | None = None
    guild_id: int | None = None
    user: User | None = None
    sort_value: int | None = None

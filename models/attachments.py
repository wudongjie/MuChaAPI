from __future__ import annotations
from pydantic import BaseModel
from enum import IntEnum


class AttachmentFlag(IntEnum):
    IS_REMIX = 1 << 2


class Attachment(BaseModel):
    id: int
    filename: str
    description: str | None = None
    content_type: str | None = None
    size: int
    url: str
    proxy_url: str | None = None
    height: int | None = None
    width: int | None = None
    ephemeral: bool | None = None
    duration_secs: float | None = None
    waveform: str | None = None
    flags: AttachmentFlag | None = None

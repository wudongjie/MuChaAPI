from enum import Enum
from pydantic import BaseModel


class EmbedType(str, Enum):
    rich = "rich"
    image = "image"
    video = "video"
    gifv = "gifv"
    article = "article"
    link = "link"


class EmbedThumbnail(BaseModel):
    url: str
    proxy_url: str | None = None
    height: int | None = None
    width: int | None = None


class EmbedVideo(BaseModel):
    url: str | None = None
    proxy_url: str | None = None
    height: int | None = None
    width: int | None = None


class EmbedImage(BaseModel):
    url: str
    proxy_url: str | None = None
    height: int | None = None
    width: int | None = None


class EmbedProvider(BaseModel):
    name: str | None = None
    url: str | None = None


class EmbedAuthor(BaseModel):
    name: str
    url: str | None = None
    icon_url: str | None = None
    proxy_icon_url: str | None = None


class EmbedFooter(BaseModel):
    text: str
    icon_url: str | None = None
    proxy_icon_url: str | None = None


class EmbedField(BaseModel):
    name: str
    value: str
    inline: bool | None = None

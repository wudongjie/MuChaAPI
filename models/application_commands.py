from __future__ import annotations
from pydantic import BaseModel
from .enum_model import ApplicationCommandType, Locale, ApplicationCommandOptionType, ChannelType


class ApplicationCommandOptionChoice(BaseModel):
    name: str
    name_localizations: dict[Locale, str] | None = None
    value: str | int | float


class ApplicationCommandOption(BaseModel):
    type: ApplicationCommandOptionType
    name: str
    name_localizations: dict[Locale, str] | None = None
    description: str = ""
    description_localizations: dict[Locale, str] | None = None
    required: bool | None = None
    choices: list[ApplicationCommandOptionChoice] | None = None
    options: list[ApplicationCommandOption] | None = None
    channel_types: list[ChannelType] | None = None
    min_value: int | float | None = None
    max_value: int | float | None = None
    min_length: int | None = None
    max_length: int | None = None
    autocomplete: bool | None = None


class ApplicationCommand(BaseModel):
    id: int
    type: ApplicationCommandType = 1
    application_id: int
    guild_id: int | None = None
    name: str | None = None
    name_localizations: dict[Locale, str] | None = None
    description: str = ""
    description_localizations: dict[Locale, str] | None = None
    options: list[ApplicationCommandOption] | None = None
    default_member_permissions: str = ""
    dm_permission: bool | None = None
    default_permission: bool | None = None
    nsfw: bool | None = None
    version: int

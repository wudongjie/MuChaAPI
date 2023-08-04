from __future__ import annotations

from pydantic import BaseModel

from .channels import Channel
from .enum_model import InteractionType, InteractionResponseType
from .guilds import GuildMember
from .interaction_data import InteractionData, ApplicationCommandData
from .messages import Message
from .users import User


class Interaction(BaseModel):
    id: int
    application_id: int
    type: InteractionType
    data: ApplicationCommandData | None = None
    guild_id: int | None = None
    channel: Channel | None = None
    channel_id: int | None = None
    member: GuildMember | None = None
    user: User | None = None
    token: str
    version: int = 1
    message: Message | None = None
    app_permissions: str | None = None
    locale: str | None = None
    guild_locale: str | None = None
    # session_id: str


class InteractionRequest(BaseModel):
    id: int
    type: InteractionType
    application_id: int
    data: InteractionData | None = None
    guild_id: int | None = None
    channel: Channel | None = None
    channel_id: int | None = None
    session_id: str
    version: int = 1


class InteractionResponse(BaseModel):
    type: InteractionResponseType
    data: InteractionData | None = None

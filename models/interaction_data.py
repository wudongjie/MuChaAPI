from __future__ import annotations
from typing import Any, List

from pydantic import BaseModel, Field
from .allowed_mentions import AllowedMention
from .attachments import Attachment
from .channels import Channel
from .embeds import Embed
from .guilds import GuildMember
from .messages import Component, Message, MessageFlags
from .roles import Role
from .users import User
from .enum_model import InteractionType, InteractionResponseType, ApplicationCommandType
from .message_types import ComponentType
from .emojis import Emoji


class InteractionDataOptions(BaseModel):
    name: str
    type: int
    value: Any
    options: List[InteractionDataOptions] = []
    focused: bool | None = None


class SelectOption(BaseModel):
    label: str
    value: str
    description: str | None = None
    emoji: Emoji | None = None
    default: bool | None = None


class InteractionData(BaseModel):
    pass


class ResolvedData(InteractionData):  # Check about partial!
    users: User | None = None
    members: GuildMember | None = None
    roles: Role | None = None
    channels: Channel | None = None
    messages: Message | None = None
    attachments: Attachment | None = None


class ApplicationCommandData(InteractionData):
    id: int
    name: str
    type: ApplicationCommandType
    version: int = 1
    resolved: ResolvedData | None = None
    options: List[InteractionDataOptions] | None = None
    guild_id: int | None = None
    target_id: int | None = None


class MessageComponentData(InteractionData):
    custom_id: str
    component_type: ComponentType
    values: list[SelectOption] | None = None


class ModalSubmitData(InteractionData):
    custom_id: str
    components: list[Component]


class InteractionResponseData(InteractionData):
    tts: bool | None = None
    content: str | None = None
    embeds: list[Embed] | None = None
    allowed_mentions: AllowedMention | None = None
    flags: MessageFlags | None = None
    components: list[Component] | None = None
    attachments: list[Attachment] | None = None

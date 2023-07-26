from __future__ import annotations
from datetime import datetime
from typing import Any
from pydantic import BaseModel, Field
from .channels import ChannelMention, Channel
from .embeds import Embed
from .reactions import Reaction
from .attachments import Attachment
from .applications import Application
from .users import User
from .stickers import Sticker
from .enum_model import InteractionType
from .guilds import GuildMember
from .message_types import *
from .allowed_mentions import AllowedMention


class Component(BaseModel):
    type: ComponentType
    components: list[Component] = []


class MessageActivity(BaseModel):
    type: MessageActivityType
    party_id: str


class MessageInteraction(BaseModel):
    id: int
    type: InteractionType
    name: str
    user: User
    member: GuildMember


class MessageReference(BaseModel):
    message_id: int | None = None
    channel_id: int | None = None
    guild_id: int | None = None
    fail_if_not_exists: bool | None = None


class RoleSubscriptionData(BaseModel):
    role_subscription_listing_id: int
    tier_name: str
    total_months_subscribed: int
    is_renewal: bool


class MessageRequest(BaseModel):
    content: str | None = None
    nonce: str | int | None = None
    tts: bool | None = None
    embeds: Embed | None = None
    allowed_mentions: AllowedMention | None = None
    message_reference: MessageReference | None = None
    components: list[Component] | None = None
    sticker_ids: list[int] | None = None
    files: Any = Field(alias='files[n]', default=None)
    payload_json: str | None = None
    attachments: list[Attachment] | None = None
    flags: MessageFlags | None = None


class Message(BaseModel):
    id: int
    channel_id: int
    author: User
    content: str
    timestamp: datetime
    edited_timestamp: datetime | None
    tts: bool
    mention_everyone: bool
    mentions: list[User] = []
    mention_roles: list[int] = []
    mention_channels: list[ChannelMention] = []
    attachments: list[Attachment] = []
    embeds: list[Embed] = []
    reactions: list[Reaction] = []
    nonce: int | str | None = None
    pinned: bool
    webhook_id: int | None = None
    type: int
    activity: MessageActivity | None = None
    application: Application | None = None
    application_id: int | None = None
    message_reference: MessageReference | None = None
    flags: int | None = None
    referenced_message: Message | None = None
    interaction: MessageInteraction | None = None
    thread: Channel | None = None
    components: list[Component] | None = None   # fix this
    sticker_items: list[Sticker] | None = None
    position: int | None = None
    role_subscription_data: RoleSubscriptionData | None = None

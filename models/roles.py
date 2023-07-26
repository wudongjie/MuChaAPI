from __future__ import annotations
from pydantic import BaseModel


class RoleTags(BaseModel):
    bot_id: int | None = None
    integration_id: int | None = None
    premium_subscriber: bool | None = None
    subscription_listing_id: int | None = None
    available_for_purchase: bool | None = None
    guild_connections: bool | None = None


class Role(BaseModel):
    id: int
    name: str
    color: int
    hoist: bool
    icon: str | None = None
    unicode_emoji: str | None = None
    position: int
    permissions: str
    managed: bool
    mentionable: bool
    tags: RoleTags | None = None
    flags: int

from __future__ import annotations
from pydantic import BaseModel
from .emojis import Emoji
from .roles import Role
from .users import User
from datetime import datetime
from .stickers import Sticker
from .enum_model import GuildFeatures, GuildMemberFlags, GuildNSFWLevel, VerificationLevel, MessageNotificationLevel, MFALevel, ExplicitContentFilterLevel, PremiumTier


class WelcomeScreenChannel(BaseModel):
    channel_id: int
    description: str = ""
    emoji_id: int | None = None
    emoji_name: str | None = None


class WelcomeScreen(BaseModel):
    description: str | None = None
    welcome_channels: list[WelcomeScreenChannel]


class GuildMember(BaseModel):
    user: User
    nick: str | None = None
    avatar: str | None = None
    roles: list[int]
    joined_at: datetime
    premium_since: datetime | None = None
    deaf: bool
    mute: bool
    flags: GuildMemberFlags = 0
    pending: bool | None = None
    permissions: str | None = None
    communication_disabled_until: datetime | None = None


class Guild(BaseModel):
    id: int
    name: str
    icon: str | None = None
    icon_hash: str | None = None
    splash: str | None = None
    discovery_splash: str | None = None
    owner: bool | None = None
    owner_id: int
    permissions: str | None = None
    region: str | None = None
    afk_channel_id: int | None = None
    afk_timeout: int
    widget_enabled: bool | None = None
    widget_channel_id: int | None = None
    verification_level: VerificationLevel
    default_message_notifications: MessageNotificationLevel
    explicit_content_filter: ExplicitContentFilterLevel
    roles: list[Role] = []
    emojis: list[Emoji] = []
    features: list[GuildFeatures] = []
    mfa_level: MFALevel
    application_id: int | None = None
    system_channel_id: int | None = None
    system_channel_flags: int
    rules_channel_id: int | None = None
    max_presences: int | None = None
    max_members: int | None = None
    vanity_url_code: str = ""
    description: str = ""
    banner: str = ""
    premium_tier: PremiumTier
    premium_subscription_count: int | None = None
    preferred_locale: str
    public_updates_channel_id: int | None = None
    max_video_channel_users: int | None = None
    max_stage_video_channel_users: int | None = None
    approximate_member_count: int | None = None
    approximate_presence_count: int | None = None
    welcome_screen: WelcomeScreen | None = None
    nsfw_level: GuildNSFWLevel
    stickers: list[Sticker] | None = None
    premium_progress_bar_enabled: bool
    safety_alerts_channel_id: int | None = None

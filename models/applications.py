from __future__ import annotations
from pydantic import BaseModel
from .users import User
from .teams import Team
from .guilds import Guild


class InstallParams(BaseModel):
    scopes: list[str] = []
    permissions: str


class Application(BaseModel):
    id: int
    name: str
    icon: str | None = None
    description: str
    rpc_origins: list[str] = []
    bot_public: bool
    bot_require_code_grant: bool
    terms_of_service_url: str | None = None
    privacy_policy_url: str | None = None
    owner: User | None = None
    summary: str = ""
    verify_key: str
    team: Team | None = None
    guild_id: int | None = None
    guild: Guild | None = None
    primary_sku_id: int | None = None
    slug: str | None = None
    cover_image: str | None = None
    flags: int | None = None
    approximate_guild_count: int | None = None
    tags: list[str] = []
    install_params: InstallParams | None = None
    custom_install_url: str | None = None
    role_connections_verification_url: str | None = None

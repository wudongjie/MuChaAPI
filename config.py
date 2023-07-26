from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache


class Settings(BaseSettings):
    discord_token: str
    user_token: str
    guild_id: int
    channel_id: int
    application_id: int
    imagine_id: int = 938956540159881230
    session_id: str = "0deb67ca254c9362f66f4540d843598e"
    version_id: int = 1118961510123847772
    openai_api_key: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings():
    return Settings()

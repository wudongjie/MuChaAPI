from pydantic import BaseModel
from .message_types import AllowedMentionType


class AllowedMention(BaseModel):
    parse: list[AllowedMentionType]
    roles: list[str]
    users: list[str]
    replied_user: bool

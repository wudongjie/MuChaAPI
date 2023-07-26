from pydantic import BaseModel
from .users import User
from .roles import Role


class Emoji(BaseModel):
    id: int | None
    name: str | None
    roles: list[Role] = []
    user: User | None = None
    require_colons: bool | None = None
    managed: bool | None = None
    animated: bool | None = None
    available: bool | None = None

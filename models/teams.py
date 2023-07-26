from __future__ import annotations
from pydantic import BaseModel
from .users import User
from .enum_model import MembershipState


class TeamMember(BaseModel):
    membership_state: MembershipState
    permissions: list[str] = ["*"]
    team_id: int
    user: User


class Team(BaseModel):
    icon: str | None = None
    id: int
    members: list[TeamMember]
    name: str
    owner_user_id: int

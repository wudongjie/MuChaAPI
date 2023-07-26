from pydantic import BaseModel
from models import Emoji


class Reaction(BaseModel):
    count: int
    me: bool
    emoji: Emoji

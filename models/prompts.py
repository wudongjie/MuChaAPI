from pydantic import BaseModel, Field
from typing import Annotated
from .enum_model import MidJourneyPromptStyle, MidJourneyPromptVersion


class Prompt(BaseModel):
    prompt: str


class MidJourneyPrompt(Prompt):
    aspect: str | None = None
    chaos: Annotated[int, Field(ge=0, le=100)] | None = None
    fast: bool | None = None
    iw: Annotated[float, Field(ge=0, le=2)] = 1.0
    no: str | None = None
    quality: Annotated[float, Field(gt=0, le=1)] = 1.0
    relax: bool | None = None
    repeat: Annotated[int, Field(ge=1, le=40)] | None = None
    seed: Annotated[int, Field(ge=0, le=4294967295)] | None = None
    stop: Annotated[int, Field(ge=10, le=100)] | None = None
    style: MidJourneyPromptStyle | None = None
    stylize: int | None = None
    tile: bool | None = None
    turbo: bool | None = None
    weird: Annotated[int, Field(ge=0, le=3000)] | None = None
    niji: bool | None = None
    version: MidJourneyPromptVersion | None = None

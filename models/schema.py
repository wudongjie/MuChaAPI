from pydantic import BaseModel, Field


class PromptOptions(BaseModel):
    type: int
    name: str
    value: str = Field(title="The prompt for mid journey api", max_length=300)


class ImagineData(BaseModel):
    version: str
    id: int
    name: str
    type: int
    options: list[PromptOptions]
    attachments: list = []


class ImagineRequest(BaseModel):
    id: int = 1000000
    type: int
    application_id: int
    guild_id: int
    channel_id: int
    session_id: str
    data: ImagineData


class ImagineResponse(BaseModel):
    status_code: str
    msg: str

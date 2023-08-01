from pydantic import BaseModel


class Prompt(BaseModel):
    prompts: str

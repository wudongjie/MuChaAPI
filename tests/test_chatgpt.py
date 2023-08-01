import pytest
from fastapi.testclient import TestClient

from app import app
from models.prompts import Prompt

client = TestClient(app)


def test_chatgpt_post():
    req = Prompt(prompts="generate a cat name")

    response = client.post("/chatgpt/",
                           json=req.model_dump())
    assert response.status_code == 200
    assert type(response.json()['choices'][0]['text']) == str


def test_chatgpt_summarize():
    prompt1 = Prompt(prompts="generate a story")
    response = client.post("/chatgpt", json=prompt1.model_dump())
    assert response.status_code == 200
    story = response.json()['choices'][0]['text']
    prompt2 = Prompt(prompts=story)
    response = client.post("/chatgpt/summarize",
                           json=prompt2.model_dump())
    assert response.status_code == 200
    assert type(response.json()['choices'][0]['text']) == str

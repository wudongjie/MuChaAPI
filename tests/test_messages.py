from fastapi.testclient import TestClient
import pytest
from app import app
import os
from models import Message

client = TestClient(app)


def test_midjourney_create_messages():
    message = "Hello World!"
    response = client.post("/midjourney/messages?text=" + message)
    assert response.json()['content']['edited_timestamp'] == None
    message = Message(**response.json()['content'])
    assert response.status_code == 200
    assert response.json()['msg'] == "Message created!"
    assert type(message).__name__ == "Message"

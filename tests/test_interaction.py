from fastapi.testclient import TestClient
import pytest
from app import app
from midjourney import midjourney
import os
from models.interactions import InteractionType
client = TestClient(app)


def test_midjourney_interactions_ping():
    header = {
        "Content-Type": "application/json",
        'authorization': os.environ['AUTHORIZATION']
    }
    req = {
        'id': 100001,
        'type': InteractionType.PING,
        'application_id': os.environ['APPLICATION_ID'],
        'token': "fjdskfjakj",
        'version': os.environ['VERSION_ID']
    }
    response = client.post("/midjourney/interactions",
                           headers=header,
                           json=req)
    assert response.status_code == 200
    assert response.json() == {"type": 1, "msg": "Pong"}

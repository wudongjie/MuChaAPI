from fastapi.testclient import TestClient
import pytest
from app import app
from midjourney import midjourney
import os
from models.interactions import InteractionType, Interaction
from models.interaction_data import ApplicationCommandData, InteractionDataOptions
from httpx import AsyncClient
from config import Settings, get_settings
client = TestClient(app)


def test_midjourney_interactions_ping():
    setting = get_settings()
    req = {
        'id': 100001,
        'type': 1,
        'application_id': setting.application_id,
        'token': "fjdskfjakj",
        'version': setting.version_id
    }
    response = client.post("/midjourney/interactions",
                           json=req)
    assert response.status_code == 200
    assert response.json() == {"type": 1, "msg": "Pong"}


# @pytest.mark.anyio
# async def test_midjourney_interactions_test():
#     # req = {
#     #     'id': 100003,
#     #     'guild_id': os.environ['GUILD_ID'],
#     #     'session_id': os.environ['SESSION_ID'],
#     #     'channel_id': os.environ['CHANNEL_ID'],
#     #     'type': 2,
#     #     'data': {'id': 1135434235382079508, 'name': 'test', 'type': 1, 'guild_id': os.environ['GUILD_ID']},
#     #     'application_id': os.environ['APPLICATION_ID'],
#     #     'token': "fjdskfjakj",
#     #     'version': os.environ['VERSION_ID']
#     # }
#     setting = get_settings()
#     req = {
#         "id": 12312232,
#         "type": 2,
#         "application_id": setting.application_id,
#         "guild_id": setting.guild_id,
#         "channel_id": setting.channel_id,
#         "session_id": "775609e8d69984c682e58527ab9fbec5",
#         "data": {"version": "1135434235382079509",
#                  "id": "1135434235382079508",
#                  "guild_id": setting.guild_id,
#                  "name": "test",
#                  "type": 1,
#                  "options": [{"type": 3, "name": "arg", "value": "a"}]},
#         "token": "dfjkadsjfk",
#         "version": setting.version_id
#     }
#     interaction = InteractionRequest(**req)
#     assert type(interaction) == InteractionRequest
#     async with AsyncClient(app=app, base_url="http://127.0.0.1:8000/") as session:
#         resp = await session.post("/midjourney/interactions",
#                                   json=req)
#     assert resp.status_code == 200
#     assert await resp.json() == {"type": 2, "msg": "Pong"}
#     return


def test_midjourney_interactions_test():
    setting = get_settings()
    req = {"id": 213123123,
           "version": 1,
           "type": 2,
           "token": "hsdjfasdjf",
           "application_id": "1128110065900081334",
           "guild_id": setting.guild_id,
           "channel_id": setting.channel_id,
           "session_id": "077cc0c4b93a7090a4e80229f33a8089",
           "data": {"version": "1135434235382079509",
                    "id": "1135434235382079508",
                    "guild_id": setting.guild_id,
                    "name": "test",
                    "type": 1,
                    "options": [{"type": 3, "name": "arg", "value": "a"}]}}
    interaction = Interaction(**req)
    assert type(interaction) == Interaction
    response = client.post("/midjourney/interactions",
                           json=interaction.model_dump())
    assert response.status_code == 200
    assert response.json() == {"msg": "Interaction created!"}

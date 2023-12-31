from fastapi.testclient import TestClient
import pytest
from app import app
from midjourney import midjourney
import os
from models.interactions import InteractionType, InteractionRequest
from models.interaction_data import ApplicationCommandData, InteractionDataOptions
from httpx import AsyncClient
from config import Settings, get_settings
from payloads import TestPayload
client = TestClient(app)
setting = get_settings()


def test_midjourney_interactions_ping():
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

# @pytest.mark.anyio
# async def test_midjourney_interactions_test():
#     setting = get_settings()
#     header = {
#         "Content-Type": "application/json",
#         'authorization': setting.user_token
#     }
#     req = {"id": 123712937,
#            "type": 2,
#            "application_id": "1128110065900081334",
#            "guild_id": "1125988642519785584",
#            "channel_id": "1125988643178299425",
#            "session_id": "1c1b1a9ee11d3db4d480507e3e953be2",
#            "data": {"version": "1135434235382079509",
#                     "id": "1135434235382079508",
#                     "guild_id": "1125988642519785584",
#                     "name": "test",
#                     "type": 1,
#                     "options": [],
#                     "application_command": {"id": "1135434235382079508",
#                                             "application_id": "1128110065900081334",
#                                             "version": "1135434235382079509",
#                                             "default_member_permissions": None, "type": 1,
#                                             "nsfw": False, "name": "test", "description": "Test",
#                                             "guild_id": "1125988642519785584",
#                                             "options": [{"type": 3, "name": "arg", "description": "…"}]},
#                     "attachments": []}, "nonce": "1136523667631505408"}

#     interaction = InteractionRequest(**req)
#     assert interaction.type == 2
#     assert type(interaction) == InteractionRequest
#     async with AsyncClient(app=app) as session:
#         resp = await session.post("https://discord.com/api/v9/interactions",
#                                   json=interaction.model_dump(),
#                                   headers=header)
#         assert resp.status_code == 200
#         assert resp.json() == {"msg": "Interaction created!"}

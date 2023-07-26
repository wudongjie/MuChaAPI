from fastapi import APIRouter, Depends
from models.schema import ImagineRequest, PromptOptions, ImagineData, ImagineResponse
from models.messages import MessageRequest
import aiohttp
import random
from models.interactions import InteractionRequest, InteractionType, InteractionResponseType
from config import Settings, get_settings
from typing_extensions import Annotated


mj_api = APIRouter()


@mj_api.post("/imagine", )
async def midjourney_imagine(prompt: str, settings: Annotated[Settings, Depends(get_settings)]):
    header = {
        "Content-Type": "application/json",
        'authorization': settings.user_token
    }

    id = random.randint(1000000, 9000000)
    options = PromptOptions(type='3', name='prompt', value=prompt)
    data = ImagineData(
        version=settings.version_id,
        id=settings.imagine_id,
        name='imagine',
        type='1',
        options=[options]
    )
    payroad = ImagineRequest(
        id=id,
        type='2',
        application_id=settings.application_id,
        guild_id=settings.guild_id,
        channel_id=settings.channel_id,
        session_id=settings.session_id,
        data=data
    )
    json_payroad = payroad.model_dump()
    print(json_payroad)
    async with aiohttp.ClientSession() as session:
        async with session.post('https://discord.com/api/v9/interactions',
                                json=json_payroad,
                                headers=header) as resp:
            if resp.status == 200:
                return {
                    "status_code": resp.status,
                    "content": await resp.text(),
                    "msg": "Imagine job launched successfully"
                }
            else:
                return {
                    "status_code": resp.status,
                    "content": await resp.text(),
                    "msg": "Imagine job failed"
                }


@mj_api.post("/interactions")
async def midjourney_interactions(req: InteractionRequest):
    if req.type == 1:
        return {
            'type': InteractionResponseType.PONG,
            'msg': 'Pong'
        }
    else:
        return {
            'type': 0,
            'msg': 'interaction failed!'
        }


@mj_api.post("/messages")
async def midjourney_create_messages(text: str, settings: Annotated[Settings, Depends(get_settings)]):
    header = {
        "Content-Type": "application/json",
        'authorization': settings.user_token
    }
    req = MessageRequest(content=text)
    req_url = 'https://discord.com/api/v9/channels/' + \
        str(settings.channel_id) + "/messages"
    async with aiohttp.ClientSession() as session:
        async with session.post(req_url,
                                json=req.model_dump(),
                                headers=header) as resp:
            if resp.status == 200:
                return {
                    "status_code": resp.status,
                    "content": await resp.json(),
                    "msg": "Message created!"
                }
            else:
                return {
                    "status_code": resp.status,
                    "content": await resp.json(),
                    "msg": "Create message failed"
                }
# @mj_api.get("/imagine/{id}")
# async def midjourney_get_imagine_by_id(id: int):
#     application_id = os.environ['APPLICATION_ID']
#     interaction_id = id
#     header = {
#         "Content-Type": "application/json",
#         'authorization': os.environ['AUTHORIZATION']
#     }
#     url = "https://discord.com/api/webhooks/1131841279530119228/UmyRz0gMtCgjAxLEUzve1rZffiB2UNXWEzwqj6wZ8NyAe74Q168wWg4s_L77-1EhJClu/messages/1131839929572405303"
#     # url = 'https://discord.com/api/v9/webhooks/' + \
#     #     str(application_id) + '/' + str(id) + '/' + 'messages/@original'
#     # print(url)
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url,
#                                headers=header) as resp:
#             if resp.status == 200:
#                 return {
#                     "status_code": resp.status,
#                     "content": await resp.json(),
#                     "msg": "Imagine job launched successfully"
#                 }
#             else:
#                 return {
#                     "status_code": resp.status,
#                     "content": await resp.json(),
#                     "msg": "Imagine job failed"
#                 }

from models.schema import PromptOptions, ImagineRequest, ImagineData
from fastapi import testclient
from models import Interaction
import pytest


def test_promptoptions():
    pmtopt = PromptOptions(type=3, name="prompt", value="a man with a cat")
    assert pmtopt.type == 3
    assert pmtopt.name == "prompt"
    assert pmtopt.value == "a man with a cat"


def test_imaginedata():
    pmtopt = PromptOptions(type=3, name="prompt", value="a man with a cat")
    imgdata = ImagineData(version="1.0", id=2,
                          name="imagine", type=3, options=[pmtopt])
    assert imgdata.version == "1.0"
    assert imgdata.id == 2
    assert imgdata.name == "imagine"
    assert imgdata.type == 3
    assert imgdata.options == [pmtopt]
    assert type(imgdata.options) == list


def test_interaction():
    payload = {
        "type": 2,
        "token": "A_UNIQUE_TOKEN",
        "member": {
            "user": {
                "id": "53908232506183680",
                "username": "Mason",
                "avatar": "a_d5efa99b3eeaa7dd43acca82f5692432",
                "discriminator": "1337",
                "public_flags": 131141
            },
            "roles": ["539082325061836999"],
            "premium_since": None,
            "permissions": "2147483647",
            "pending": False,
            "nick": None,
            "mute": False,
            "joined_at": "2017-03-13T19:19:14.040000+00:00",
            "is_pending": False,
            "deaf": False
        },
        "id": "786008729715212338",
        "channel_id": "645027906669510667",
        "application_id": "123918239123",
        "guild_id": "290926798626357999",
        "app_permissions": "442368",
        "guild_locale": "en-US",
        "locale": "en-US",
        "data": {
            "options": [{
                "type": 3,
                "name": "cardname",
                "value": "The Gitrog Monster"
            }],
            "type": 1,
            "name": "cardsearch",
            "id": "771825006014889984"
        }
    }
    req = Interaction(**payload)
    assert type(req) == Interaction

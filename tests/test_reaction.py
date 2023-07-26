import pytest
from fastapi import testclient

from models import Emoji, Reaction, Role


def test_reactions():
    role1 = Role(id=21321389, name="role1", color=1, hoist=True,
                 position=1, permissions="*", managed=True, mentionable=True, flags=1)
    emoji1 = Emoji(id=1, name="haha", roles=[role1])
    reaction1 = Reaction(count=1, me=True, emoji=emoji1)
    assert reaction1.count == 1
    assert reaction1.me == True
    assert reaction1.emoji == emoji1

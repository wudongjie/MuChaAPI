from enum import IntEnum, Enum


class ComponentType(IntEnum):
    ACTIONROW = 1
    BUTTON = 2
    STRINGSELECT = 3
    TEXTINPUT = 4
    USERSELECT = 5
    ROLESELECT = 6
    MENTIONABLESELECT = 7
    CHANNELSELECT = 8


class MessageActivityType(IntEnum):
    JOIN = 1
    SPECTATE = 2
    LISTEN = 3
    JOIN_REQUEST = 4


class MessageFlags(IntEnum):
    CROSSPOSTED = 1 << 0
    IS_CROSSPOST = 1 << 1
    SUPPRESS_EMBEDS = 1 << 2
    SOURCE_MESSAGE_DELETED = 1 << 3
    URGENT = 1 << 4
    HAS_THREAD = 1 << 5
    EPHEMERAL = 1 << 6
    LOADING = 1 << 7
    FAILED_TO_MENTION_SOME_ROLES_IN_THREAD = 1 << 8
    SUPPRESS_NOTIFICATIONS = 1 << 12
    IS_VOICE_MESSAGE = 1 << 13


class AllowedMentionType(str, Enum):
    RoleMentions = "roles"
    UserMentions = "users"
    EveryoneMentions = "everyone"

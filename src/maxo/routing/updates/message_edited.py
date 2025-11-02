from datetime import datetime

from maxo.enums import UpdateType
from maxo.routing.updates.base import MaxUpdate
from maxo.types.message import Message


class MessageEdited(MaxUpdate):
    type = UpdateType.MESSAGE_EDITED

    timestamp: datetime
    message: Message

from datetime import datetime

from maxo.enums import UpdateType
from maxo.routing.updates.base import MaxUpdate
from maxo.types.message import Message


class MessageCreated(MaxUpdate):
    type = UpdateType.MESSAGE_CREATED

    message: Message
    timestamp: datetime
    user_locale: str | None = None

from datetime import datetime

from maxo.enums import UpdateType
from maxo.routing.updates.base import MaxUpdate


class MessageRemoved(MaxUpdate):
    type = UpdateType.MESSAGE_REMOVED

    timestamp: datetime
    message_id: str | None = None
    chat_id: str | None = None
    user_id: int | None = None

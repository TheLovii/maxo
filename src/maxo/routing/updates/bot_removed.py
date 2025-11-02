from datetime import datetime

from maxo.enums import UpdateType
from maxo.routing.updates.base import MaxUpdate
from maxo.types.user import User


class BotRemoved(MaxUpdate):
    type = UpdateType.BOT_REMOVED

    timestamp: datetime
    chat_id: int | None = None
    user: User

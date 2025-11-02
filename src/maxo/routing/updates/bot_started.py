from datetime import datetime

from maxo.enums import UpdateType
from maxo.routing.updates.base import MaxUpdate
from maxo.types.user import User


class BotStarted(MaxUpdate):
    type = UpdateType.BOT_STARTED

    timestamp: datetime
    chat_id: int
    user: User
    payload: str | None = None
    user_locale: str | None = None

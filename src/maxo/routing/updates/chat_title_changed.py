from datetime import datetime

from maxo.enums import UpdateType
from maxo.routing.updates.base import MaxUpdate
from maxo.types.user import User


class ChatTitileChanged(MaxUpdate):
    type = UpdateType.CHAT_TITLE_CHANGED

    timestamp: datetime
    chat_id: int | None = None
    user: User
    title: str | None = None

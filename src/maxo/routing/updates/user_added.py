from datetime import datetime

from maxo.enums import UpdateType
from maxo.routing.updates.base import MaxUpdate
from maxo.types.user import User


class UserAdded(MaxUpdate):
    type = UpdateType.USER_ADDED

    timestamp: datetime
    chat_id: int | None = None
    user: User
    inviter_id: int | None = None

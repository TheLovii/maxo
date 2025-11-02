from datetime import datetime

from maxo.enums import UpdateType
from maxo.routing.updates.base import MaxUpdate
from maxo.types.chat import Chat


class MessageChatCreated(MaxUpdate):
    type = UpdateType.MESSAGE_CHAT_CREATED

    timestamp: datetime
    chat: Chat
    message_id: str | None = None
    start_payload: str | None = None

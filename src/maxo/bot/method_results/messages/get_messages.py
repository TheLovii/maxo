from collections.abc import Sequence

from maxo.types.base import MaxoType
from maxo.types.message import Message


class GetMessagesResult(MaxoType):
    """
    Результат получения сообщений.

    Args:
        messages: Массив сообщений.

    """

    messages: Sequence[Message]

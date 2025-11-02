from maxo.types.base import MaxoType
from maxo.types.chat import Chat


class GetChatsResult(MaxoType):
    """
    Результат метода GetChats.

    Args:
        chats: Список запрашиваемых чатов
        marker: Указатель на следующую страницу запрашиваемых чатов

    """

    chats: list[Chat]
    marker: int | None = None

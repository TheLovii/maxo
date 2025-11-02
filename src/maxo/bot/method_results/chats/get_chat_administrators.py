from collections.abc import Sequence

from maxo.omit import Omittable
from maxo.types.base import MaxoType
from maxo.types.chat_member import ChatMember


class GetChatAdministratorsResult(MaxoType):
    """
    Результат получения списка администраторов чата.

    Args:
        members: Список участников чата с информацией о времени последней активности.
        marker: Указатель на следующую страницу данных.

    """

    members: Sequence[ChatMember]
    marker: Omittable[int | None] = None

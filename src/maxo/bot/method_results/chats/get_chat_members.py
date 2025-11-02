from collections.abc import Sequence

from maxo.omit import Omittable, Omitted
from maxo.types.base import MaxoType
from maxo.types.chat_member import ChatMember


class GetChatMembersResult(MaxoType):
    """
    Результат получения участников чата.

    Args:
        members: Список участников чата с информацией о времени последней активности.
        marker: Указатель на следующую страницу данных.

    """

    members: Sequence[ChatMember]
    marker: Omittable[int | None] = Omitted()

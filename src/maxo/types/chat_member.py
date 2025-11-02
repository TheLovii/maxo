from collections.abc import Sequence
from datetime import datetime

from maxo.enums.chat_admin_permission import ChatAdminPermission
from maxo.omit import Omittable, Omitted
from maxo.types.user_with_photo import UserWithPhoto


class ChatMember(UserWithPhoto):
    last_access_time: Omittable[datetime] = Omitted()
    is_owner: Omittable[bool] = Omitted()
    is_admin: Omittable[bool] = Omitted()
    join_time: Omittable[datetime] = Omitted()
    permissions: Omittable[Sequence[ChatAdminPermission] | None] = Omitted()

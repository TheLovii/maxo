from maxo.omit import Omittable, Omitted
from maxo.types.bot_command import BotCommand
from maxo.types.user_with_photo import UserWithPhoto


class BotInfo(UserWithPhoto):
    """
    Информация о текущем боте.

    Args:
        commands: Команды, поддерживаемые ботом. До 32 элементов.

    """

    commands: Omittable[list[BotCommand] | None] = Omitted()

from typing import Self

from maxo.enums.attachment_type import AttachmentType
from maxo.types.base import MaxoType
from maxo.types.keyboard import Keyboard
from maxo.types.keyboard_buttons import KeyboardButtons


class InlineKeyboardAttachment(MaxoType):
    """
    Вложение инлайн клавиатуры.

    Args:
        payload: Данные вложения инлайн клавиатуры.

    """

    type = AttachmentType.INLINE_KEYBOARD

    payload: Keyboard

    @classmethod
    def factory(cls, buttons: list[list[KeyboardButtons]]) -> Self:
        """
        Фабричный метод.

        Args:
            buttons: Двумерный массив кнопок.

        """
        return cls(
            payload=Keyboard(
                buttons=buttons,
            ),
        )

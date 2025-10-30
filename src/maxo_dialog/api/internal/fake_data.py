from typing import Any, Literal

from maxo.methods import AnswerCallback
from maxo.types import (
    Callback,
    Chat,
    Message,
    User,
)


class ReplyCallback(Callback):
    original_message: Message

    def answer(self, *args: Any, **kwargs: Any) -> AnswerCallback:
        raise ValueError(
            "This callback query is generated from ReplyButton click. "
            "Support of `.answer()` call is impossible.",
        )


class FakeUser(User):
    fake: Literal[True] = True


class FakeChat(Chat):
    fake: Literal[True] = True

from typing import Any, Generic, TypeVar

from maxo.routing.signals.base import BaseSignal

_ExceptionT = TypeVar("_ExceptionT", bound=Exception)


class ErrorEvent(BaseSignal, Generic[_ExceptionT]):
    exception: _ExceptionT
    update: Any

    @property
    def error(self) -> _ExceptionT:
        return self.exception

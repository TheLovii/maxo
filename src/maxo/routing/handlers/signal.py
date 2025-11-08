from inspect import signature
from typing import Any, Generic, Protocol, TypeVar

from maxo.routing.ctx import Ctx
from maxo.routing.filters.always import AlwaysTrueFilter
from maxo.routing.interfaces.filter import Filter
from maxo.routing.interfaces.handler import Handler
from maxo.routing.signals.base import BaseSignal

_SignalT = TypeVar("_SignalT", bound=BaseSignal)
_ReturnT_co = TypeVar("_ReturnT_co", covariant=True)


class SignalHandlerFn(Protocol[_SignalT, _ReturnT_co]):
    async def __call__(self, **kwargs: Any) -> _ReturnT_co: ...


class SignalHandler(
    Handler[_SignalT, _ReturnT_co],
    Generic[_SignalT, _ReturnT_co],
):
    __slots__ = (
        "_filter",
        "handler_fn",
    )

    def __init__(
        self,
        handler_fn: SignalHandlerFn[_SignalT, _ReturnT_co],
        filter: Filter[_SignalT] | None = None,
    ) -> None:
        if filter is None:
            filter = AlwaysTrueFilter()

        self._filter = filter
        self.handler_fn = handler_fn

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(handler_fn={self.handler_fn}, filter={self._filter})"
        )

    def _prepare_kwargs(self, ctx: Ctx) -> dict[str, Any]:
        spec = signature(self.handler_fn)
        varkw = any(
            param.kind == param.VAR_KEYWORD for param in spec.parameters.values()
        )

        if varkw:
            return ctx

        return {k: ctx[k] for k in spec.parameters if k in ctx}

    async def execute_filter(self, ctx: Ctx) -> bool:
        return await self._filter(ctx["update"], ctx)

    async def __call__(self, ctx: Ctx) -> _ReturnT_co:
        return await self.handler_fn(**self._prepare_kwargs(ctx))

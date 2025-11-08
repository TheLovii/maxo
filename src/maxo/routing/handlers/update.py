from inspect import signature
from typing import Any, Generic, Protocol, TypeVar, runtime_checkable

from maxo.routing.ctx import Ctx
from maxo.routing.filters.always import AlwaysTrueFilter
from maxo.routing.interfaces.filter import Filter
from maxo.routing.interfaces.handler import Handler
from maxo.routing.updates.base import BaseUpdate

_UpdateT = TypeVar("_UpdateT", bound=BaseUpdate)
_ReturnT_co = TypeVar("_ReturnT_co", covariant=True)


@runtime_checkable
class UpdateHandlerFn(Protocol[_UpdateT, _ReturnT_co]):
    async def __call__(
        self,
        update: _UpdateT,
        /,
        **kwargs: Any,
    ) -> _ReturnT_co: ...


class UpdateHandler(
    Handler[_UpdateT, _ReturnT_co],
    Generic[_UpdateT, _ReturnT_co],
):
    __slots__ = (
        "_filter",
        "_handler_fn",
    )

    def __init__(
        self,
        handler_fn: UpdateHandlerFn[_UpdateT, _ReturnT_co],
        filter: Filter[_UpdateT] | None = None,
    ) -> None:
        if filter is None:
            filter = AlwaysTrueFilter()

        self._filter = filter
        self._handler_fn = handler_fn

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(handler_fn={self._handler_fn}, filter={self._filter})"
        )

    def _prepare_kwargs(self, ctx: Ctx) -> dict[str, Any]:
        spec = signature(self._handler_fn)
        varkw = any(
            param.kind == param.VAR_KEYWORD for param in spec.parameters.values()
        )

        if varkw:
            return ctx

        return {k: ctx[k] for k in spec.parameters if k in ctx}

    async def execute_filter(self, ctx: Ctx) -> bool:
        return await self._filter(ctx["update"], ctx)

    async def __call__(self, ctx: Ctx) -> _ReturnT_co:
        return await self._handler_fn(ctx["update"], **self._prepare_kwargs(ctx))

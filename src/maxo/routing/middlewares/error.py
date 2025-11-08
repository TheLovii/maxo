from typing import Any

from maxo.routing.ctx import Ctx
from maxo.routing.interfaces.middleware import BaseMiddleware, NextMiddleware
from maxo.routing.interfaces.router import Router
from maxo.routing.sentinels import UNHANDLED
from maxo.routing.signals.exception import ExceptionEvent


class ErrorMiddleware(BaseMiddleware[Any]):
    __slots__ = ("_router",)

    def __init__(self, router: Router) -> None:
        self._router = router

    async def __call__(
        self,
        update: Any,
        ctx: Ctx,
        next: NextMiddleware[Any],
    ) -> Any:
        try:
            return await next(ctx)
        except Exception as error:
            exception_event = ExceptionEvent(
                error=error,
                update=update,
            )
            new_ctx = ctx.copy()
            new_ctx["update"] = exception_event
            result = await self._router.trigger(new_ctx)
            if result is UNHANDLED:
                raise
            return result

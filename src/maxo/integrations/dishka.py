__all__ = ("CONTAINER_NAME", "MaxoProvider", "inject", "setup_dishka")

from typing import Any, Callable, Concatenate, ParamSpec, TypeVar, overload

from dishka import AsyncContainer

from maxo.routing.handlers.signal import SignalHandlerFn
from maxo.routing.handlers.update import UpdateHandlerFn
from maxo.routing.interfaces.middleware import BaseMiddleware, NextMiddleware
from maxo.routing.signals.base import BaseSignal
from maxo.routing.signals.update import Update

try:
    from dishka import Provider, Scope, from_context
    from dishka.integrations.base import wrap_injection
except ImportError as e:
    e.add_note(" * Please run `pip install maxo[dishka]`")
    raise

from maxo.bot.bot import Bot
from maxo.fsm.manager import FSMContext
from maxo.fsm.storages.base import BaseStorage, RawState
from maxo.routing.ctx import Ctx
from maxo.routing.dispatcher import Dispatcher
from maxo.routing.updates.base import BaseUpdate
from maxo.types.update_context import UpdateContext

CONTAINER_NAME = "dishka_container"

_ReturnT = TypeVar("_ReturnT")
_ParamsP = ParamSpec("_ParamsP")
_UpdateT = TypeVar("_UpdateT", bound=BaseUpdate)
_SignalT = TypeVar("_SignalT", bound=BaseSignal)

_SignalHandlerFn = Callable[Concatenate[Ctx, _ParamsP], _ReturnT]
_UpdateHandlerFn = Callable[Concatenate[_UpdateT, Ctx, _ParamsP], _ReturnT]


@overload
def inject(
    func: _SignalHandlerFn[_SignalT, _ParamsP, _ReturnT],
) -> SignalHandlerFn[_SignalT, _ReturnT]: ...


@overload
def inject(
    func: _UpdateHandlerFn[_UpdateT, _ParamsP, _ReturnT],
) -> UpdateHandlerFn[_UpdateT, _ReturnT]: ...


def inject(func: Any) -> Any:
    return wrap_injection(
        func=func,
        is_async=True,
        container_getter=lambda args, kwargs: kwargs["ctx"][CONTAINER_NAME],
    )


def setup_dishka(
    dispatcher: Dispatcher,
    container: AsyncContainer,
    auto_inject: bool,
    extra_context: dict[Any, Any] | None = None,
) -> None:
    dispatcher.update.middleware.outer(
        DishkaMiddleware(container, extra_context),
    )


class DishkaMiddleware(BaseMiddleware[Update[Any]]):
    __slots__ = ("_container", "_extra_context")

    def __init__(
        self, container: AsyncContainer, extra_context: dict[Any, Any] | None = None
    ) -> None:
        self._container = container
        self._extra_context = extra_context or {}

    async def __call__(
        self,
        update: Update[Any],
        ctx: Ctx,
        next: NextMiddleware[Update[Any]],
    ) -> Any:
        async with self._container(
            {
                Update[Any]: update,
                Update[type(update.update)]: update,  # type: ignore[misc]
                Ctx: ctx,
            }
            | self._extra_context,
        ) as container:
            ctx[CONTAINER_NAME] = container
            return await next(ctx)


class MaxoProvider(Provider):
    scope = Scope.REQUEST

    context = (
        from_context(provides=Bot)
        + from_context(provides=Dispatcher)
        + from_context(provides=UpdateContext)
        + from_context(provides=BaseStorage)
        + from_context(provides=FSMContext)
        + from_context(provides=RawState)
        + from_context(provides=Update[Any])
        + from_context(provides=Update[_UpdateT])
        + from_context(provides=Ctx)
    )

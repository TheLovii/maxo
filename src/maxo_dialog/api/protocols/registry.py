from abc import abstractmethod
from typing import Protocol, Union

from maxo.alta.state_system import State, StatesGroup

from .dialog import DialogProtocol


class DialogRegistryProtocol(Protocol):
    @abstractmethod
    def find_dialog(self, state: Union[State, str]) -> DialogProtocol:
        raise NotImplementedError

    @abstractmethod
    def states_groups(self) -> dict[str, type[StatesGroup]]:
        raise NotImplementedError

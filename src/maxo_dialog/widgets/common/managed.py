from typing import Generic, TypeVar

from maxo_dialog.api.internal import Widget
from maxo_dialog.api.protocols import DialogManager

W = TypeVar("W", bound=Widget)


class ManagedWidget(Generic[W]):
    def __init__(self, widget: W, manager: DialogManager):
        self.widget = widget
        self.manager = manager

    def __getattr__(self, item):
        return getattr(self.widget, item)

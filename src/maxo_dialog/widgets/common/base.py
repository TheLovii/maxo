from typing import Any, Optional

from maxo_dialog import DialogManager
from maxo_dialog.api.internal import Widget


class BaseWidget(Widget):
    def managed(self, manager: DialogManager) -> Any:
        return self

    def find(self, widget_id: str) -> Optional["Widget"]:
        return None

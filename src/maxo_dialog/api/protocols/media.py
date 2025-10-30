from abc import abstractmethod
from typing import Optional, Protocol

from maxo.types import ContentType

from maxo_dialog.api.entities import MediaId


class MediaIdStorageProtocol(Protocol):
    @abstractmethod
    async def get_media_id(
            self,
            path: Optional[str],
            url: Optional[str],
            type: ContentType,
    ) -> Optional[MediaId]:
        raise NotImplementedError

    @abstractmethod
    async def save_media_id(
            self,
            path: Optional[str],
            url: Optional[str],
            type: ContentType,
            media_id: MediaId,
    ) -> None:
        raise NotImplementedError

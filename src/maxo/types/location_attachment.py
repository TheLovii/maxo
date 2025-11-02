from maxo.enums.attachment_type import AttachmentType
from maxo.types.base import MaxoType


class LocationAttachment(MaxoType):
    """
    Вложение локации.

    Args:
        latitude: Широта
        longitude: Долгота

    """

    type = AttachmentType.LOCATION

    latitude: float
    longitude: float

from maxo.types.audio_attachment import AudioAttachment
from maxo.types.contact_attachment import ContactAttachment
from maxo.types.file_attachment import FileAttachment
from maxo.types.image_attachment import ImageAttachment
from maxo.types.keyboard import Keyboard
from maxo.types.location_attachment import LocationAttachment
from maxo.types.share_attachment import ShareAttachment
from maxo.types.sticker_attachment import StickerAttachment
from maxo.types.video_attachment import VideoAttachment

Attachments = (
    ImageAttachment
    | VideoAttachment
    | AudioAttachment
    | FileAttachment
    | StickerAttachment
    | ContactAttachment
    | Keyboard
    | ShareAttachment
    | LocationAttachment
)

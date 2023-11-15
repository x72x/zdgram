from .send_message import SendMessage
from .send_request import SendRequest
from .forward_message import ForwardMessage
from .get_me import GetMe
from .copy_message import CopyMessage
from .send_sticker import SendSticker
from .send_photo import SendPhoto
from .send_media_group import SendMediaGroup

class Methods(
    SendMessage,
    SendRequest,
    ForwardMessage,
    GetMe,
    CopyMessage,
    SendSticker,
    SendPhoto,
    SendMediaGroup
):
    pass
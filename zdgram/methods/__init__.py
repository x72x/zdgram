from .send_message import SendMessage
from .send_request import SendRequest
from .forward_message import ForwardMessage
from .get_me import GetMe
from .copy_message import CopyMessage
from .send_sticker import SendSticker
from .send_photo import SendPhoto
from .send_media_group import SendMediaGroup
from .send_audio import SendAudio
from .send_document import SendDocument
from .send_video import SendVideo
from .send_animation import SendAnimation
from .send_voice import SendVoice
from .send_location import SendLocation
from .send_venue import SendVenue
from .send_video_note import SendVideoNote
from .answer_callback_query import AnswerCallbackQuery
from .answer_inline_query import AnswerInlineQuery
from .logout import LogOut
from .close import Close
from .listen import Listener
from .get_chat import GetChat

class Methods(
    SendMessage,
    SendRequest,
    ForwardMessage,
    GetMe,
    CopyMessage,
    SendSticker,
    SendPhoto,
    SendMediaGroup,
    SendAudio,
    SendDocument,
    SendVideo,
    SendAnimation,
    SendVoice,
    SendLocation,
    SendVenue,
    SendVideoNote,
    AnswerCallbackQuery,
    AnswerInlineQuery,
    LogOut,
    Close,
    Listener,
    GetChat
):
    pass
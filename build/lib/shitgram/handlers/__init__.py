from .on_message import OnMessage
from .on_update import OnUpdate
from .on_edited_message import OnEditedMessage
from .on_callback_query import OnCallbackQuery
from .on_channel_post import OnChannelPost
from .on_edited_channel_post import OnEditedChannelPost
from .on_inline_query import OnInlineQuery
from .on_chosen_inline_result import OnChosenInlineResult

class Handlers(
    OnMessage,
    OnUpdate,
    OnEditedMessage,
    OnCallbackQuery,
    OnChannelPost,
    OnEditedChannelPost,
    OnInlineQuery,
    OnChosenInlineResult
):
    pass
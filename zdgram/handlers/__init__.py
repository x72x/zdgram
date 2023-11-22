from .on_message import OnMessage
from .on_update import OnUpdate
from .on_edited_message import OnEditedMessage
from .on_callback_query import OnCallbackQuery
from .on_channel_post import OnChannelPost
from .on_edited_channel_post import OnEditedChannelPost
from .on_inline_query import OnInlineQuery
from .on_chosen_inline_result import OnChosenInlineResult
from .on_my_chat_member import OnMyChatMember
from .on_chat_member import OnChatMember
from .on_chat_join_request import OnChatJoinRequest
from .on_poll import OnPoll
from .on_poll_answer import OnPollAnswer
from .on_shipping_query import OnShippingQuery
from .on_pre_checkout_query import OnPreCheckoutQuery

class Handlers(
    OnMessage,
    OnUpdate,
    OnEditedMessage,
    OnCallbackQuery,
    OnChannelPost,
    OnEditedChannelPost,
    OnInlineQuery,
    OnChosenInlineResult,
    OnMyChatMember,
    OnChatMember,
    OnChatJoinRequest,
    OnPoll,
    OnPollAnswer,
    OnShippingQuery,
    OnPreCheckoutQuery,
):
    pass
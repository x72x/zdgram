from .on_message import OnMessage
from .on_update import OnUpdate
from .on_edited_message import OnEditedMessage
from .on_callback_query import OnCallbackQuery

class Handlers(
    OnMessage,
    OnUpdate,
    OnEditedMessage,
    OnCallbackQuery
):
    pass
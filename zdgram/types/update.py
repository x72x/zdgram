
from .parser import Parser
import zdgram
import logging

class DictionaryToClass(Parser):
    def __init__(self, dic: dict):
        super().__init__()
        __ = False
        while not __:
            try:
                for i in dic:
                    if isinstance(dic[i], dict):
                        if i in {"from", "user"}:
                            dic[i]=zdgram.bot.user_manager._parse(dic[i])
                        elif i == "chat":
                            dic[i]=zdgram.bot.chat_manager._parse(dic[i])
                        setattr(self, "from_user" if i == "from" else "message" if i in ["edited_message", "channel_post", "edited_channel_post"] else i, DictionaryToClass(dic[i]))
                    elif isinstance(dic[i], list):
                        setattr(self, i, [DictionaryToClass(x) if isinstance(x, dict) else x for x in dic[i]])
                    else:
                        setattr(self, i, dic[i])
                __ = True
            except Exception as e:
                logging.getLogger(__name__).debug("Error %s", str(e))

    def __getattr__(self, __name: str) -> None:
        return None

class Update:
    message: "zdgram.types.Message"
    callback_query: "zdgram.types.CallbackQuery"
    inline_query: "zdgram.types.InlineQuery"
    chosen_inline_result: "zdgram.types.ChosenInlineResult"
    my_chat_member: "zdgram.types.ChatMemberUpdated"
    chat_member: "zdgram.types.ChatMemberUpdated"
    chat_join_request: "zdgram.types.ChatJoinRequest"
    poll: "zdgram.types.Poll"
    poll_answer: "zdgram.types.PollAnswer"
    shipping_query: "zdgram.types.ShippingQuery"
    pre_checkout_query: "zdgram.types.PreCheckoutQuery"
    update_id: int

    def _parse(self, dt: dict) -> "Update":
        for i in dt:
            if (
                isinstance(dt[i], dict) and i in ["message", "edited_message", "channel_post", "edited_channel_post"]
            ):
                dt[i]=zdgram.bot.message_manager._parse(dt[i])
            elif (
                isinstance(dt[i], dict) and i == "callback_query"
            ):
                dt['callback_query']['message']=zdgram.bot.message_manager._parse(dt['callback_query']['message'])

        return DictionaryToClass(dt)


from .parser import Parser
import shitgram


class DictionaryToClass(Parser):
    def __init__(self, dic: dict):
        super().__init__()
        self.__dict = dic
        __ = False
        while not __:
            try:
                for i in dic:
                    if isinstance(dic[i], dict):
                        if i == "from":
                            dic[i]=shitgram.types.User()._parse(dic[i])
                        setattr(self, "from_user" if i == "from" else "message" if i in ["edited_message", "channel_post", "edited_channel_post"] else i, DictionaryToClass(dic[i]))
                    elif isinstance(dic[i], list):
                        setattr(self, i, [DictionaryToClass(x) if isinstance(x, dict) else x for x in dic[i]])
                    else:
                        setattr(self, i, dic[i])
                __ = True
            except Exception as e:
                print(e)

    def __getattr__(self, __name: str) -> None:
        return None

class Update:
    message: "shitgram.types.Message"
    callback_query: "shitgram.types.CallbackQuery"
    inline_query: "shitgram.types.InlineQuery"
    chosen_inline_result: "shitgram.types.ChosenInlineResult"
    def _parse(self, dt: dict) -> "Update":
        for i in dt:
            if (
                isinstance(dt[i], dict) and i in ["message", "edited_message", "channel_post", "edited_channel_post"]
            ):
                dt[i]=shitgram.types.Message()._parse(dt[i])
            elif (
                isinstance(dt[i], dict) and i == "callback_query"
            ):
                dt['callback_query']['message']=shitgram.types.Message()._parse(dt['callback_query']['message'])

        return DictionaryToClass(dt)

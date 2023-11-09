
from .parser import Parser
import shitgram


class dtc(Parser):
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
                        setattr(self, "from_user" if i == "from" else "message" if i == "edited_message" else i, dtc(dic[i]))
                    elif isinstance(dic[i], list):
                        setattr(self, i, [dtc(x) if isinstance(x, dict) else x for x in dic[i]])
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

    def _parse(self, dt: dict) -> "Update":
        for i in dt:
            if (
                isinstance(dt[i], dict) and i == "message"
            ):
                dt['message']=shitgram.types.Message()._parse(dt['message'])
            elif (
                isinstance(dt[i], dict) and i == "callback_query"
            ):
                dt['callback_query']['message']=shitgram.types.Message()._parse(dt['callback_query']['message'])

        return dtc(dt)

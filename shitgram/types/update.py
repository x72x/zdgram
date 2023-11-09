from json import dumps
from .message import Message
from .user import User
from .callbackquery import CallbackQuery

class Parser:
    def __init__(self):
        pass

    @staticmethod
    def __default__(obj: "Parser"):
        return {
            **{
                attr: (
                    getattr(obj, attr)
                )
                for attr in obj.__dict__
                if getattr(obj, attr) is not None and not attr.startswith("_")
            }
        } if not isinstance(obj, set) else [i for i in obj]

    def __str__(self) -> str:
        return dumps(self, indent=4, default=Parser.__default__, ensure_ascii=False)

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
                            dic[i]=User()._parse(dic[i])
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
    message: Message
    callback_query: CallbackQuery

    def _parse(self, dt: dict) -> "Update":
        for i in dt:
            if (
                isinstance(dt[i], dict) and i == "message"
            ):
                dt['message']=Message()._parse(dt['message'])
            elif (
                isinstance(dt[i], dict) and i == "callback_query"
            ):
                dt['callback_query']['message']=Message()._parse(dt['callback_query']['message'])

        return dtc(dt)

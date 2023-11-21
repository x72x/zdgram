import shitgram

from typing import Callable

class OnMyChatMember:
    def onMyChatMember(self: "shitgram.Bot", func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_my_chat_member_handler(func_, func)
            return func_
        return decorator

    def on_my_chat_member(self: "shitgram.Bot", func: Callable = None):
        return self.onMyChatMember(func)
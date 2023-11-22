import zdgram

from typing import Callable

class OnChatMember:
    def onChatMember(self: "zdgram.Bot", func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_chat_member_handler(func_, func)
            return func_
        return decorator

    def on_chat_member(self: "zdgram.Bot", func: Callable = None):
        return self.onChatMember(func)
import shitgram

from typing import Callable

class OnChatJoinRequest:
    def onChatJoinRequest(self: "shitgram.Bot", func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_chat_join_request_handler(func_, func)
            return func_
        return decorator

    def on_chat_join_request(self: "shitgram.Bot", func: Callable = None):
        return self.onChatJoinRequest(func)
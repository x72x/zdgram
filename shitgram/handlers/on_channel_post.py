import shitgram

from typing import Callable

class OnChannelPost:
    def onChannelPost(self: "shitgram.Bot", func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_channel_post_handler(func_, func)

        return decorator
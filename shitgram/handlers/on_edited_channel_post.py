import shitgram

from typing import Callable

class OnEditedChannelPost:
    def onEditedChannelPost(self: "shitgram.Bot", func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_edited_channel_post_handler(func_, func)
            return func_
        return decorator
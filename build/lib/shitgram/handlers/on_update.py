import shitgram

from typing import Callable

class OnUpdate:
    @property
    def onUpdate(self: "shitgram.Bot"):
        def decorator(func_: Callable) -> Callable:
            self.add_any_update_handler(func_)
            return func_
        return decorator
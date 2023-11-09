import shitgram

from typing import Callable

class OnUpdate:
    @property
    def onUpdate(self: "shitgram.Bot"):
        def decorator(func: Callable) -> Callable:
            self.add_any_update_handler(func)

        return decorator
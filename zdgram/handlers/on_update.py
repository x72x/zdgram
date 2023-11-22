import zdgram

from typing import Callable

class OnUpdate:
    @property
    def onUpdate(self: "zdgram.Bot"):
        def decorator(func_: Callable) -> Callable:
            self.add_any_update_handler(func_)
            return func_
        return decorator

    on_update = onUpdate
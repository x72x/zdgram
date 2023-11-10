from typing import Union

class InputFile:
    def __init__(
            self,
            path: Union[str, bytes]
        ) -> None:
            self.path = path

    @property
    def get(self):
        if isinstance(self.path, str):
            with open(self.path, 'rb') as f:
                return f
        elif isinstance(self.path, bytes):
            return self.path
from typing import Union

class InputFile:
    def __init__(
            self,
            path: Union[str, bytes]
        ) -> bytes:
            if isinstance(path, bytes):
                return path
            else:
                with open(path, 'rb') as f:
                        return f.read()
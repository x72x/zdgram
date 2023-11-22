import string
import random
import os

from io import IOBase
from pathlib import Path
def generate_random_token() -> str:
    """
    Generates a random token consisting of letters and digits, 16 characters long.

    :return: a random token
    :rtype: :obj:`str`
    """
    return ''.join(random.sample(string.ascii_letters, 16))

class InputFile:
    def __init__(self, file) -> None:
        self._file, self.file_name = self._resolve_file(file)

    def _resolve_file(self, file):
        if isinstance(file, str):
            _file = open(file, 'rb')
            return _file, os.path.basename(_file.name)
        elif isinstance(file, IOBase):
            return file, generate_random_token()
        elif isinstance(file, Path):
            _file = open(file, 'rb')
            return _file, os.path.basename(_file.name)
        else:
            raise TypeError("File must be a string or a file-like object(pathlib.Path, io.IOBase).")

    @property
    def file(self):
        """
        File object.
        """
        return self._file
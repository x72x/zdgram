import shitgram
from .parser import Parser

class MessageEntity(
    Parser
):
    def __init__(
            self,
            type: str = None,
            offset: int = None,
            length: int = None,
            url: str = None,
            user: "shitgram.types.User" = None,
            language: str = None,
            custom_emoji_id: str = None
    ):
        super().__init__()
        self.custom_emoji_id = custom_emoji_id
        self.language = language
        self.user = user
        self.url = url
        self.length = length
        self.offset = offset
        self.type = type
import shitgram

class MessageEntity:
    type: str
    offset: int
    length: int
    url: str
    user: "shitgram.types.User"
    language: str
    custom_emoji_id: str
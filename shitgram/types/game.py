import shitgram
from typing import List

class Game:
    title: str
    description: str
    photo: List["shitgram.types.PhotoSize"]
    text: str
    text_entities: List["shitgram.types.MessageEntity"]
    animation: "shitgram.types.Animation"
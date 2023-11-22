import zdgram
from typing import List

class Game:
    title: str
    description: str
    photo: List["zdgram.types.PhotoSize"]
    text: str
    text_entities: List["zdgram.types.MessageEntity"]
    animation: "zdgram.types.Animation"
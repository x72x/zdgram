import shitgram

class Document:
    file_id: str
    file_unique_id: str
    thumbnail: "shitgram.types.PhotoSize"
    file_name: str
    mime_type: str
    file_size: int
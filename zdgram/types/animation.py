import zdgram


class Animation:
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumbnail: "zdgram.types.PhotoSize"
    file_name: str
    mime_type: str
    file_size: int
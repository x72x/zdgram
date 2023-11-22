import zdgram
from .parser import Parser
from typing import List, Union
from json import dumps

class InputMediaPhoto(
    Parser
):
    def __init__(
            self,
            media,
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List["zdgram.types.MessageEntity"] = None,
            has_spoiler: bool = None
    ):
        super().__init__()
        self.has_spoiler = has_spoiler
        self.caption_entities = dumps([str(i) if isinstance(i, zdgram.types.MessageEntity) else i.__dict__.get("_DictionaryToClass__dict") for i in caption_entities], ensure_ascii=False) if caption_entities else None
        self.parse_mode = parse_mode
        self.caption = caption
        self.media = media
        self.type = "photo"

class InputMediaAudio(
    Parser
):
    def __init__(
            self,
            media,
            thumbnail: Union["zdgram.types.InputFile", str] = None,
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List["zdgram.types.MessageEntity"] = None,
            duration: int = None,
            performer: str = None,
            title: str = None
    ):
        super().__init__()
        self.title = title
        self.performer = performer
        self.duration = duration
        self.thumbnail = thumbnail
        self.caption_entities = dumps([str(i) if isinstance(i, zdgram.types.MessageEntity) else i.__dict__.get("_DictionaryToClass__dict") for i in caption_entities], ensure_ascii=False) if caption_entities else None
        self.parse_mode = parse_mode
        self.caption = caption
        self.media = media
        self.type = "audio"


class InputMediaDocument(
    Parser
):
    def __init__(
            self,
            media,
            thumbnail: Union["zdgram.types.InputFile", str] = None,
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List["zdgram.types.MessageEntity"] = None,
            disable_content_type_detection: bool = None
    ):
        super().__init__()
        self.disable_content_type_detection = disable_content_type_detection
        self.thumbnail = thumbnail
        self.caption_entities = dumps([str(i) if isinstance(i, zdgram.types.MessageEntity) else i.__dict__.get("_DictionaryToClass__dict") for i in caption_entities], ensure_ascii=False) if caption_entities else None
        self.parse_mode = parse_mode
        self.caption = caption
        self.media = media
        self.type = "document"

class InputMediaAnimation(
    Parser
):
    def __init__(
            self,
            media,
            thumbnail: Union["zdgram.types.InputFile", str] = None,
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List["zdgram.types.MessageEntity"] = None,
            width: int = None,
            height: int = None,
            duration: int = None,
            has_spoiler: bool = None
    ):
        super().__init__()
        self.has_spoiler = has_spoiler
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.caption_entities = dumps([str(i) if isinstance(i, zdgram.types.MessageEntity) else i.__dict__.get("_DictionaryToClass__dict") for i in caption_entities], ensure_ascii=False) if caption_entities else None
        self.parse_mode = parse_mode
        self.caption = caption
        self.media = media
        self.type = "animation"

class InputMediaVideo(
    Parser
):
    def __init__(
            self,
            media,
            thumbnail: Union["zdgram.types.InputFile", str] = None,
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List["zdgram.types.MessageEntity"] = None,
            width: int = None,
            height: int = None,
            duration: int = None,
            has_spoiler: bool = None,
            supports_streaming: bool = None
    ):
        super().__init__()
        self.supports_streaming = supports_streaming
        self.has_spoiler = has_spoiler
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.caption_entities = dumps([str(i) if isinstance(i, zdgram.types.MessageEntity) else i.__dict__.get("_DictionaryToClass__dict") for i in caption_entities], ensure_ascii=False) if caption_entities else None
        self.parse_mode = parse_mode
        self.caption = caption
        self.media = media
        self.type = "video"
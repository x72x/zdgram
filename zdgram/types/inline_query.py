import zdgram
import random
from .parser import Parser
from typing import List, Union

class InlineQuery:
    id: str
    from_user: "zdgram.types.User"
    query: str
    offset: str
    chat_type: str
    location: "zdgram.types.Location"

class ChosenInlineResult:
    result_id: str
    from_user: "zdgram.types.User"
    location: "zdgram.types.Location"
    inline_message_id: str
    query: str

class InlineQueryResultsButton(
    Parser
):
    def __init__(
            self,
            text: str,
            web_app: "zdgram.types.WebAppInfo" = None,
            start_parameter: str = None
    ):
        super().__init__()
        self.start_parameter = start_parameter
        self.web_app = web_app
        self.text = text

class InputTextMessageContent(
    Parser
):
    def __init__(
            self,
            message_text: str,
            parse_mode: str = None,
            entities: List["zdgram.types.MessageEntity"] = None,
            disable_web_page_preview: bool = None
    ):
        super().__init__()
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.entities = entities
        self.disable_web_page_preview = disable_web_page_preview

class InputLocationMessageContent(
    Parser
):
    def __init__(
            self,
            latitude: float,
            longitude: float,
            horizontal_accuracy: float = None,
            live_period: int = None,
            heading: int = None,
            proximity_alert_radius: int = None
    ):
        super().__init__()
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius

class InputVenueMessageContent(
    Parser
):
    def __init__(
            self,
            latitude: float,
            longitude: float,
            title: str,
            address: str,
            foursquare_id: str = None,
            foursquare_type: str = None,
            google_place_id: str = None,
            google_place_type: str = None
    ):
        super().__init__()
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type

class InputContactMessageContent(
    Parser
):
    def __init__(
            self,
            phone_number: str,
            first_name: str,
            last_name: str = None,
            vcard: str = None
    ):
        super().__init__()
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard

class LabeledPrice(
    Parser
):
    def __init__(self, label: str, amount: int):
        super().__init__()
        self.amount = amount
        self.label = label


class InputInvoiceMessageContent(
    Parser
):
    def __init__(
            self,
            title: str,
            description: str,
            payload: str,
            provider_token: str,
            currency: str,
            prices: List["LabeledPrice"],
            max_tip_amount: int = None,
            suggested_tip_amounts: List["int"] = None,
            provider_data: str = None,
            photo_url: str = None,
            photo_size: int = None,
            photo_width: int = None,
            photo_height: int = None,
            need_name: bool = None,
            need_phone_number: bool = None,
            need_email: bool = None,
            need_shipping_address: bool = None,
            send_phone_number_to_provider: bool = None,
            send_email_to_provider: bool = None,
            is_flexible: bool = None
    ):
        super().__init__()
        self.title = title
        self.description = description
        self.payload = payload
        self.provider_token = provider_token
        self.currency = currency
        self.prices = [self.__default__(i) for i in prices] if prices is not None else prices
        self.max_tip_amount = max_tip_amount
        self.suggested_tip_amounts = suggested_tip_amounts
        self.provider_data = provider_data
        self.photo_url = photo_url
        self.photo_size = photo_size
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.need_name = need_name
        self.need_phone_number = need_phone_number
        self.need_email = need_email
        self.need_shipping_address = need_shipping_address
        self.send_phone_number_to_provider = send_phone_number_to_provider
        self.send_email_to_provider = send_email_to_provider
        self.is_flexible = is_flexible

class InlineQueryResultArticle(
    Parser
):
    def __init__(
            self,
            title: str,
            input_message_content: Union[
                "InputTextMessageContent",
                "InputLocationMessageContent",
                "InputVenueMessageContent",
                "InputContactMessageContent",
                "InputInvoiceMessageContent"
            ],
            reply_markup: "zdgram.types.InlineKeyboardMarkup" = None,
            url: str = None,
            hide_url: bool = None,
            description: str = None,
            thumbnail_url: str = None,
            thumbnail_width: int = None,
            thumbnail_height: int = None
    ):
        super().__init__()
        self.id = str(random.randint(1000, 1000*10*10))
        self.type = "article"
        self.title = title
        self.input_message_content = self.__default__(input_message_content)
        self.reply_markup = reply_markup.get_json if reply_markup is not None else reply_markup
        self.url = url
        self.hide_url = hide_url
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

class InlineQueryResultPhoto(
    Parser
):
    def __init__(
            self,
            photo_url: str,
            thumbnail_url: str,
            photo_width: int = None,
            photo_height: int = None,
            title: str = None,
            description: str = None,
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List["zdgram.types.MessageEntity"] = None,
            reply_markup: "zdgram.types.InlineKeyboardMarkup" = None,
            input_message_content: Union[
                "InputTextMessageContent",
                "InputLocationMessageContent",
                "InputVenueMessageContent",
                "InputContactMessageContent",
                "InputInvoiceMessageContent"
            ] = None,
    ):
        super().__init__()
        self.id = str(random.randint(1000, 1000*10*10))
        self.type = "photo"
        self.photo_url = photo_url
        self.thumbnail_url = thumbnail_url
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = [self.__default__(i) for i in caption_entities] if caption_entities is not None else caption_entities
        self.reply_markup = reply_markup.get_json if reply_markup is not None else reply_markup
        self.input_message_content = self.__default__(input_message_content) if input_message_content is not None else input_message_content


class InlineQueryResultGif(
    Parser
):
    def __init__(
            self,
            gif_url: str,
            thumbnail_url: str,
            thumbnail_mime_type: str = None,
            gif_width: int = None,
            gif_height: int = None,
            gif_duration: int = None,
            title: str = None,
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List["zdgram.types.MessageEntity"] = None,
            reply_markup: "zdgram.types.InlineKeyboardMarkup" = None,
            input_message_content: Union[
                "InputTextMessageContent",
                "InputLocationMessageContent",
                "InputVenueMessageContent",
                "InputContactMessageContent",
                "InputInvoiceMessageContent"
            ] = None,
    ):
        super().__init__()
        self.id = str(random.randint(1000, 1000*10*10))
        self.type = "gif"
        self.gif_url = gif_url
        self.thumbnail_url = thumbnail_url
        self.thumbnail_mime_type = thumbnail_mime_type
        self.gif_width = gif_width
        self.gif_height = gif_height
        self.gif_duration = gif_duration
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = [self.__default__(i) for i in caption_entities] if caption_entities is not None else caption_entities
        self.reply_markup = reply_markup.get_json if reply_markup is not None else reply_markup
        self.input_message_content = self.__default__(input_message_content) if input_message_content is not None else input_message_content


class InlineQueryResultMpeg4Gif(
    Parser
):
    def __init__(
            self,
            mpeg4_url: str,
            thumbnail_url: str,
            thumbnail_mime_type: str = None,
            mpeg4_width: int = None,
            mpeg4_height: int = None,
            mpeg4_duration: int = None,
            title: str = None,
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List["zdgram.types.MessageEntity"] = None,
            reply_markup: "zdgram.types.InlineKeyboardMarkup" = None,
            input_message_content: Union[
                "InputTextMessageContent",
                "InputLocationMessageContent",
                "InputVenueMessageContent",
                "InputContactMessageContent",
                "InputInvoiceMessageContent"
            ] = None,
    ):
        super().__init__()
        self.id = str(random.randint(1000, 1000*10*10))
        self.type = "mpeg4_gif"
        self.mpeg4_url = mpeg4_url
        self.thumbnail_url = thumbnail_url
        self.thumbnail_mime_type = thumbnail_mime_type
        self.mpeg4_width = mpeg4_width
        self.mpeg4_height = mpeg4_height
        self.mpeg4_duration = mpeg4_duration
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = [self.__default__(i) for i in caption_entities] if caption_entities is not None else caption_entities
        self.reply_markup = reply_markup.get_json if reply_markup is not None else reply_markup
        self.input_message_content = self.__default__(input_message_content) if input_message_content is not None else input_message_content

class InlineQueryResultVideo(
    Parser
):
    def __init__(
            self,
            title: str,
            video_url: str,
            mime_type: str,
            thumbnail_url: str,
            video_width: int = None,
            video_height: int = None,
            video_duration: int = None,
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List["zdgram.types.MessageEntity"] = None,
            reply_markup: "zdgram.types.InlineKeyboardMarkup" = None,
            input_message_content: Union[
                "InputTextMessageContent",
                "InputLocationMessageContent",
                "InputVenueMessageContent",
                "InputContactMessageContent",
                "InputInvoiceMessageContent"
            ] = None,
    ):
        super().__init__()
        self.id = str(random.randint(1000, 1000*10*10))
        self.type = "video"
        self.video_url = video_url
        self.mime_type = mime_type
        self.thumbnail_url = thumbnail_url
        self.video_width = video_width
        self.video_height = video_height
        self.video_duration = video_duration
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = [self.__default__(i) for i in caption_entities] if caption_entities is not None else caption_entities
        self.reply_markup = reply_markup.get_json if reply_markup is not None else reply_markup
        self.input_message_content = self.__default__(input_message_content) if input_message_content is not None else input_message_content


class InlineQueryResultAudio(
    Parser
):
    def __init__(
            self,
            title: str,
            audio_url: str,
            audio_duration: int = None,
            performer: str = None,
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List["zdgram.types.MessageEntity"] = None,
            reply_markup: "zdgram.types.InlineKeyboardMarkup" = None,
            input_message_content: Union[
                "InputTextMessageContent",
                "InputLocationMessageContent",
                "InputVenueMessageContent",
                "InputContactMessageContent",
                "InputInvoiceMessageContent"
            ] = None,
    ):
        super().__init__()
        self.id = str(random.randint(1000, 1000*10*10))
        self.type = "audio"
        self.audio_url = audio_url
        self.audio_duration = audio_duration
        self.performer = performer
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = [self.__default__(i) for i in caption_entities] if caption_entities is not None else caption_entities
        self.reply_markup = reply_markup.get_json if reply_markup is not None else reply_markup
        self.input_message_content = self.__default__(input_message_content) if input_message_content is not None else input_message_content

class InlineQueryResultVoice(
    Parser
):
    def __init__(
            self,
            title: str,
            voice_url: str,
            voice_duration: int = None,
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List["zdgram.types.MessageEntity"] = None,
            reply_markup: "zdgram.types.InlineKeyboardMarkup" = None,
            input_message_content: Union[
                "InputTextMessageContent",
                "InputLocationMessageContent",
                "InputVenueMessageContent",
                "InputContactMessageContent",
                "InputInvoiceMessageContent"
            ] = None,
    ):
        super().__init__()
        self.id = str(random.randint(1000, 1000*10*10))
        self.type = "voice"
        self.voice_url = voice_url
        self.voice_duration = voice_duration
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = [self.__default__(i) for i in caption_entities] if caption_entities is not None else caption_entities
        self.reply_markup = reply_markup.get_json if reply_markup is not None else reply_markup
        self.input_message_content = self.__default__(input_message_content) if input_message_content is not None else input_message_content
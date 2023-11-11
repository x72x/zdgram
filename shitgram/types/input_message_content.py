import shitgram
from .parser import Parser
from typing import List

class InputTextMessageContent(
    Parser
):
    def __init__(
            self,
            message_text: str,
            parse_mode: str = None,
            entities: List["shitgram.types.MessageEntity"] = None,
            disable_web_page_preview: bool = None
    ):
        super().__init__()
        self.disable_web_page_preview = disable_web_page_preview
        self.entities = entities
        self.parse_mode = parse_mode
        self.message_text = message_text


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
        self.proximity_alert_radius = proximity_alert_radius
        self.heading = heading
        self.live_period = live_period
        self.horizontal_accuracy = horizontal_accuracy
        self.longitude = longitude
        self.latitude = latitude

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
        self.google_place_type = google_place_type
        self.google_place_id = google_place_id
        self.foursquare_type = foursquare_type
        self.foursquare_id = foursquare_id
        self.address = address
        self.title = title
        self.longitude = longitude
        self.latitude = latitude

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
        self.vcard = vcard
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number


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
        self.prices = prices
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
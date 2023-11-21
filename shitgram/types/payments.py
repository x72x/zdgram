import shitgram

class ShippingAddress:
    country_code: str
    state: str
    city: str
    street_line: str
    street_line2: str
    post_code: str

class OrderInfo:
    name: str
    phone_number: str
    email: str
    shipping_address: "ShippingAddress"

class SuccessfulPayment:
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: str
    order_info: "OrderInfo"
    telegram_payment_charge_id: str
    provider_payment_charge_id: str

class ShippingQuery:
    id: str
    from_user: "shitgram.types.User"
    invoice_payload: str
    shipping_address: "ShippingAddress"

class PreCheckoutQuery:
    id: str
    from_user: "shitgram.types.User"
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: str
    order_info: "OrderInfo"
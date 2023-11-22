from typing import List
from random import randint
from .parser import Parser

import zdgram

class ReplyKeyboardMarkup(
    Parser
):
    def __init__(self, keyboard: List[List["KeyboardButton"]], is_persistent: bool = None, resize_keyboard: bool = None, one_time_keyboard: bool = None, input_field_placeholder: bool = None, selective: bool = None):
        super().__init__()
        self.keyboard = keyboard
        if is_persistent is not None: self.is_persistent = is_persistent
        if resize_keyboard is not None: self.resize_keyboard = resize_keyboard
        if one_time_keyboard is not None: self.one_time_keyboard = one_time_keyboard
        if input_field_placeholder is not None: self.input_field_placeholder = input_field_placeholder
        if selective is not None: self.selective = selective

class ReplyKeyboardRemove(
    Parser
):
    def __init__(self, selective: bool = None):
        super().__init__()
        self.remove_keyboard = True
        if selective is not None: self.selective = selective

class KeyboardButton(
    Parser
):
    def __init__(self, text: str, request_user: "KeyboardButtonRequestUser" = None, request_chat: "KeyboardButtonRequestChat" = None, request_contact: bool = None, request_location: bool = None, request_poll: "KeyboardButtonPollType" = None, web_app: "zdgram.types.WebAppInfo" = None):
        super().__init__()
        self.text = text
        if request_user is not None: self.request_user = request_user
        if request_chat is not None: self.request_chat = request_chat
        if request_contact is not None: self.request_contact = request_contact
        if request_location is not None: self.request_location = request_location
        if request_poll is not None: self.request_poll = request_poll
        if web_app is not None: self.web_app = web_app

class KeyboardButtonRequestUser(
    Parser
):
    def __init__(self, request_id: int = None, user_is_bot: bool = None, user_is_premium: bool = None):
        super().__init__()
        self.request_id = request_id or randint(100, 100*100*10)
        self.user_is_bot = user_is_bot
        self.user_is_premium = user_is_premium

class KeyboardButtonRequestChat(
    Parser
):
    def __init__(self, request_id: int = None, chat_is_channel: bool = None, chat_is_forum: bool = None, chat_has_username: bool = None, chat_is_created: bool = None, user_administrator_rights: "zdgram.types.ChatAdministratorRights" = None, bot_administrator_rights: "zdgram.types.ChatAdministratorRights" = None, bot_is_member: bool = None):
        super().__init__()
        if bot_administrator_rights is not None: self.bot_administrator_rights = bot_administrator_rights
        if user_administrator_rights is not None: self.user_administrator_rights = user_administrator_rights
        self.chat_is_created = chat_is_created
        self.chat_is_channel = chat_is_channel
        self.chat_is_forum = chat_is_forum
        self.chat_has_username = chat_has_username
        self.bot_is_member = bot_is_member
        self.request_id = request_id or randint(100, 100*100*10)

class KeyboardButtonPollType(
    Parser
):
    def __init__(self, type: str):
        super().__init__()
        self.type = type
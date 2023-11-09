from . import types
from typing import Union
from json import dumps

def reply_markup_parse(
        reply_markup: Union["str", "dict", "types.InlineKeyboardMarkup", "types.ForceReply"]
):
    if isinstance(reply_markup, dict):
        return dumps(reply_markup, ensure_ascii=False)
    elif isinstance(reply_markup, str):
        return reply_markup
    elif isinstance(
        reply_markup, types.InlineKeyboardMarkup
    ) or isinstance(
        reply_markup, types.ForceReply
    ) or isinstance(
        reply_markup, types.ReplyKeyboardMarkup
    ) or isinstance(
        reply_markup, types.ReplyKeyboardRemove
    ):
        return str(reply_markup)
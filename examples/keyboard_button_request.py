import logging

from zdgram import Bot, enums, types
from typing import Callable

logging.basicConfig(level=logging.INFO)

bot = Bot("TOKEN")

def textAndPrivate(func: Callable) -> Callable:
    async def decorator(_: Bot, message: types.Message):
        if (message.text and message.text == '/start') and (message.chat.type == enums.ChatType.PRIVATE):
            return await func(_, message)

    return decorator

@bot.onMessage()
@textAndPrivate
async def on_private(bot: Bot, message: types.Message):
    return await bot.sendMessage(
        message.chat.id,
        "Choose a chat :",
        reply_to_message_id=message.id,
        reply_markup=types.ReplyKeyboardMarkup(
            [
                [
                    types.KeyboardButton(
                        "Channel",
                        request_chat=types.KeyboardButtonRequestChat(chat_is_channel=True)
                    ),
                    types.KeyboardButton(
                        "Group", request_chat=types.KeyboardButtonRequestChat(chat_has_username=False)
                    )
                ],
                [
                    types.KeyboardButton(
                        "Public Group", request_chat=types.KeyboardButtonRequestChat(chat_has_username=True)
                    ),
                    types.KeyboardButton(
                        "User", request_user=types.KeyboardButtonRequestUser(user_is_premium=False)
                    )
                ],
                [
                    types.KeyboardButton(
                        "Premium User",
                        request_user=types.KeyboardButtonRequestUser(user_is_premium=True)
                    ),
                    types.KeyboardButton(
                        "Your own Groups",
                        request_chat=types.KeyboardButtonRequestChat(chat_is_created=True)
                    )
                ],
                [
                    types.KeyboardButton(
                        "Your own Channels",
                        request_chat=types.KeyboardButtonRequestChat(chat_is_created=True, chat_is_channel=True)
                    )
                ]
            ],
            resize_keyboard=True,
            input_field_placeholder=":)"
        )
    )

@bot.onMessage(func=lambda m: m.chat_shared or m.user_shared)
async def on_chat_shared(bot: Bot, message: types.Message):
    return await bot.sendMessage(
        message.chat.id,
        f"Chat ID Is : `{message.chat_shared.chat_id if message.chat_shared else message.user_shared.user_id}`",
        parse_mode=enums.ParseMode.MARKDOWN,
        reply_to_message_id=message.id
    )

bot.run()
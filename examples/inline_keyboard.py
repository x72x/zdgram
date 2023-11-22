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
        "Choose a Button :",
        reply_to_message_id=message.id,
        reply_markup=types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton("Url", url=f"http://t.me/{message.chat.username}"),
                    types.InlineKeyboardButton("User Buttom", user_id=message.chat.id)
                ],
                [
                    types.InlineKeyboardButton("Inline Query Current Chat", switch_inline_query_current_chat="hi")
                ],
                [
                    types.InlineKeyboardButton("Inline Query Specific Chat", switch_inline_query_chosen_chat=types.SwitchInlineQueryChosenChat("hi", allow_user_chats=True, allow_bot_chats=False, allow_group_chats=False, allow_channel_chats=False))
                ],
                [
                    types.InlineKeyboardButton("Callback", callback_data="none")
                ]
            ]
        )
    )

@bot.onCallbackQuery()
async def on_callback(bot: Bot, callback_query: types.CallbackQuery):
    if callback_query.data == "none":
        return await bot.answerCallbackQuery(
            callback_query.id,
            "Hi",
            show_alert=True,
            cache_time=60
        )

bot.run()
from zdgram import Bot, enums, types
from typing import Callable


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
                    types.InlineKeyboardButton("Inline Query Current Chat", switch_inline_query_current_chat="hi")
                ],
                [
                    types.InlineKeyboardButton("Inline Query Specific Chat", switch_inline_query_chosen_chat=types.SwitchInlineQueryChosenChat("hi", allow_user_chats=True, allow_bot_chats=False, allow_group_chats=False, allow_channel_chats=False))
                ],
            ]
        )
    )

@bot.onInlineQuery()
async def on_inline(bot: Bot, inline_query: types.InlineQuery):
    return await bot.answerInlineQuery(
        inline_query.id,
        results=[
            types.InlineQueryResultArticle(
                "Hi",
                input_message_content=types.InputTextMessageContent("Test"),
                reply_markup=types.InlineKeyboardMarkup(
                    [
                        [
                            types.InlineKeyboardButton(inline_query.from_user.first_name, user_id=inline_query.from_user.id)
                        ],
                        [
                            types.InlineKeyboardButton(inline_query.from_user.first_name, url="http://t.me/"+inline_query.from_user.username)
                        ]
                    ]
                ),
                url=f"http://t.me/{inline_query.from_user.username}",
                description=":)"
            ),
            types.InlineQueryResultPhoto(
                photo_url="https://t.me/zaid_gram/2",
                thumbnail_url="https://t.me/zaid_gram/2"
            )
        ],
    )

bot.run()
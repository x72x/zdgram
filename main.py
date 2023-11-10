from shitgram import Bot, types

import asyncio

bot = Bot("6445275649:AAGi8e3yI3OgLHYEHI4XGYv_7VbTZ7UVUgM")


@bot.onMessage()
async def on_Sticker(bot: Bot, message: types.Message):
    print(message.chat_shared)
    await bot.sendMessage(
        chat_id=message.chat.id,
        text="Hi",
        reply_to_message_id=message.id,
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(
                        "Hi", web_app=types.WebAppInfo("https://stackoverflow.com/questions/57553738/how-to-aiohttp-request-post-files-list-python-requests-module")
                    )
                ],
                [
                    types.InlineKeyboardButton(
                        "Hi 2",
                        switch_inline_query_chosen_chat=types.SwitchInlineQueryChosenChat(
                            allow_group_chats=False,
                            allow_channel_chats=False,
                            allow_bot_chats=False,
                        )
                    )
                ]
            ]
        )
    )

if __name__ == "__main__":
    print(asyncio.run(bot.getMe()))
    bot.start_polling()
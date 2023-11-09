from shitgram import Bot
from shitgram.types import Update, Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

import logging

logging.basicConfig(level=logging.INFO)

bot = Bot("6445275649:AAGi8e3yI3OgLHYEHI4XGYv_7VbTZ7UVUgM")

@bot.onUpdate
async def on_anything(bot: Bot, update: Update):
    if (update.message) and not update.message.sticker:
        print("No")

@bot.onMessage(func=lambda m: m.sticker)
async def on_stickers(bot: Bot, message: Message):
    await bot.sendMessage(
        message.chat.id,
        message.sticker.file_id,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("hi", callback_data="none"),
                    InlineKeyboardButton("hi2", url="https://t.me/y88f8")
                ],
                [
                    InlineKeyboardButton("hi3", user_id=message.from_user.id),
                    InlineKeyboardButton("hi4", switch_inline_query="none4")
                ]
            ]
        ),
        reply_to_message_id=message.id
    )

@bot.onEditedMessage(func=lambda m: m.photo)
async def on_edited(bot: Bot, message: Message):
    print(message)

@bot.onCallbackQuery()
async def on_callback(bot: Bot, query: CallbackQuery):
    print(query)

if __name__ == "__main__":
    bot.start_polling()
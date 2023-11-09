from shitgram import Bot
from shitgram.types import Update, Message

import logging

logging.basicConfig(level=logging.INFO)

bot = Bot("6445275649:AAGi8e3yI3OgLHYEHI4XGYv_7VbTZ7UVUgM")

@bot.onUpdate
async def on_anything(bot: Bot, update: Update):
    if update.message and (
        not update.message.sticker
    ):
        print("No")

@bot.onMessage(func=lambda m: m.sticker)
async def on_stickers(bot: Bot, message: Message):
    print(message)

@bot.onEditedMessage(func=lambda m: m.photo)
async def on_edited(bot: Bot, message: Message):
    print(message)

if __name__ == "__main__":
    bot.start_polling()
from shitgram import Bot
from shitgram.types import Update
from shitgram.exceptions import ApiException

import logging

logging.basicConfig(level=logging.INFO)

bot = Bot("6445275649:AAGi8e3yI3OgLHYEHI4XGYv_7VbTZ7UVUgM")

@bot.on_update
async def on_updates(bot: Bot, update: Update):
    await bot.sendMessage(
        update.message.chat.id,
        text=update.message.text,
        entities=update.message.entities
    )

if __name__ == "__main__":
    bot.start_polling()
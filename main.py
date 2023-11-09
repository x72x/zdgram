from shitgram import Bot, types

bot = Bot("6445275649:AAGi8e3yI3OgLHYEHI4XGYv_7VbTZ7UVUgM")


@bot.onMessage()
async def on_Sticker(bot: Bot, message: types.Message):
    print(message.chat_shared)
    await bot.sendMessage(
        message.chat.id,
        "Hi",
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton(
                        text="Hi",
                        request_chat=types.KeyboardButtonRequestChat()
                    )
                ]
            ],
            resize_keyboard=True
        )
    )

if __name__ == "__main__":
    bot.start_polling()
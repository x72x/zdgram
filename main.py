from shitgram import Bot, types, enums

bot = Bot(
    "5860767186:AAF32kvjD6--ZWqszgsIS8AjIeH9mAnIM9E",
    disable_web_page_preview=True,
    parse_mode=enums.ParseMode.MARKDOWN
)

print(bot.run(bot.getMe()))

def only_text_and_private(m: types.Message):
    return bool(m.text and m.chat.type == enums.ChatType.PRIVATE)

@bot.onMessage(func=only_text_and_private)
async def on_message(bot: Bot, message: types.Message):
    await bot.sendMessage(
        message.chat.id,
        "Send Your name",
        reply_to_message_id=message.id
    )
    msg = await bot.Listen(func=only_text_and_private)
    return await bot.sendMessage(
        message.chat.id,
        "Your name is : "+msg.text,
        reply_to_message_id=msg.id
    )

bot.run()
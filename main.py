from shitgram import Bot, types, enums, run_multiple_bots
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot("6445275649:AAGi8e3yI3OgLHYEHI4XGYv_7VbTZ7UVUgM")
bot2 = Bot("5860767186:AAF32kvjD6--ZWqszgsIS8AjIeH9mAnIM9E")

# @bot.onMessage()
# async def on_Sticker(bot: Bot, message: types.Message):
#     if message.chat.type == enums.ChatType.PRIVATE:
#         # await bot.sendMessage(
#         #     chat_id=message.chat.id,
#         #     text="Hi",
#         #     reply_to_message_id=message.id,
#         #     reply_markup=types.InlineKeyboardMarkup(
#         #         inline_keyboard=[
#         #             [
#         #                 types.InlineKeyboardButton(
#         #                     "Hi", web_app=types.WebAppInfo("https://stackoverflow.com/questions/57553738/how-to-aiohttp-request-post-files-list-python-requests-module")
#         #                 )
#         #             ],
#         #             [
#         #                 types.InlineKeyboardButton(
#         #                     "Hi 2",
#         #                     switch_inline_query_chosen_chat=types.SwitchInlineQueryChosenChat(
#         #                         allow_group_chats=False,
#         #                         allow_channel_chats=False,
#         #                         allow_bot_chats=False,
#         #                     )
#         #                 )
#         #             ]
#         #         ]
#         #     )
#         # )
#         await bot.sendPhoto(
#             message.chat.id,
#             photo=types.InputFile("img.jpg"),
#             caption="blyaad",
#             caption_entities=[
#                 types.MessageEntity(
#                     type="text_link",
#                     offset=1,
#                     length=5,
#                     url="https://t.me/zaid"
#                 )
#             ],
#             has_spoiler=True
#         )

@bot2.onMessage()
@bot2.onEditedMessage()
async def bot2_test(_: Bot, m: types.Message):
    # await _.copyMessage(
    #     m.chat.id,
    #     m.chat.id,
    #     m.id,
    #     reply_to_message_id=m.id,
    #     reply_markup=types.InlineKeyboardMarkup(
    #         [
    #             [
    #                 types.InlineKeyboardButton(
    #                     "Hi",
    #                     switch_inline_query_chosen_chat=types.SwitchInlineQueryChosenChat()
    #                 )
    #             ]
    #         ]
    #     )
    # )
    print(m)

@bot.onChannelPost()
@bot.onMessage()
async def on_channel_post(bot, message: types.Message):
    if message.sticker:
        await bot.sendSticker(
            message.chat.id,
            message.sticker.file_id
        )
    else:
        await bot.sendSticker(
            message.chat.id,
            sticker=types.InputFile("sticker.webp")
        )

@bot.onEditedChannelPost()
async def on_edited_channel_post(_, message: types.Message):
    print(message)


if __name__ == "__main__":
    asyncio.run(run_multiple_bots([bot, bot2]))
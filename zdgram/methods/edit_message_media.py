import zdgram
from typing import Union

class EditMessageMedia:
    async def editMessageMedia(
            self: "zdgram.Bot",
            media: Union[
                "zdgram.types.InputMediaPhoto",
                "zdgram.types.InputMediaAnimation",
                "zdgram.types.InputMediaAudio",
                "zdgram.types.InputMediaVideo",
                "zdgram.types.InputMediaDocument"
            ],
            chat_id: Union[str, int] = None,
            message_id: int = None,
            inline_message_id: str = None,
            reply_markup: "zdgram.types.InlineKeyboardMarkup" = None,
            timeout: int = None,
    ) -> Union["zdgram.types.Message", "bool"]:
        """Use this method to edit animation, audio, document, photo, or video messages. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo or a video otherwise. When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.
        https://core.telegram.org/bots/api#editmessagemedia

        Args:

            media: (`InputMedia`): A JSON-serialized object for a new media content of the message.

            chat_id: (Union[`str`, `int`], optional): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername). Default to None.

            message_id: (`int`, optional): Required if inline_message_id is not specified. Identifier of the message to edit. Default to None.

            inline_message_id: (`str`, optional): Required if chat_id and message_id are not specified. Identifier of the inline message. Default to None.

            reply_markup: (`InlineKeyboardMarkup`, optional): A JSON-serialized object for a new inline keyboard. Default to None.

        Returns:

            On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Example:

            ```
            msg = await bot.sendPhoto(chat_id, "old_photo_url")
            await asyncio.sleep(2.5)
            await bot.editMessageMedia(
                chat_id=msg.chat.id,
                media=InputMediaPhoto(
                    media="new_photo_url"
                )
            )
            ```
        """
        data = {
            "media": media.__default__(media)
        }
        if chat_id:
            data["chat_id"]=chat_id
        if message_id:
            data["message_id"]=message_id
        if inline_message_id:
            data["inline_message_id"]=inline_message_id
        if reply_markup:
            data["reply_markup"]=zdgram.utils.reply_markup_parse(reply_markup)

        response = await self.sendRequest(
            "editMessageMedia",
            params=data,
            timeout=timeout
        )

        if isinstance(response.get("result"), dict):
            return zdgram.bot.update_manager._parse(
                zdgram.bot.message_manager._parse(
                    response.get("result")
                )
            )
        else:
            return True

    edit_message_media = editMessageMedia
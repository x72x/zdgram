import zdgram
from typing import Union

class EditMessageReplyMarkup:
    async def editMessageReplyMarkup(
            self: "zdgram.Bot",
            chat_id: Union[str, int] = None,
            message_id: int = None,
            inline_message_id: str = None,
            reply_markup: "zdgram.types.InlineKeyboardMarkup" = None,
            timeout: int = None,
    ) -> Union["zdgram.types.Message", bool]:
        """Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.
        https://core.telegram.org/bots/api#editmessagereplymarkup

        Args:

            chat_id (`Union[int, str]`, optional): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername). Default to None.

            message_id (`int`, optional): Required if inline_message_id is not specified. Identifier of the message to edit. Default to None.

            inline_message_id (`str`, optional): Required if chat_id and message_id are not specified. Identifier of the inline message. Default to None.

            reply_markup (`InlineKeyboardMarkup`, optional): A JSON-serialized object for an inline keyboard. Default to None.

        Returns:
            On success, if the edited message is not an inline message, the edited `Message` is returned, otherwise True is returned.

        Example:
            ```
            msg = await bot.sendMessage(
                chat_id,
                "hi",
                reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton("b1", url="url")
                        ]]
                )
            )
            await asyncio.sleep(2.5)
            await bot.editMessageReplyMarkup(msg.chat.id, msg.id, reply_markup=new_inline_keyboard_markup)
            ```
        """
        data = {}
        if chat_id:
            data["chat_id"]=chat_id
        if message_id:
            data["message_id"]=message_id
        if inline_message_id:
            data["inline_message_id"]=inline_message_id
        if reply_markup:
            data["reply_markup"]=zdgram.utils.reply_markup_parse(reply_markup)

        response = await self.sendRequest(
            "editMessageReplyMarkup",
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

    edit_message_reply_markup = editMessageReplyMarkup
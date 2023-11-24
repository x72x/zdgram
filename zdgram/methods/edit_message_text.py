import zdgram
from typing import Union, List
from json import dumps

class EditMessageText:
    async def editMessageText(
            self: "zdgram.Bot",
            text: str,
            chat_id: Union[str, int] = None,
            message_id: int = None,
            inline_message_id: str = None,
            parse_mode: str = None,
            entities: List["zdgram.types.MessageEntity"] = None,
            disable_web_page_preview: bool = None,
            reply_markup: "zdgram.types.InlineKeyboardMarkup" = None,
            timeout: int = None,
    ) -> Union["zdgram.types.Message", "bool"]:
        """Use this method to edit text and game messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.
        https://core.telegram.org/bots/api#editmessagetext

        Args:
            text (`str`): New text of the message, 1-4096 characters after entities parsing

            chat_id (Union[`str`, `int`], optional): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername). Defaults to None.

            message_id (`int`, optional): Required if inline_message_id is not specified. Identifier of the message to edit. Defaults to None.

            inline_message_id (`str`, optional): Required if chat_id and message_id are not specified. Identifier of the inline message. Defaults to None.

            parse_mode (`str`, optional): Mode for parsing entities in the message text. See formatting options for more details.. Defaults to None.

            entities (List[`zdgram.types.MessageEntity`], optional): A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode. Defaults to None.

            disable_web_page_preview (`bool`, optional): Disables link previews for links in this message. Defaults to None.

            reply_markup (`zdgram.types.InlineKeyboardMarkup`, optional): A JSON-serialized object for an inline keyboard.. Defaults to None.

        Returns:
            On success, if the edited message is not an inline message, the edited `Message` is returned, otherwise `True` is returned.

        Example:
            ```
            @bot.onMessage()
            async def on_message(bot: Bot, message: Message):
                msg = await bot.sendMessage(
                    message.chat.id, "Hi"
                )
                await asyncio.sleep(2.5)
                await bot.editMessageText(
                    "Hi 2",
                    chat_id=msg.chat.id,
                    message_id=msg.id
                )
            ```
        """
        data = {
            "text": text
        }
        if chat_id:
            data["chat_id"]=chat_id
        if message_id:
            data["message_id"]=message_id
        if inline_message_id:
            data["inline_message_id"]=inline_message_id
        if parse_mode is not None:
            data["parse_mode"]=parse_mode
        if entities:
            data['entities']=dumps([str(i) if isinstance(i, zdgram.types.MessageEntity) else i.__default__(i) for i in entities])
        if disable_web_page_preview is not None:
            data["disable_web_page_preview"]=disable_web_page_preview
        if reply_markup:
            data["reply_markup"]=zdgram.utils.reply_markup_parse(reply_markup)

        response = await self.sendRequest(
            "editMessageText",
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

    edit_message_text = editMessageText
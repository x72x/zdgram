import zdgram
import asyncio

class Listener:
    async def Listen(self: "zdgram.Bot", func: callable) -> "zdgram.types.Message":
        """Wait to get that message you need to it.

        Args:
            func (`callable`): filter func

        Returns:
            `zdgram.types.Message`: Returns Message type.

        Example:
            ```
            def filter_text_and_private(m: types.Message):
                return bool(m.text and m.chat.type == enums.ChatType.PRIVATE)

            @bot.onMessage(func=filter_text_and_private)
            async def on_message(bot: Bot, message: types.Message):
                await bot.sendMessage(
                    message.chat.id,
                    "Send your name",
                    reply_to_message_id=message.id
                )
                msg = await bot.listen(filter_text_and_private)
                return await bot.sendMessage(
                    message.chat.id,
                    "Your name is : " + msg.text
                )
            ```
        """
        self.add_listen_handler(func)
        loop = asyncio.get_event_loop()
        def _():
            while func in self._listener:
                pass
            return self._listener_cache.get(id(func))

        return await loop.run_in_executor(
            None, _
        )

    async def listenCallbackQuery(self: "zdgram.Bot", data: str) -> "zdgram.types.CallbackQuery":
        """Wait to get that callback query you need to it.

        Args:
            data (`str`): callback query data

        Returns:
            `zdgram.types.CallbackQuery`: Returns CallbackQuery

        Examples:
            ```
            def text_and_private(m: types.Message):
                return bool(m.text and m.chat.type == enums.ChatType.PRIVATE)

            @bot.onMessage(text_and_private)
            async def on_m(bot: Bot, message: types.Message):
                data = f"zaid:{message.chat.id}"
                await bot.sendMessage(
                    message.chat.id,
                    "Click on button",
                    reply_markup=types.InlineKeyboardMarkup(
                        [[types.InlineKeyboardButton("B", callback_data=data)]]
                    )
                )
                callback = await bot.listenCallbackQuery(data)
                await bot.answerCallbackQuery(
                    callback.id,
                    callback.from_user.first_name,
                    show_alert=True
                )
            ```
        """
        self.add_callback_listen_handler(data)
        loop = asyncio.get_event_loop()
        def _():
            while data in self._callback_listener:
                pass
            return self._callback_listener_cache.get(data)
        return await loop.run_in_executor(
            None, _
        )


    listen = Listen
    listen_callback_query = listenCallbackQuery
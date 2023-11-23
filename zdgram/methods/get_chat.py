import zdgram
from typing import Union, AsyncGenerator, Any

class GetChat:
    async def getChat(
            self: "zdgram.Bot",
            chat_id: Union["str", "int"],
            timeout: int = None
        ) -> "zdgram.types.Chat":
        """Use this method to get up to date information about the chat (current name of the user for one-on-one conversations, current username of a user, group or channel, etc.). Returns a Chat object on success.

        Args:
            chat_id (Union[str, int]): Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)

        Returns:
            zdgram.types.Chat: Returns a Chat object on success.
        """
        chat_id = chat_id.lower() if isinstance(chat_id, str) else chat_id
        if chat_id in self.cache:
            return self.cache.get(chat_id)
        respons = await self.sendRequest(
            "getChat",
            {
                "chat_id": chat_id
            },
            timeout=timeout
        )
        chat_object = zdgram.bot.update_manager._parse(zdgram.bot.chat_manager._parse(respons.get("result")))
        self.cache.update(
            {chat_id: chat_object}
        )
        return chat_object

    async def getChatAdministrators(
            self: "zdgram.Bot",
            chat_id: Union["str", "int"],
            timeout: int = None
    ) -> AsyncGenerator["zdgram.types.ChatMember", Any]:
        """Use this method to get a list of administrators in a chat, which aren't bots. Returns an Array of ChatMember objects.

        Args:
            chat_id (Union[str, int]): Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)

        Returns:
            AsyncGenerator[zdgram.types.ChatMember]: Returns an Array of ChatMember objects.
        """
        respons = await self.sendRequest(
            "getChatAdministrators",
            {
                "chat_id": chat_id
            },
            timeout=timeout
        )
        for i in respons.get("result"):
            x = zdgram.bot.update_manager._parse(i)
            yield x

    async def getChatMemberCount(
            self: "zdgram.Bot",
            chat_id: Union["str", "int"],
            timeout: int = None
    ) -> int:
        """Use this method to get the number of members in a chat. Returns Int on success.

        Args:
            chat_id (Union[&quot;str&quot;, &quot;int&quot;]): Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)

        Returns:
            int: Returns Int on success.
        """
        response = await self.sendRequest(
            "getChatMemberCount",
            {
                "chat_id": chat_id
            },
            timeout=timeout
        )
        return response.get("result")

    async def getChatMember(
            self: "zdgram.Bot",
            chat_id: Union["str", "int"],
            user_id: int,
            timeout: int = None
    ) -> "zdgram.types.ChatMember":
        """Use this method to get information about a member of a chat. The method is only guaranteed to work for other users if the bot is an administrator in the chat. Returns a ChatMember object on success.

        Args:
            chat_id (Union[&quot;str&quot;, &quot;int&quot;]): Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
            user_id (int): Unique identifier of the target user

        Returns:
            zdgram.types.ChatMember: Returns a ChatMember object on success.
        """
        response = await self.sendRequest(
            "getChatMember",
            {
                "chat_id": chat_id,
                "user_id": user_id
            },
            timeout=timeout
        )
        return zdgram.bot.update_manager._parse(response.get("result"))

    get_chat = getChat
    get_chat_administrators, get_chat_admins = getChatAdministrators, getChatAdministrators
    get_chat_member_count = getChatMemberCount
    get_chat_member = getChatMember
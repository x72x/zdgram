import aiohttp
import asyncio
import logging
import ssl
import certifi
import zdgram


from typing import Callable, Union, List
from json import loads
from .methods import Methods
from .types import Update, User, Message, Chat
from .handlers import Handlers
from .utils import all_updates

logger = logging.getLogger(__name__)

API_URL = "https://api.telegram.org/"

class SessionManager:
    # https://github.com/eternnoir/pyTelegramBotAPI/blob/f91f42321c95e0cedda483ba5442e0b4eee057c5/telebot/asyncio_helper.py#L31
    def __init__(self) -> None:
        self.session = None
        self.ssl_context = ssl.create_default_context(cafile=certifi.where())


    async def create_session(self):
        self.session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(
            limit=50,
            ssl_context=self.ssl_context
        ))
        return self.session

    async def get_session(self):
        if self.session is None:
            self.session = await self.create_session()
            return self.session

        if self.session.closed:
            self.session = await self.create_session()

        # noinspection PyProtectedMember
        if not self.session._loop.is_running():
            await self.session.close()
            self.session = await self.create_session()
        return self.session


session_manager = SessionManager()
update_manager = Update()
message_manager = Message()
user_manager = User()
chat_manager = Chat()

class Bot(Methods, Handlers):
    def __init__(
            self,
            bot_token: str,
            api_url: str = None,
            allowed_updates: List["str"] = None,
            parse_mode: str = None,
            disable_web_page_preview: bool = None,
            protect_content: bool = None,
            disable_notification: bool = None,
        ) -> None:
        """Auth the bot

        Args:
            bot_token (`str`): HTTP URL TOKEN

            api_url (`str`, optional): API Server URL. Defaults to https://api.telegram.org/.

            allowed_updates(`List[str]`, optional): List of allowed updates.

            parse_mode (`str`, optional): Default parse_mode.

            disable_web_page_preview (`bool`, optional): Pass true to disable all web page previews from the bot.

            protect_content (`bool`, optional): Protect all outgoing messages from the bot.

            disable_notification (`bool`, optional): Send all outgoing messages silently.

            ```
            from zdgram import Bot

            bot = Bot("TOKEN_HERE")
            ```
        """
        self.bot_token = bot_token
        self.parse_mode = parse_mode
        self.disable_web_page_preview = disable_web_page_preview
        self.protect_content = protect_content
        self.disable_notification = disable_notification
        self.version = zdgram.__version__
        self.__funcs = []
        self.__message_handlers = []
        self.__edited_message_handlers = []
        self.__callback_query_handlers = []
        self.__inline_query_handlers = []
        self.__chosen_inline_result_handlers = []
        self.__channel_post_handlers = []
        self.__edited_channel_post_handlers = []
        self.__my_chat_member_handlers = []
        self.__chat_member_handlers = []
        self.__chat_join_request_handlers = []
        self.__poll_handlers = []
        self.__poll_answer_handlers = []
        self.__shipping_query_handlers = []
        self.__pre_checkout_query_handlers = []
        self._listener = []
        self._listener_cache = {}
        self.cache = {}
        self.api = (api_url or API_URL) + "bot{}/{}"
        self.getUpdatesData = {
            "offset": -1,
            "allowed_updates": allowed_updates or all_updates,
            "limit": 100
        }
        self.me: Union["User", "None"] = None
        self.id = bot_token.split(':')[0]

    async def get_updates(self):
        updates = await self.sendRequest(
            method_name="getUpdates",
            params=self.getUpdatesData,
            timeout=55
        )
        for update in updates.get("result"):
            self.getUpdatesData.update(
                {"offset": update.get("update_id") + 1}
            )
            upd = update_manager._parse(update)
            logger.debug(
                "   New update at %s - Update id : %s",
                self.me.username,
                upd.update_id
            )
            for func in self.__funcs:
                asyncio.create_task(func(self, upd))
            if update.get("message"):
                _ = True
                for func in self.__message_handlers:
                    if (func['filter_func']) and not func['filter_func'](upd.message):
                        continue
                    for i in self._listener:
                        if i(upd.message):
                            _ = False
                            break
                    if not _:
                        continue
                    else:
                        logger.debug(
                            "   Creating TASK into %s , handler : %s",
                            func['func'].__name__,
                            "onMessage"
                        )
                        asyncio.create_task(func['func'](self, upd.message))
            if update.get("message"):
                for func in self._listener:
                    if not func(upd.message):
                        continue
                    else:
                        self._listener_cache.update(
                            {id(func): upd.message}
                        )
                        self._listener.remove(func)
            if update.get("edited_message"):
                for func in self.__edited_message_handlers:
                    if (func['filter_func']) and not func['filter_func'](upd.message):
                        continue
                    else:
                        logger.debug(
                            "   Creating TASK into %s , handler : %s",
                            func['func'].__name__,
                            "onEditedMessage"
                        )
                        asyncio.create_task(func['func'](self, upd.message))
            if update.get("callback_query"):
                for func in self.__callback_query_handlers:
                    if (func['filter_func']) and not func['filter_func'](upd.callback_query):
                        continue
                    else:
                        logger.debug(
                            "   Creating TASK into %s , handler : %s",
                            func['func'].__name__,
                            "onCallbackQuery"
                        )
                        asyncio.create_task(func['func'](self, upd.callback_query))
            if update.get("inline_query"):
                for func in self.__inline_query_handlers:
                    if (func['filter_func']) and not func['filter_func'](upd.inline_query):
                        continue
                    else:
                        logger.debug(
                            "   Creating TASK into %s , handler : %s",
                            func['func'].__name__,
                            "onInlineQuery"
                        )
                        asyncio.create_task(func['func'](self, upd.inline_query))
            if update.get("chosen_inline_result"):
                for func in self.__chosen_inline_result_handlers:
                    if (func['filter_func']) and not func['filter_func'](upd.chosen_inline_result):
                        continue
                    else:
                        logger.debug(
                            "   Creating TASK into %s , handler : %s",
                            func['func'].__name__,
                            "onChosenInlineResult"
                        )
                        asyncio.create_task(func['func'](self, upd.chosen_inline_result))
            if update.get("channel_post"):
                for func in self.__channel_post_handlers:
                    if (func['filter_func']) and not func['filter_func'](upd.message):
                        continue
                    else:
                        logger.debug(
                            "   Creating TASK into %s , handler : %s",
                            func['func'].__name__,
                            "onChannelPost"
                        )
                        asyncio.create_task(func['func'](self, upd.message))
            if update.get("edited_channel_post"):
                for func in self.__edited_channel_post_handlers:
                    if (func['filter_func']) and not func['filter_func'](upd.message):
                        continue
                    else:
                        logger.debug(
                            "   Creating TASK into %s , handler : %s",
                            func['func'].__name__,
                            "onEditedChannelPost"
                        )
                        asyncio.create_task(func['func'](self, upd.message))
            if update.get("my_chat_member"):
                for func in self.__my_chat_member_handlers:
                    if (func['filter_func']) and not func['filter_func'](upd.my_chat_member):
                        continue
                    else:
                        logger.debug(
                            "   Creating TASK into %s , handler : %s",
                            func['func'].__name__,
                            "onMyChatMember"
                        )
                        asyncio.create_task(func['func'](self, upd.my_chat_member))
            if update.get("chat_member"):
                for func in self.__chat_member_handlers:
                    if (func['filter_func']) and not func['filter_func'](upd.chat_member):
                        continue
                    else:
                        logger.debug(
                            "   Creating TASK into %s , handler : %s",
                            func['func'].__name__,
                            "onChatMember"
                        )
                        asyncio.create_task(func['func'](self, upd.chat_member))
            if update.get("chat_join_request"):
                for func in self.__chat_join_request_handlers:
                    if (func['filter_func']) and not func['filter_func'](upd.chat_join_request):
                        continue
                    else:
                        logger.debug(
                            "   Creating TASK into %s , handler : %s",
                            func['func'].__name__,
                            "onChatJoinRequest"
                        )
                        asyncio.create_task(func['func'](self, upd.chat_join_request))
            if update.get("poll"):
                for func in self.__poll_handlers:
                    if (func['filter_func']) and not func['filter_func'](upd.poll):
                        continue
                    else:
                        logger.debug(
                            "   Creating TASK into %s , handler : %s",
                            func['func'].__name__,
                            "onPoll"
                        )
                        asyncio.create_task(func['func'](self, upd.poll))
            if update.get("poll_answer"):
                for func in self.__poll_handlers:
                    if (func['filter_func']) and not func['filter_func'](upd.poll_answer):
                        continue
                    else:
                        logger.debug(
                            "   Creating TASK into %s , handler : %s",
                            func['func'].__name__,
                            "onPollAnswer"
                        )
                        asyncio.create_task(func['func'](self, upd.poll_answer))
            if update.get("shipping_query"):
                for func in self.__shipping_query_handlers:
                    if (func['filter_func']) and not func['filter_func'](upd.shipping_query):
                        continue
                    else:
                        logger.debug(
                            "   Creating TASK into %s , handler : %s",
                            func['func'].__name__,
                            "onShippingQuery"
                        )
                        asyncio.create_task(func['func'](self, upd.shipping_query))
            if update.get("pre_checkout_query"):
                for func in self.__pre_checkout_query_handlers:
                    if (func['filter_func']) and not func['filter_func'](upd.pre_checkout_query):
                        continue
                    else:
                        logger.debug(
                            "   Creating TASK into %s , handler : %s",
                            func['func'].__name__,
                            "onPreCheckoutQuery"
                        )
                        asyncio.create_task(func['func'](self, upd.pre_checkout_query))

    async def auto_clean_cache(self):
        while not await asyncio.sleep(600):
            self.cache.clear()
            logger.debug(
                "   Cache are cleared at %s",
                self.me.username
            )

    def add_any_update_handler(self, func_: Callable):
        self.__funcs.append(func_)
        logger.info(
            "   Added %s to any update handlers at %s",
            func_.__name__,
            self.id
        )

    def add_callback_query_handler(self, func_: Callable, func: Callable = None):
        self.__callback_query_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )
        logger.info(
            "   Added %s to callback_query handlers at %s",
            func_.__name__,
            self.id
        )

    def add_inline_query_handler(self, func_: Callable, func: Callable = None):
        self.__inline_query_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )
        logger.info(
            "   Added %s to inline_query handlers at %s",
            func_.__name__,
            self.id
        )

    def add_chosen_inline_result_handler(self, func_: Callable, func: Callable = None):
        self.__chosen_inline_result_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )
        logger.info(
            "   Added %s to chosen_inline_result handlers at %s",
            func_.__name__,
            self.id
        )

    def add_edited_message_handler(self, func_: Callable, func: Callable = None):
        self.__edited_message_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )
        logger.info(
            "   Added %s to edited_message handlers at %s",
            func_.__name__,
            self.id
        )

    def add_message_handler(self, func_: Callable, func: Callable = None):
        self.__message_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )
        logger.info(
            "   Added %s to message handlers at %s",
            func_.__name__,
            self.id
        )

    def add_channel_post_handler(self, func_: Callable, func: Callable = None):
        self.__channel_post_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )
        logger.info(
            "   Added %s to channel_post handlers at %s",
            func_.__name__,
            self.id
        )

    def add_edited_channel_post_handler(self, func_: Callable, func: Callable = None) -> Callable:
        self.__edited_channel_post_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )
        logger.info(
            "   Added %s to edited_channel_post handlers at %s",
            func_.__name__,
            self.id
        )

    def add_my_chat_member_handler(self, func_: Callable, func: Callable = None):
        self.__my_chat_member_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )
        logger.info(
            "   Added %s to my_chat_member handlers at %s",
            func_.__name__,
            self.id
        )

    def add_chat_member_handler(self, func_: Callable, func: Callable = None):
        self.__chat_member_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )
        logger.info(
            "   Added %s to chat_member handlers at %s",
            func_.__name__,
            self.id
        )

    def add_chat_join_request_handler(self, func_: Callable, func: Callable = None):
        self.__chat_join_request_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )
        logger.info(
            "   Added %s to chat_join_request handlers at %s",
            func_.__name__,
            self.id
        )

    def add_poll_handler(self, func_: Callable, func: Callable = None):
        self.__poll_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )
        logger.info(
            "   Added %s to poll handlers at %s",
            func_.__name__,
            self.id
        )

    def add_poll_answer_handler(self, func_: Callable, func: Callable = None):
        self.__poll_answer_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )
        logger.info(
            "   Added %s to poll_answer handlers at %s",
            func_.__name__,
            self.id
        )

    def add_shipping_query_handler(self, func_: Callable, func: Callable = None):
        self.__shipping_query_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )
        logger.info(
            "   Added %s to shipping_query handlers at %s",
            func_.__name__,
            self.id
        )

    def add_pre_checkout_query_handler(self, func_: Callable, func: Callable = None):
        self.__pre_checkout_query_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )
        logger.info(
            "   Added %s to pre_checkout_query handlers at %s",
            func_.__name__,
            self.id
        )

    def add_listen_handler(self, func: Callable = None):
        if func in self._listener:
            return
        self._listener.append(func)
        self._listener_cache.update(
            {id(func): None}
        )

    def __clear_bugs(self):
        _ = []
        for i in self.__funcs:
            if not asyncio.iscoroutinefunction(i):
                _.append(i.__name__)
                self.__funcs.remove(i)

        for i in self.__message_handlers:
            if not asyncio.iscoroutinefunction(i['func']):
                _.append(i['func'].__name__)
                self.__message_handlers.remove(i)

        for i in self.__edited_message_handlers:
            if not asyncio.iscoroutinefunction(i['func']):
                _.append(i['func'].__name__)
                self.__edited_message_handlers.remove(i)

        for i in self.__channel_post_handlers:
            if not asyncio.iscoroutinefunction(i['func']):
                _.append(i['func'].__name__)
                self.__channel_post_handlers.remove(i)

        for i in self.__edited_channel_post_handlers:
            if not asyncio.iscoroutinefunction(i['func']):
                _.append(i['func'].__name__)
                self.__edited_channel_post_handlers.remove(i)

        for i in self.__callback_query_handlers:
            if not asyncio.iscoroutinefunction(i['func']):
                _.append(i['func'].__name__)
                self.__callback_query_handlers.remove(i)

        for i in self.__inline_query_handlers:
            if not asyncio.iscoroutinefunction(i['func']):
                _.append(i['func'].__name__)
                self.__inline_query_handlers.remove(i)

        for i in self.__chosen_inline_result_handlers:
            if not asyncio.iscoroutinefunction(i['func']):
                _.append(i['func'].__name__)
                self.__chosen_inline_result_handlers.remove(i)

        for i in self.__my_chat_member_handlers:
            if not asyncio.iscoroutinefunction(i['func']):
                _.append(i['func'].__name__)
                self.__my_chat_member_handlers.remove(i)

        for i in self.__chat_member_handlers:
            if not asyncio.iscoroutinefunction(i['func']):
                _.append(i['func'].__name__)
                self.__chat_member_handlers.remove(i)

        for i in self.__chat_join_request_handlers:
            if not asyncio.iscoroutinefunction(i['func']):
                _.append(i['func'].__name__)
                self.__chat_join_request_handlers.remove(i)

        for i in self.__poll_handlers:
            if not asyncio.iscoroutinefunction(i['func']):
                _.append(i['func'].__name__)
                self.__poll_handlers.remove(i)

        for i in self.__poll_answer_handlers:
            if not asyncio.iscoroutinefunction(i['func']):
                _.append(i['func'].__name__)
                self.__poll_answer_handlers.remove(i)

        for i in self.__shipping_query_handlers:
            if not asyncio.iscoroutinefunction(i['func']):
                _.append(i['func'].__name__)
                self.__shipping_query_handlers.remove(i)

        for i in self.__pre_checkout_query_handlers:
            if not asyncio.iscoroutinefunction(i['func']):
                _.append(i['func'].__name__)
                self.__pre_checkout_query_handlers.remove(i)

        if _:
            msg = ", ".join(_)
            logger.info(
                "   Deleted %s handlers, because they're not coroutine functions", msg
            )

    async def start_polling(self):
        self.__clear_bugs()
        try:
            me = await self.getMe()
        except zdgram.exceptions.ApiException as x:
            if loads(str(x)).get("description") == "Not Found":
                raise zdgram.exceptions.BotTokenInvalid(
                    f"API TOKEN IS WRONG : {loads(str(x))}"
                )

        logger.info(
            "   Start polling at %s", me
        )
        self.me = me
        asyncio.create_task(self.auto_clean_cache())
        while True:
            await asyncio.create_task(self.get_updates())

    def run(self, coro=None):
        if coro:
            return asyncio.run(coro)
        return asyncio.run(self.start_polling())
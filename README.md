# Install :
```commandline
pip install -U zdgram
```

# How to use?
- Config your bot :
---
```python
from zdgram import Bot, types

API_TOKEN = "API_TOKEN_HERE"

bot = Bot(API_TOKEN, allowed_updates=["message"])
```

- Add handlers to recive updates from telegram:
---
- Any update from telegram:
```python
@bot.onUpdate
async def on_updates(bot: Bot, update: types.Update):
    print(update)
```

- message and edited_message:
```python
@bot.onMessage()
async def on_message(bot: Bot, message: types.Message):
    print(message)

@bot.onEditedMessage()
async def on_edited_message(bot: Bot, message: types.Message):
    print(message)

# Custom filter
def filter_admin(message: types.Message):
    admins = [123456789, 987654321]
    return bool(message.from_user.id in admins)

@bot.onMessage(func=filter_admin)
@bot.onEditedMessage(func=filter_admin)
async def on_custom_filter(bot: Bot, message: types.Message):
    print(message)

# Echo Bot
@bot.onMessage(func=lambda m: m.text)
async def echo(bot: Bot, message: types.Message):
    return await bot.sendMessage(
        message.chat.id,
        message.text,
        entities=message.entities
    )
```

- Callback Queries ~~( No CallbackQuery Methods currently )~~
```python
@bot.onCallbackQuery()
async def on_callback_query(bot: Bot, callback_query: types.CallbackQuery):
    return await bot.sendMessage(
        callback_query.message.chat.id,
        callback_query.data
    )
```

- Inline Queries ( No InlineQuery Methods currently )
```python
@bot.onInlineQuery()
async def on_inline_query(bot: Bot, inline_query: types.InlineQuery):
    print(inline_query)
```

- Start the bot:
---
```python
import logging

logging.basicConfig(level=logging.INFO)

bot.run()
```

- Start multiple bots:
---
```python
import logging

from zdgram import run_multiple_bots, Bot, types, enums

logging.basicConfig(level=logging.INFO)

bot_1 = Bot("API_TOKEN_1")
bot_2 = Bot("API_TOKEN_2")

@bot_1.onMessage()
@bot_2.onMessage()
async  def on_message(bot: Bot, message: types.Message):
    return await bot.sendMessage(
        message.chat.id,
        (await bot.getMe()).mention.markdown,
        parse_mode=enums.ParseMode.MARKDOWN
    )

bot_1.run(run_multiple_bots([bot_1, bot_2]))
```

- Create Listener ( Conversation ):
---
```python
from zdgram import types, enums, Bot

bot = Bot(bot_token="")

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

# LICENSE :
- [MIT](https://github.com/x72x/zdgram/blob/master/LICENSE)
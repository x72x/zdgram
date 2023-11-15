# Install :
```commandline
pip install shitgram==0.1.dev4
```

# How to use?
- Config your bot :
---
```python
from shitgram import Bot, types

API_TOKEN = "API_TOKEN_HERE"

bot = Bot(API_TOKEN)
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
async def on_message(bot: Bot, message: types.Update):
    print(message)

@bot.onEditedMessage()
async def on_edited_message(bot: Bot, message: types.Update):
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

- Callback Queries ( No CallbackQuery Methods currently )
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
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

asyncio.run(bot.start_polling())

# add allowed updates:
asyncio.run(bot.start_polling(allowed_updates=["message"]))
```

- Start multiple bots:
---
```python
import asyncio
import logging

from shitgram import run_multiple_bots, Bot, types, enums

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

asyncio.run(run_multiple_bots([bot_1, bot_2]))
```

# LICENSE :
- [MIT](https://github.com/x72x/shitgram/blob/master/LICENSE)
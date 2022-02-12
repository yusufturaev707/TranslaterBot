import logging, api

from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator
from oxfordLookup import getDefenitios

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=api.API_TOKEN)
dp = Dispatcher(bot)

translator = Translator()


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.reply(f"Assalomu aleykum {message.chat.username}. "
                        f"Tarjimon botiga xush kelibsiz.")


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.reply(f"Sizga qanday yordam kerak?")


@dp.message_handler()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text

        lookup = getDefenitios(word_id)
        if lookup:
            await message.reply(f"Word: {word_id} \nDefinitions: \n{lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
            else:
                await message.reply("Bunday so'z topilmadi.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

import json
import config

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json

bot = Bot('7713082479:AAGnRc_bPCWKIJNU5WMJLMsMO5cZRbCbYHY')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб-страницу', web_app = WebAppInfo(url='https://monge-bayir.github.io/index.github.io/')))
    await message.answer('Привет, мой друг!', reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name: {res["name"]}. Email: {res["email"]}. Phone: {res["phone"]}')


executor.start_polling(dp)
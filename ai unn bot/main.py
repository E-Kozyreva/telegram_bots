import bot_token
import buttons

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=bot_token.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет, нажми на кнопку ниже 🙃", reply_markup=buttons.hi)


@dp.message_handler()
async def bot_message(msg: types.Message):
    if msg.text == "Привет 👋":
        text = "Привет, выбери тип тренировки слов 😉"
        await bot.send_message(msg.from_user.id, text, reply_markup=buttons.traning)
    else:
        text = "Я тебя не понимаю, нажми на кнопку ниже 😶‍🌫️"
        await bot.send_message(msg.from_user.id, text, reply_markup=buttons.hi)


if __name__ == '__main__':
    executor.start_polling(dp)

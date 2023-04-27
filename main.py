from config import *
import rate
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import date


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.Message):
    reply_message = "Команды бота: \n/help - информация о доступных командах \n/crypto BTC ETH и т.д. - информация о стоимости криптовалюты\n"
    await bot.send_message(message.from_user.id, reply_message)


@dp.message_handler(commands=['crypto'])
async def send_currency_rate(message: types.Message):
    currencies = tuple(message.text.split()[1:])
    result = rate.get_rate(currencies)

    reply_message = f'Курс криптовалюты на {date.today().strftime("%d.%m.%y")}:\n'
    for k, v in result.items():
        reply_message += f'{k}:  {v}\n' if v is not None else f'{k}:  Нет данных\n'
    await bot.send_message(message.from_user.id, reply_message)


if __name__ == '__main__':
    executor.start_polling(dp)

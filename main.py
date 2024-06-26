from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
import string
import random

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)
async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы узнать с чем может помочь наш бот')
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands=['description'])
async def desc_command(message: types.Message):
    await message.answer('Данная команда умеет отправлять рандомные символы латинского алфавита')
    await message.delete()

@dp.message_handler()
async def send_random_letter(message: types.Message):
    await  message.reply(random.choice(string.ascii_letters))

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет я твой первый бот!')


@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Я помогу тебе..!')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup= on_startup)
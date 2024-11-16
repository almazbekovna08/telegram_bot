from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
import asyncio
import logging
import random
from config import token

bot=Bot(token=token)
dp=Dispatcher()

@dp.message(CommandStart())
async def start(message:types.Message):
    await message.answer('Привет! \nЭто игра "Угадай число". \nЧтобы начать игру напиши "Я готов(-а)"')

@dp.message(F.text.in_({'Я готова', 'я готова', 'Я готов', 'я готов'}))
async def ready(message: types.Message):
    await message.reply('Загадай число от 1 до 3')

@dp.message()
async def randomm(message: types.Message):
    number=random.choice([1, 2, 3])
    user_num=int(message.text)
    if user_num==number:
        await message.reply_photo(photo='https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
        await message.answer(f'Выбранное число было {number}')
    else:
        await message.reply_photo(photo='https://media.makeameme.org/created/sorry-you-lose.jpg')
        await message.answer(f'Выбранное число было {number}')

@dp.message()
async def error(message: types.Message):
     await message.reply('Я вас не понял. Введите корректный текст')

async def main():
        await dp.start_polling(bot)
if __name__=='__main__':
    try:
         asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход')

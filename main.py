import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.photo)
async def aussie(message: Message):
    list = ['Ого, какая прекрасная собака!','Вот это пёсель','Какой забавный зверь! ','Хороший мальчик!']
    aswer_photo = random.choice(list)
    await message.answer(aswer_photo)

@dp.message(F.text == 'Аусси')
async def aussie(message: Message):
    await message.answer('Австралийская овчарка прекрасно подойдет в качестве первой собаки, идеально впишется в семью с маленькими детьми, станет надежным компаньоном активным людям, которые проводят много времени на свежем воздухе и могут быть вместе с собакой достаточно продолжительное время в течение дня.')

@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://cs6.livemaster.ru/storage/0b/b7/595b05011d19e2352a060fb3061s.jpg','https://cs12.pikabu.ru/post_img/2022/12/18/12/167139399811471020.jpg','https://cs6.livemaster.ru/storage/15/a7/245a484ec82be7032dcece26e7op.jpg']
    rand_photo = random.choice(list)
    await message.answer_photo(photo = rand_photo, caption = 'Ого, какая прекрасная собака!')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start - Начало работы \n /help - Справка')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Приветствую, {message.from_user.full_name}. Я - бот")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

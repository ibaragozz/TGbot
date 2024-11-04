import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN, WEATHER_API
import random
import requests

bot = Bot(token=TOKEN)
dp = Dispatcher()
weather = bot(WEATHER_API)
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
    await message.answer('Этот бот умеет выполнять команды: \n /start - Начало работы \n /help - Справка \n /weather - Прогноз погоды на неделю \n /photo - Случайная фотография собачки')

@dp.message(Command('weather'))
async def weather_command(message: Message):
    response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API}&q=Москва&days=7')
    data = response.json()
    forecast = data['forecast']['forecastday'][0]['day']['condition']['text']  # Пример получения прогноза
    await message.answer(f'Прогноз погоды на неделю: {forecast}')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Приветствую, {message.from_user.full_name}. Я - бот")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import TOKEN, WEATHER_API
import random
import requests

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('video'))
async def video(message: Message):
    await message.answer()

@dp.message(Command('audio'))
async def audio(message: Message):
    await message.answer()

@dp.message(F.photo)
async def aussie(message: Message):
    list = ['Ого, какая прекрасная собака!','Вот это пёсель','Какой забавный зверь! ','Хороший мальчик!']
    aswer_photo = random.choice(list)
    await message.answer(aswer_photo)
    await bot.download(message.photo[-1].file_id, f'tmp/{message.photo[-1].file_id}.jpg')

@dp.message(F.text == 'Аусси')
async def aussie(message: Message):
    await message.answer('Австралийская овчарка прекрасно подойдет в качестве первой собаки, идеально впишется в семью с маленькими детьми, станет надежным компаньоном активным людям, которые проводят много времени на свежем воздухе и могут быть вместе с собакой достаточно продолжительное время в течение дня.')

@dp.message(Command('photo', prefix='$'))
async def photo(message: Message):
    list = ['https://cs6.livemaster.ru/storage/0b/b7/595b05011d19e2352a060fb3061s.jpg',
            'https://cs12.pikabu.ru/post_img/2022/12/18/12/167139399811471020.jpg',
            'https://cs6.livemaster.ru/storage/15/a7/245a484ec82be7032dcece26e7op.jpg']
    rand_photo = random.choice(list)
    await message.answer_photo(photo = rand_photo, caption = 'Ого, какая прекрасная собака!')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start - Начало работы \n /help - Справка \n /weather - Текущая погода \n /photo - Случайная фотография собачки')


@dp.message(Command('weather'))
async def weather_command(message: Message):

    api_key = WEATHER_API
    city = 'Severomorsk'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'


    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        temp = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']


        weather_report = (
            f"Погода в {city} сейчас:\n"
            f"Температура: {temp}°C\n"
            f"Описание: {weather_description.capitalize()}\n"
            f"Влажность: {humidity}%\n"
            f"Скорость ветра: {wind_speed} м/с"
        )
    else:
        weather_report = "Не удалось получить данные о погоде."


    await message.answer(weather_report)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Приветствую, {message.from_user.full_name}. Я - бот")

@dp.message()
async def start(message: Message):
    if message.text.lower() == 'тест':
    # await message.send_copy(chat_id=message.chat.id)
        await message.answer('Тестируем')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

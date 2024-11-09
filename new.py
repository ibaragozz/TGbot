# Создаем бота погоды для определенного юзера

import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import ContentType
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN, WEATHER_API
import aiohttp
import logging
import sqlite3

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

class Form(StatesGroup):
    name = State()
    age = State()
    city = State()

def init_db():
    conn = sqlite3.connect('user_data.db')
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    city TEXT NOT NULL)
    """)
    conn.commit()
    conn.close()

init_db()

@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer("Привет!\nКак тебя зовут?")
    await state.set_state(Form.name.state)

@dp.message(Form.name)
async def name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Сколько тебе лет?")
    await state.set_state(Form.age.state)

@dp.message(Form.age)
async def age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("В каком городе живешь?")
    await state.set_state(Form.city.state)

@dp.message(Form.city)
async def city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    user_data = await state.get_data()

    conn=sqlite3.connect('user_data.db')
    cur=conn.cursor()
    cur.execute("""
        INSERT INTO users (name, age, city) VALUES (?, ?, ?)""", (user_data['name'], user_data['age'], user_data['city']))
    conn.commit()
    conn.close()

    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.openweathermap.org/data/2.5/weather?q={user_data['city']}&appid={WEATHER_API}&units=metric') as resp:
            if resp.status == 200:
                weather_data = await resp.json()
                main = weather_data['main']
                weather = weather_data['weather'][0]
                temp = main['temp']
                humidity = main['humidity']
                description = weather['description']
                weather_report = (f'Погода в городе {user_data["city"]}: {description}, \nтемпература {temp}°C, \nвлажность {humidity}%, описание {weather["description"]}')
                await message.answer(weather_report)
            else:
                await message.answer('Не удалось получить данные о погоде.')
    await state.clear()







async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
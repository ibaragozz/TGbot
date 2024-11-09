# Создаем бота погоды для определенного юзера

import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import ContentType
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
import aiohttp
import logging
import sqlite3

vbot = Bot(token=TOKEN)
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
    name TEXT,
    age INTEGER,
    city TEXT)
    """)
    conn.commit()
    conn.close()

















async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
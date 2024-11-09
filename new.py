# import sqlite3
#
# conn = sqlite3.connect('bot.db')
# c = conn.cursor()
#
# c.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     age INTEGER,
#     grade TEXT)
#     """)
#
# conn.commit()
# conn.close()


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















async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
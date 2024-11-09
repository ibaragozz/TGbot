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
from config import TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import os
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Меню с кнопками
button_hi = KeyboardButton('Привет')
button_bye = KeyboardButton('Пока')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi, button_bye)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=greet_kb)

# Обработчик кнопки "Привет"
@dp.message_handler(lambda message: message.text == 'Привет')
async def greet_user(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')

# Обработчик кнопки "Пока"
@dp.message_handler(lambda message: message.text == 'Пока')
async def farewell_user(message: types.Message):
    await message.answer(f'До свидания, {message.from_user.first_name}!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
from aiogram import Bot, Dispatcher, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import asyncio
from config import TOKEN


# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

# Меню с кнопками
button_hi = KeyboardButton(text='Привет')
button_bye = KeyboardButton(text='Пока')
greet_kb = ReplyKeyboardMarkup(keyboard=[[button_hi], [button_bye]], resize_keyboard=True)

# Обработчик команды /start
@router.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=greet_kb)

# Обработчик кнопки "Привет"
@router.message(F.text == 'Привет')
async def greet_user(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')

# Обработчик кнопки "Пока"
@router.message(F.text == 'Пока')
async def farewell_user(message: types.Message):
    await message.answer(f'До свидания, {message.from_user.first_name}!')


@router.message(Command('links'))
async def send_links(message: types.Message):
    # Создаём инлайн-кнопки с URL-ссылками
    links_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Новости", url="https://www.fc-baltika.ru/news/")],
        [InlineKeyboardButton(text="Музыка", url="https://www.zaycev.net/")],
        [InlineKeyboardButton(text="Видео", url="https://www.rutube.com/")]
    ])

    await message.answer("Выберите ссылку:", reply_markup=links_kb)


@router.message(Command('dynamic'))
async def send_dynamic_keyboard(message: types.Message):
    # Начальная кнопка "Показать больше"
    show_more_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
    ])

    await message.answer("Выберите опцию:", reply_markup=show_more_kb)


# Обработчик нажатия на кнопку "Показать больше"
@router.callback_query(F.data == "show_more")
async def show_more_options(callback: CallbackQuery):
    # Замена кнопки на две новые "Опция 1" и "Опция 2"
    options_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
        [InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
    ])

    await callback.message.edit_text("Выберите опцию:", reply_markup=options_kb)


# Обработчики для кнопок "Опция 1" и "Опция 2"
@router.callback_query(F.data == "option_1")
async def option_1_selected(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали Опцию 1!")


@router.callback_query(F.data == "option_2")
async def option_2_selected(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали Опцию 2!")

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
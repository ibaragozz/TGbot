from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Кнопка1")],
        [KeyboardButton(text="Кнопка2"), KeyboardButton(text="Кнопка3")],
], resize_keyboard=True)

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Каталог", callback_data='catalog')],
   [InlineKeyboardButton(text="Новости", callback_data='news')],
   [InlineKeyboardButton(text="Профиль", callback_data='person')]
])

test = ['Кнопка1', 'Кнопка2', 'Кнопка3', 'Кнопка4']

# async def test_keyboard():
#     keyboard = ReplyKeyboardBuilder()
#     for k in test:
#         keyboard.add(KeyboardButton(text=k))
#     return keyboard.adjust(2).as_markup()

async def test_keyboard():
    keyboard = InlineKeyboardBuilder()
    for k in test:
        keyboard.add(InlineKeyboardButton(text=k, url='https://www.google.com/search?q=%D0%B1%D0%B0%D0%BB%D1%82%D0%B8%D0%BA%D0%B0+%D1%82%D1%83%D1%80%D0%BD%D0%B8%D1%80%D0%BD%D0%B0%D1%8F+%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0&oq=&gs_lcrp=EgZjaHJvbWUqCQgAECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQkxNDA2ajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8'))
    return keyboard.adjust(2).as_markup()
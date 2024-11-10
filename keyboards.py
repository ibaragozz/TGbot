from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
main = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Кнопка1")],
        [KeyboardButton(text="Кнопка2"), KeyboardButton(text="Кнопка3")],
], resize_keyboard=True)

inline = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Фото", url="https://moderndogmagazine.com/wp-content/uploads/2014/02/AustralianShepherd_AKC_Mary-Bloom.jpg")]
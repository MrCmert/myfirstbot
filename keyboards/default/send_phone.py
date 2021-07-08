from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

markup_request_phone = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(KeyboardButton('Відправити телефон з Telegram', request_contact=True))


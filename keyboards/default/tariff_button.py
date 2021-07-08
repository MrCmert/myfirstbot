from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from keyboards.inline.taryfy import inline_tariffs

tariffs = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Комфорт 100')],
              [KeyboardButton(text='Fiber 100')],
               [KeyboardButton(text='Гігабіт')],
              [KeyboardButton(text='Fiber 300')]], resize_keyboard=True)


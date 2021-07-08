from aiogram import types

from keyboards.inline import start_menu_keyboard
from loader import dp, bot


@dp.message_handler(commands=['start_menu'])
async def process_command(message: types.Message):
    await message.reply("Вход в головне меню", reply_markup=start_menu_keyboard.inline_kb_main)


@dp.message_handler(commands=['id'])
async def process_command(message: types.Message):
    await message.reply(f"Ваш id в цьому Telegram-bot:\n"
                        f"{message.from_user.id}")


@dp.callback_query_handler(text="send_facebook")
async def send_facebook(callback_query: types.CallbackQuery):
    await callback_query.message.edit_reply_markup()
    await bot.send_message(callback_query.from_user.id, text="https://www.facebook.com/OKINETua/")


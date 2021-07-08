from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import database
from data.config import ADMINS
from keyboards.inline import start_menu_keyboard
from loader import dp, _, bot

db = database.DBCommands()


@dp.message_handler(CommandStart())
async def register_user(message: types.Message):
    chat_id = message.from_user.id
    user = await db.add_new_user()
    id = user.id
    count_users = await db.count_users()
    lang = 'uk'
    await db.set_language(lang)
    # Для многоязычности, все тексты, передаваемые пользователю должны передаваться в функцию "_"
    # Вместо "текст" передаем _("текст")

    text = _("Вітаю вас!!\n")
    text2 = _("Зараз в базі {count_users}").format(count_users=count_users)
    if message.from_user.id == int(ADMINS[0]):
        await bot.send_message(ADMINS[0], text2)
    else:
        await bot.send_message(chat_id, text, reply_markup=start_menu_keyboard.inline_kb_main)


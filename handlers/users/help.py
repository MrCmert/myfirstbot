from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Почати роботу з ботом",
            "/help - Справка ",
            "/start_menu - Відкрити головне меню")
    
    await message.answer("\n".join(text))

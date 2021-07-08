from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import callback_query, ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default.send_phone import markup_request_phone
from keyboards.default.tariff_button import tariffs
from keyboards.inline import start_menu_keyboard
from loader import dp, bot


from loader import dp
from states.offers import Offer

admin_id = ADMINS

@dp.callback_query_handler(text="offers", state=None)
async def offer1(callback_query: types.CallbackQuery):
    await callback_query.message.edit_reply_markup()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text="Введіть пропозицію щодо покращення бота")
    # , reply_markup=markup_request_phone)

    # Вариант 1 - с помощью функции сет
    await Offer.offer.set()

    # Вариант 2 - с помощью first
    # await Test.first()


@dp.message_handler(state=Offer.offer)
async def offer2(message: types.Message, state: FSMContext):
    offer = message.text
    user_abon = message.from_user.username
    id_abon = message.from_user.id
    await message.answer("Дякуюємо. Ми обов'язково зробимо все для реалізації цього в боті")
    await bot.send_message(admin_id[0], f"@{user_abon},{id_abon}\n{offer}")
    # Вариант 1
    await state.finish()

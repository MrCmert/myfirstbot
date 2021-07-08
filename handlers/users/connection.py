from asyncio import sleep
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import callback_query, ReplyKeyboardRemove
from data.config import ADMINS
from keyboards.default.tariff_button import tariffs
from loader import dp, bot
from states.connection import Connection



@dp.callback_query_handler(text="connection", state=None)
async def enter_phone(callback_query: types.CallbackQuery):
    await callback_query.message.edit_reply_markup()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           text="Введіть номер телефону для зв'язку з вами")
                           #, reply_markup=markup_request_phone)
    await Connection.phone.set()


@dp.message_handler(state=Connection.phone)
async def address(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(phone=answer)
    await message.answer("Введіть адресу підключення")
    await Connection.next()


@dp.message_handler(state=Connection.address)
async def tariff(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(address=answer)
    #await message.answer(reply_markup=inline_tariffs)
    await message.answer("Оберіть тариф", reply_markup=tariffs)
    await Connection.next()


@dp.message_handler(state=Connection.tariff)
async def address(message: types.Message, state: FSMContext):
    # Достаем переменные
    data = await state.get_data()
    phone = data.get("phone")
    address = data.get("address")
    tariff = message.text
    user_abon = message.from_user.username
    await message.answer("Дякуємо!", reply_markup=ReplyKeyboardRemove())
    await message.answer(f"Ви ввели\n"
                         f"телефон: {phone}\n"
                         f"Адресу: {address}\n"
                         f"Тариф: {tariff}\n"
                         f"Очікуйте дзвінка оператора для визначення часу підключення\n"
                         f" і щодо додаткових послуг")
    text = f"Підключка @{user_abon} \nТелефон: {phone} Адрес: {address} Тариф: {tariff}"

    for admin in ADMINS:
        try:
            await bot.send_message(admin,
                                   f"Підключка @{user_abon} \n"
                                   f"Телефон: {phone} Адрес: {address} Тариф: {tariff}\n")
            await sleep(0.3)
        except Exception:
            pass
    await state.finish()



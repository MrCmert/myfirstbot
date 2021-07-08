from aiogram.dispatcher.filters.state import StatesGroup, State


class Connection(StatesGroup):
    phone = State()
    address = State()
    tariff = State()

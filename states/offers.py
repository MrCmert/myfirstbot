from aiogram.dispatcher.filters.state import StatesGroup, State


class Offer(StatesGroup):
    offer = State()

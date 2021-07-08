from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, _, bot


markup_request = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(KeyboardButton('Send phone number', request_contact=True))\
    .add(KeyboardButton('Send location', request_location=True))\



inline_bid = InlineKeyboardButton(_("Заявка на підключення"), callback_data='connection')
inline_cab = InlineKeyboardButton(_("Особистий кабинет"), url='https://stats.okinet.com.ua/index/main')
inline_chat = InlineKeyboardButton(_("Чат з оператором"), callback_data='chat', url='https://t.me/MrCmert')
#inline_setting = InlineKeyboardButton(_("Налаштування"), callback_data='setting')
inline_about_us = InlineKeyboardButton(_("Про нас"), url='https://okinet.com.ua/novyny/tekhnichni-roboty-2')
inline_offers_bot = InlineKeyboardButton(_("Пропозиції по покращенню бота"), callback_data="offers")
inline_facebook = InlineKeyboardButton(_("Ми в Facebook"), callback_data='send_facebook')
#inline_often_questions = InlineKeyboardButton(_("Часті запитання"), callback_data='often_question')
inline_kb_main = InlineKeyboardMarkup(row_width=1).add(inline_bid, inline_cab,
                                                       inline_chat, inline_about_us,
                                                       inline_offers_bot, inline_facebook)



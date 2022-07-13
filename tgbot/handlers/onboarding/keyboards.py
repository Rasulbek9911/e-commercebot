from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from tgbot.handlers.onboarding.static_text import PRODUCTS, PHONE, COMPUTER


def make_keyboard_for_start_command() -> ReplyKeyboardMarkup:
    buttons = [
        [PRODUCTS],
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def category() -> ReplyKeyboardMarkup:
    buttons = [
        [PHONE],
        [COMPUTER]
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def product_next(products) -> InlineKeyboardMarkup:
    for product in products:
        buttons = [
            [
                InlineKeyboardButton("⏪ orqaga", callback_data=f"back-{product.id}"),
                InlineKeyboardButton("⏩ oldinga", callback_data=f"next-{product.id}")
            ],
            [
                InlineKeyboardButton("🛒 savatchaga qoshish", callback_data="add")
            ]
        ]

    return InlineKeyboardMarkup(buttons)

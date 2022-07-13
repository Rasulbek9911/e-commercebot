import datetime

from django.utils import timezone
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from tgbot.handlers.onboarding import static_text
from tgbot.handlers.utils.info import extract_user_data_from_update
from tgbot.models import User
from .keyboards import make_keyboard_for_start_command, category, product_next
from telegram import ReplyKeyboardRemove
from product.models import Product


def command_start(update: Update, context: CallbackContext) -> None:
    u, created = User.get_user_and_created(update, context)

    if created:
        text = static_text.start_created.format(first_name=u.first_name)
    else:
        text = static_text.start_not_created.format(first_name=u.first_name)

    update.message.reply_text(text=text, reply_markup=make_keyboard_for_start_command())


def products_category(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="categoryni tanglang", reply_markup=category())


def products_phone(update: Update, context: CallbackContext) -> None:
    product = Product.objects.all().first()
    cap = f"{product.name}\n{product.description}\n narxi: {product.price}$"
    update.message.reply_photo(photo=product.image, caption=cap, reply_markup=product_next(product))


def next_data(update: Update, context: CallbackContext) -> None:
    print("keldi")

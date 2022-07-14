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
    products = Product.objects.all()
    product_next(products)
    update.message.reply_text(text="categoryni tanglang", reply_markup=category())


def products_phone(update: Update, context: CallbackContext) -> None:
    products = Product.objects.all()
    for i in products:
        cap = f"{i.name}\n{i.description}\n narxi: {i.price}$"
        update.message.reply_photo(photo=i.image, caption=cap, reply_markup=product_next(i.id))


def next_data(update: Update, context: CallbackContext) -> None:
    product_id = update.callback_query.data.split("-")[1]
    data = Product.objects.filter(id=int(product_id) + 1)
    print(data.name)

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Токен вашего бота
BOT_TOKEN = "8198124928:AAGtmS3rOMSMe6_IRY_xNGzE7hGDWLtMVvU"

# Пример меню ресторана
MENU = {
    "Салаты": {"Цезарь": 350, "Греческий": 300},
    "Горячие блюда": {"Мясо в горшочке": 700, "Кебаб": 450},
    "Напитки": {"Кофе": 150, "Чай": 100}
}

# Стартовая команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Меню", callback_data="menu")],
        [InlineKeyboardButton("Связаться с нами", callback_data="contact")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Добро пожаловать в наш ресторан! Чем могу помочь?", reply_markup=reply_markup)

# Показать меню
async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query:
        await query.answer()
        menu_text = "Меню ресторана:\n"
        for category, items in MENU.items():
            menu_text += f"\n{category}:\n"
            for dish, price in items.items():
                menu_text += f" - {dish}: {price} сом.\n"
        keyboard = [[InlineKeyboardButton("Назад", callback_data="back")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(menu_text, reply_markup=reply_markup)

# Контактная информация
async def contact_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query:
        await query.answer()
        contact_text = "Связаться с нами:\nТелефон: +996 507 001 835\nАдрес: ул. Ахунбаева, 101"
        keyboard = [[InlineKeyboardButton("Назад", callback_data="back")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(contact_text, reply_markup=reply_markup)

# Вернуться в главное меню
async def back_to_main(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query:
        await query.answer()
        keyboard = [
            [InlineKeyboardButton("Меню", callback_data="menu")],
            [InlineKeyboardButton("Связаться с нами", callback_data="contact")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Добро пожаловать в наш ресторан! Чем могу помочь?", reply_markup=reply_markup)

def main():
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(show_menu, pattern="menu"))
    application.add_handler(CallbackQueryHandler(contact_info, pattern="contact"))
    application.add_handler(CallbackQueryHandler(back_to_main, pattern="back"))

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()

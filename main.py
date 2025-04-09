import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Обкладинки", callback_data='covers')],
        [InlineKeyboardButton("Глави книги", callback_data='chapters')],
        [InlineKeyboardButton("Свідчення", callback_data='testimony')],
        [InlineKeyboardButton("Для киць", callback_data='kittens')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Тихий простір. Вибери, що тобі потрібно зараз:", reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'covers':
        await query.message.reply_text("Ось три обкладинки книги (UA, RU, EN):")
    elif query.data == 'chapters':
        await query.message.reply_text("Оберіть мову глав:")
    elif query.data == 'testimony':
        await query.message.reply_text("Свідчення тих, хто вижив:\n\n“Ти не зламалась — ти стала м’якішою.”")
    elif query.data == 'kittens':
        await query.message.reply_text("Це простір для киць. Тут не треба бути сильним. Просто будь.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == '__main__':
    main()

import logging
from scanport import *
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

tokenbot = "TELEGRAM_BOT_TOKEN"
chatid = TELEGRAM_CHAT_ID
portnormal = [NORMAL_PORT]


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id == chatid:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="This is bot for check open port")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm Sorry your chat ID isn't valid")
        return 0

async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    if update.effective_chat.id == chatid:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Wait a minutes")
        isi = scanport()
        for x in portnormal:
            for y in isi:
                if y == x:
                    await update.message.reply_text(text="Just normal port, no malicious port open")
                else:
                    await update.message.reply_text(text=f"ALERT! PORT {y} OPEN")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm Sorry your chat ID isn't valid")
        return 0
     
    
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Bot stopped")

if __name__ == '__main__':
    application = ApplicationBuilder().token(tokenbot).build()

    start_handler = CommandHandler('start', start)
    scan_handler = CommandHandler('scan', scan)
    stop_handler = CommandHandler('stop', stop)

    application.add_handler(start_handler)
    application.add_handler(scan_handler)
    application.add_handler(stop_handler)
    
    application.run_polling()

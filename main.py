from dotenv import load_dotenv
import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from handlers.unknown_command import unknown
from handlers.start import start
from handlers.error import error_handler
from handlers.image import receive_image


load_dotenv()

token = os.getenv("BOT_TOKEN")

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, receive_image))
    application.add_error_handler(error_handler)
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    application.run_polling()
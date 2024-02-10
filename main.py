from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from file_utils import resize_file

from handlers.duck import duck
from handlers.import_sticker_set import import_sticker_set
from handlers.unknown_command import unknown
from handlers.start import start
from handlers.error import error_handler

import caribou

load_dotenv()

token = os.getenv("BOT_TOKEN")

async def receive_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    photo_id = photo.file_id
    new_photo = await context.bot.get_file(photo_id)
    path = await new_photo.download_to_drive()

    updated_path = resize_file(path.as_posix())

    os.remove(path.as_posix())
    
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document=open(updated_path, 'rb'),
        filename="Resized.png"
    )

    os.remove(updated_path)

if __name__ == '__main__':
    db_path = 'db/bot.db'
    migrations_path = 'db/migrations'
    caribou.upgrade(db_path, migrations_path)
    
    application = ApplicationBuilder().token(token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler('duck', duck))
    application.add_handler(MessageHandler(filters.PHOTO, receive_image))
    application.add_handler(CommandHandler('import_sticker', import_sticker_set, has_args = True))
    application.add_error_handler(error_handler)
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    application.run_polling()
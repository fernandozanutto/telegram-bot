from dotenv import load_dotenv
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from file_utils import resize_file


load_dotenv()

token = os.getenv("BOT_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def duck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Quack!")

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
    application = ApplicationBuilder().token(token).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(CommandHandler('duck', duck))

    image_handler = MessageHandler(
        filters.PHOTO, receive_image
    )
    application.add_handler(image_handler)

    
    application.run_polling()
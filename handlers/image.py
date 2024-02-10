import os
from telegram import Update
from telegram.ext import ContextTypes
from file_utils import resize_file

async def receive_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text("Processing...")
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
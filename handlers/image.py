import io
from telegram import Update
from telegram.ext import ContextTypes
from PIL import Image


async def receive_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text("Processing image...")

    photo = update.message.photo[-1]
    photo_id = photo.file_id
    new_photo = await context.bot.get_file(photo_id)

    buffer = io.BytesIO()

    await new_photo.download_to_memory(buffer)

    resized_image = resize_file(buffer)

    await context.bot.send_document(
        chat_id=update.effective_chat.id,
        document=resized_image,
        filename="Resized.png"
    )


def resize_file(file_bytes: io.BytesIO) -> bytes:
    image = Image.open(file_bytes)
    
    sizes = image.size

    x = sizes[0]
    y = sizes[1]

    if x > y:
        ratio = x / 512
    else:
        ratio = y / 512

    new_x = x/ratio
    new_y = y/ratio

    new_image = image.resize((int(new_x), int(new_y)))
    
    bytes_io = io.BytesIO()

    new_image.save(bytes_io, 'PNG')

    return bytes_io.getvalue()

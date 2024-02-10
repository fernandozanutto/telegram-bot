from telegram import Update, Sticker, InputSticker, constants
from telegram.ext import ContextTypes
import emoji

def map_sticker_to_input_sticker(sticker: Sticker) -> InputSticker:
    return InputSticker(
        sticker=sticker.file_id,
        emoji_list=list(map(lambda x: x['emoji'], emoji.emoji_list(sticker.emoji)))
    )

async def import_sticker_set(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        sticker_set = await context.bot.get_sticker_set(context.args[0])
    except:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Stickers não encontrados")
        return
    
    new_name = sticker_set.name + '_by_' + context.bot.username

    try:
        await context.bot.get_sticker_set(new_name)
        already_exists = True
    except:
        already_exists = False

    if not already_exists:
        input_sticker = list(
            map(
                map_sticker_to_input_sticker,
                sticker_set.stickers
            )
        )

        result = await context.bot.create_new_sticker_set(
            user_id=update.effective_message.from_user.id,
            name=new_name,
            title=sticker_set.title,
            stickers=input_sticker,
            sticker_format=constants.StickerFormat.STATIC
        )
    else:
        result = True

    if result:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Stickers: t.me/addstickers/" + new_name)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Falha")
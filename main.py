import os
import argparse
import asyncio
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

from handlers.unknown_command import unknown
from handlers.start import start
from handlers.error import error_handler
from handlers.image import receive_image

eventLoop = asyncio.new_event_loop()
asyncio.set_event_loop(eventLoop)

token = os.getenv("BOT_TOKEN")

application = ApplicationBuilder().token(token).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.PHOTO, receive_image))
application.add_error_handler(error_handler)
application.add_handler(MessageHandler(filters.COMMAND, unknown))

async def process_request(request):
    await application.initialize()

    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)

    return "event processed successfully"

def webhook(request):
    if request.method == "POST":
        return eventLoop.run_until_complete(process_request(request))
    
    return request.method

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--local", const=True, dest='local', default=False, nargs='?')
    args = parser.parse_args()

    if args.local:
        application.run_polling()
import asyncio
import os
import random

from telegram import Update
from telegram.error import RetryAfter
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from main import parse
from utils import write_to_file, create_text
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

# Search command
async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

# Xyu
    while True:
        data = parse()
        for xata in data:
            try:
                text = create_text(xata)
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=text
                )
                write_to_file(xata.get("link"))
                await asyncio.sleep(1)
            except RetryAfter as _:
                await asyncio.sleep(60)
                text = create_text(xata)
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=text
                )
                continue
        await asyncio.sleep(random.choice(range(60, 300)))


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("search", search_command))

    print("Bot is running...")
    app.run_polling()

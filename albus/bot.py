import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
from .converter import convert_file, split_extension, join_extension
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the Telegram bot token from the environment variables
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! Send me a file and I will convert it for you.')

async def convert_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_id = update.message.document.file_id
    file_name_full = update.message.document.file_name

    file_name, file_extension = split_extension(file_name_full)

    # Download the file
    file_ptr = await context.bot.get_file(file_id)
    file_path = f"{file_ptr.file_unique_id}.{file_extension}"
    
    await file_ptr.download_to_drive(custom_path=file_path)

    # Convert the file
    converted_file_name, extension = convert_file(file_path)

    # Rename the file
    converted_file_path = join_extension(converted_file_name, extension)
    renamed_file_path = join_extension(file_name, extension)
    os.rename(converted_file_path, renamed_file_path)

    # Send the converted file back
    with open(renamed_file_path, 'rb') as document:
        await update.message.reply_document(document)

    # Clean up the files
    os.remove(file_path)
    os.remove(renamed_file_path)

def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ATTACHMENT, convert_document))

    print("Bot is online.")
    app.run_polling()

if __name__ == '__main__':
    main()

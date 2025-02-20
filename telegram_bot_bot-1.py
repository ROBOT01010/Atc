import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random
import string

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define a function to generate a random username and password
def generate_credentials():
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    return username, password

# Define the start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Use /generate to get a random username and password.')

# Define the generate command handler
def generate(update: Update, context: CallbackContext) -> None:
    username, password = generate_credentials()
    update.message.reply_text(f'Username: {username}\nPassword: {password}')

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("6239580055:AAGxNr4sLp3Spe35TtJaIWRu5P8KcD9vFqg")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("generate", generate))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
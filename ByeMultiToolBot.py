import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

AUTHORIZED_USERS = {
    '@DoxiStillAlive': 'Servus, hier kommst du zum verschlüsserungs ByeMulti Tool: Link',
    '@Dragzy_V2': 'Servus, hier kommst du zum verschlüsserungs ByeMulti Tool: Link',
    '@KairoIsAlive': 'Servus, hier kommst du zum verschlüsserungs ByeMulti Tool: Link',
    '@TrawaKurwa': 'Servus, hier kommst du zum verschlüsserungs ByeMulti Tool: Link',
    '@H0hes_cc': 'Servus, hier kommst du zum verschlüsserungs ByeMulti Tool: Link',
}

ACCESS_DENIED_MESSAGE = 'Du hast keinen Zugang zum Doxis ByeMulti Tool Bot!'

def start(update: Update, context: CallbackContext) -> None:
    user_username = update.effective_user.username
    if user_username in AUTHORIZED_USERS:
        message = AUTHORIZED_USERS[user_username]
        update.message.reply_text(message)
    else:
        update.message.reply_text(ACCESS_DENIED_MESSAGE)

def main() -> None:
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

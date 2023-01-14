import logging
from telegram import Update
from telegram.ext import ApplicationBuilder
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters
import config
import requests

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    start_message = 'به ربات خوش آمدید\n با این ربات میتونید امتیاز imdb فیلم و سریال ها رو ببینید \n کافیه اسم اون فیلم یا سریال رو برفرستید.'
    await update.message.reply_text(start_message)


def get_rating(title: str) -> float:
    """get movie/series title
    return rating"""
    
    sess = requests.session()

    sess.headers = {
	    "X-RapidAPI-Key": config.RapidAPI_Key,
	    "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
    }

    # get title id
    querystring = {"q": title}
    url = "https://online-movie-database.p.rapidapi.com/auto-complete"
    titleid = sess.get(url, params=querystring).json()['d'][0]['id']

    # get rating
    querystring = {"tconst": titleid}
    url = "https://online-movie-database.p.rapidapi.com/title/get-ratings"
    rating = sess.get(url, params=querystring).json()['rating']

    return float(rating)


async def search_in_imdb(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_chat_action('typing')
    await update.message.reply_text(get_rating(update.message.text), quote=True)


def main() -> None:
    application = ApplicationBuilder().token(config.TOKEN).build()

    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(MessageHandler(filters.TEXT, search_in_imdb))
    application.run_polling()


if __name__ == '__main__':
    main()

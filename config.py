import os
import openai
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

openai.api_key = os.getenv('OPENAI_API_KEY')
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram.filters import CommandStart

bot = Bot(token="6874772287:AAFU8fyd-TQIO9gxttbe5wO3uTj8qnbmHGI")
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Новини"),
            types.KeyboardButton(text="Вчителі"),
            types.KeyboardButton(text="Розклад"),
            types.KeyboardButton(text="OpenAI"),
            types.KeyboardButton(text="Адмінпанель")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Оберіть одну з кнопок:"
    )
    await message.answer("Оберіть одну з кнопок:", reply_markup=keyboard)

@dp.message(F.text.lower() == "новини")
async def news(message: types.Message):
    await message.reply("У нас є гарні новини! Перейдіть за посиланням, щоб побачити свіжу інформацію: http://inter4.zp.ua/news")

@dp.message(F.text.lower() == "вчителі")
async def teachers(message: types.Message):
    await message.reply("Учителі завжди готові вам допомогти! Ось педагоги нашої школи: http://inter4.zp.ua/teacher/view_one/?parent_id=2")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
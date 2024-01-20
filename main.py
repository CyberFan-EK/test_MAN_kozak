import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram.filters import CommandStart
from config import *
import os
import openai

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Новини"),
            types.KeyboardButton(text="Вчителі"),
            types.KeyboardButton(text="Розклад"),
            types.KeyboardButton(text="Інше"),
            types.KeyboardButton(text="Адмінпанель")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Оберіть одну з кнопок:"
    )
    await message.answer("Вас вітає Бот-Козак, який завжди готовий прийти на допомогу! Оберіть одну з кнопок, щоб я зміг бути Вам корисним:", reply_markup=keyboard)

@dp.message(F.text.lower() == "новини")
async def news(message: types.Message):
    await message.reply("У нас є гарні новини! Перейдіть за посиланням, щоб побачити свіжу інформацію: http://inter4.zp.ua/news")

@dp.message(F.text.lower() == "вчителі")
async def teachers(message: types.Message):
    await message.reply("Вчителі завжди готові вам допомогти! Ось педагоги нашої школи: http://inter4.zp.ua/teacher/view_one/?parent_id=2")

@dp.message(F.text.lower() == "розклад")
async def schedule(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="5"),
            types.KeyboardButton(text="6"),
            types.KeyboardButton(text="7"),
            types.KeyboardButton(text="8"),
            types.KeyboardButton(text="9"),
            types.KeyboardButton(text="10"),
            types.KeyboardButton(text="11")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Оберіть свій клас:"
    )
    await message.answer("Оберіть свій клас:", reply_markup=keyboard)

@dp.message(F.text.lower() == "5")
async def five(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "6")
async def six(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "7")
async def seven(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")
@dp.message(F.text.lower() == "8")
async def eight(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "9")
async def nine(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "10")
async def ten(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "11")
async def eleven(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")



@dp.message(F.text.lower() == "інше")
async def ai(prompt):
    try:
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Тебе звати Козак. Ти готовий допомогти учням із їх запитаннями щодо навчання або організаці навчального процесу"
                },
                {
                    "role": "assistant",
                    "content": prompt
                    }
            ],
        )

        return completion.choices[0].message.content
    except:
        return None
    
@dp.message()
async def message_handler(message: types.Message):
    answer = await ai(message.text)
    if answer != None:
        await message.reply(answer)
    else:
        await message.reply("Виникла помилка, спробуйте ще раз.")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
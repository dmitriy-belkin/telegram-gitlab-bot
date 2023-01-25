#!/usr/bin/env python3

import logging
from aiogram import Bot, Dispatcher, executor, types


# class ApiConfig():
gitlab_token = "-----"
chat_id = "-----"
API_TOKEN = "----"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
vex = Dispatcher(bot)
    

@vex.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm Vex!\nPowered by Dmitriy Belkin.")
    
@vex.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(vex, skip_updates=True)
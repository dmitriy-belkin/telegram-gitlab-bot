#!/usr/bin/python

import requests
import apiconfig
from aiogram import executor, types


@vex.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm Vex!\nPowered by Dmitriy Belkin.")
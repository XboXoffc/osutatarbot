from telebot.async_telebot import AsyncTeleBot
from telebot import types
import config
import tokens
import sqlite3
import os

DATA_PATH = config.DATA_PATH
DB = config.DB
OSU_MAP_PATH = config.OSU_MAP_PATH
bot = AsyncTeleBot(tokens.TG)

async def main(message:types.Message):
    text:str = ''
    if not os.path.exists(DATA_PATH):
        os.mkdir(DATA_PATH)
        text += f'{DATA_PATH} created\n'
    else:
        text += f'{DATA_PATH} already exists\n'

    if not os.path.exists(OSU_MAP_PATH):
        os.mkdir(OSU_MAP_PATH)
        text += f'{OSU_MAP_PATH} created\n'
    else:
        text += f'{OSU_MAP_PATH} already exists\n'

    if not os.path.exists(DB):
        os.mknod(DB)
        text += f'{DB} created\n'
    else:
        text += f'{DB} already exists\n'

    text += '\n'

    with sqlite3.connect(DB) as db:
        cursor = db.cursor()
        query = f"""CREATE TABLE IF NOT EXISTS users(
                        tg_id INTEGER UNIQUE,
                        tg_username TEXT,
                        osu_id INTEGER,
                        osu_nick TEXT,
                        name TEXT,
                        city TEXT,
                        year INTEGER
                    ) """
        cursor.execute(query)
        text += f'1. {DB} initialized\n'


    await bot.reply_to(message, text)







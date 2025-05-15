from telebot.async_telebot import AsyncTeleBot
from telebot import types
import asyncio
import tokens
import validators
from src import start, reg, init
from src.osu import osuapi, score, osucallback

OSU_ID = tokens.OSU_ID
OSU_TOKEN = tokens.OSU_TOKEN
OSU_API_VER = tokens.OSU_API_VER
osu_api = osuapi.Osu(OSU_ID, OSU_TOKEN, OSU_API_VER)
bot = AsyncTeleBot(tokens.TG)

@bot.message_handler(func=lambda message: True, chat_types=['private'])
async def main(message:types.Message):
    msg:str = message.text
    msgsplit:list = msg.split()

    if msgsplit[0] == '/start':
        await start.main(message)
    elif msgsplit[0] == '/reg':
        await reg.main(message, msgsplit, osu_api)
    elif msgsplit[0] == '/init':
        await init.main(message)
    elif validators.url(msgsplit[0]):
        await score.main(message, msgsplit, osu_api)



@bot.callback_query_handler(func=lambda call:True)
async def callback(call:types.CallbackQuery):
    data = call.data.split('_')
    if data[0] == 'osu':
        await osucallback.main(call)




print("БОТ ЗАПУЩЕН\n\n")
asyncio.run(bot.polling(True))








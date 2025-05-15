from telebot.async_telebot import AsyncTeleBot
from telebot import types
import tokens
from src import other, db
from src.osu import osuapi

bot = AsyncTeleBot(tokens.TG)

async def main(message:types.Message, msgsplit:list, osu_api:osuapi.Osu):
    text:str = ''
    response = None
    if len(msgsplit) > 3:
        if await other.isint(msgsplit[2]):
            name:str = msgsplit[1]
            year:int = int(msgsplit[2])
            city:str = msgsplit[3]
            nick:str = '_'.join(msgsplit[4:])
            
            response = osu_api.profile(nick).json()
                
            if type(response) == dict:
                data = {
                    "tg_id": message.from_user.id,
                    "tg_username": message.from_user.username, 
                    "osu_id": response['id'], 
                    "osu_nick": nick, 
                    "name": name, 
                    "city": city, 
                    "year": year
                }
                if await db.main('reg', data):
                    text += f'Твои данные были записаны,\n'
                    text += f'Имя: {name}\n'
                    text += f'Год Рождения: {year}\n'
                    text += f'Город: {city}\n'
                    text += f'Ник: {nick}'
                else:
                    text += 'Что то не получилось...'
            else:
                text += 'Ошибка: такого никнейма не существует'
        else:
            text += f'Напиши год рождения числом, дебил чтоле писать буквами год рождения'
    else:
        text += f'Напиши свои данные в таком формате `/reg <Имя> <Год Рождения> <Город> <Ник>`'
    
    await bot.reply_to(message, text, parse_mode='MARKDOWN')
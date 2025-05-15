import sqlite3
import config

DB = config.DB

async def main(mode:str, data:dict):
    if mode == 'reg':
        return await reg(data['tg_id'], data['tg_username'], data['osu_id'], data["osu_nick"], data['name'], data['city'], data['year'])


async def reg(tg_id:int, tg_username:str, osu_id:int, osu_nick:str, name:str, city:str, year:int):
    try:
        with sqlite3.connect(DB) as db:
            cursor = db.cursor()
            query = f"""REPLACE INTO users(tg_id, tg_username, osu_id, osu_nick, name, city, year)
                        VALUES({tg_id}, '{tg_username}', {osu_id}, '{osu_nick}', '{name}', '{city}', {year})"""
            cursor.execute(query)

        return True
    except Exception as e:
        print(e)
        return False













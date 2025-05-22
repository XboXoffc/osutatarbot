from telebot.async_telebot import AsyncTeleBot
from telebot import types
import config
import tokens
from src.osu import osuapi, templates

CHAT_ID = config.CHAT_ID
bot = AsyncTeleBot(tokens.TG)

async def main(message:types.Message, msgsplit:list, osu_api:osuapi.Osu):
    Url:str = msgsplit[0]
    UrlSplit:list = Url.split('/')
    base_url:str = UrlSplit[2]
    if base_url == 'osu.ppy.sh' and UrlSplit[3] == 'scores':
        score_id:int = int(UrlSplit[4])
        score_res:dict = await osu_api.get_score(score_id)
        if score_res != {'error': "Specified Solo\\Score couldn't be found."} :
            tg_username = message.from_user.username
            tg_name = message.from_user.first_name
            tg_id = message.from_user.id
            userid = score_res['user']['id']
            beatmapid = score_res['beatmap']['id']
            ruleset_id = score_res['ruleset_id']
            if ruleset_id == 0:
                mode = 'osu'
            elif ruleset_id == 1:
                mode = 'mania'
            elif ruleset_id == 2:
                mode = 'taiko'
            elif ruleset_id == 3:
                mode = 'fruits'

            profile_res:dict = await osu_api.profile(userid, mode, True)
            beatmap_res:dict = await osu_api.beatmap(beatmapid)

            text = await templates.main(mode, score_res, beatmap_res, profile_res)
            text += '\n'
            if len(msgsplit) > 1:
                comment = ' '.join(msgsplit[1:])
                text += '\n'
                text += '```Comment\n'
                text += f'''{comment}\n'''
                text += '```'
            text += '\n'
            text += '#скоры\n'
            text += f'''👤 `{tg_name}({tg_username}, {tg_id})`'''

            markup = types.InlineKeyboardMarkup()
            ButtonSend = types.InlineKeyboardButton('✅Отправить✅', callback_data=f'osu_score_send@{tg_id}@{message.id}')
            ButtonReject = types.InlineKeyboardButton('❌Отклонить❌', callback_data=f'osu_score_reject@{tg_id}@{message.id}')
            markup.add(ButtonSend, ButtonReject)
            await bot.send_message(CHAT_ID, text, parse_mode='MARKDOWN', link_preview_options=types.LinkPreviewOptions(False, beatmap_res['beatmapset']['covers']['card@2x'], prefer_large_media=True, show_above_text=True), reply_markup=markup)
            await bot.reply_to(message, 'Ваш скор был отправлен на модерацию')
        else:
            text = 'Ошибка: Нету такого скора!'
            await bot.reply_to(message, text, parse_mode='MARKDOWN')
    else:
        text = 'Ошибка: Вставляйте ссылки только в формате `https://osu.ppy.sh/scores/<айди скора>`'
        await bot.reply_to(message, text, parse_mode='MARKDOWN')

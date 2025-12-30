from telebot.async_telebot import AsyncTeleBot
from telebot import types
import tokens, config

ACCESS_USERS:list = config.ACCESS_LIST
CHANNEL_ID:int = config.CHANNEL_ID
CHAT_ID:int = config.CHAT_ID
bot = AsyncTeleBot(tokens.TG)

async def main(call:types.CallbackQuery):
    calldata = call.data.split('@')
    if calldata[0] in ['osu_score_send', 'osu_score_reject'] and call.from_user.id in ACCESS_USERS:
        userid = calldata[1]
        messageid = calldata[2]
        if calldata[0] == 'osu_score_send':
            text = call.message.text
            entities = call.message.entities
            await bot.send_message(CHANNEL_ID, text, link_preview_options=call.message.link_preview_options, entities=entities)
            await bot.delete_message(CHAT_ID, call.message.id)
            await bot.send_message(userid, 'Ваш скор был успешно одобрен✅', reply_to_message_id=messageid)
        elif calldata[0] == 'osu_score_reject':
            await bot.edit_message_text(f'Пост отклонен {call.from_user.first_name}({call.from_user.username}, {call.from_user.id})', CHAT_ID, call.message.id)
            await bot.send_message(userid, 'Ваш скор был отклонен❌', reply_to_message_id=messageid)
    elif calldata[0] in ['osu_score_send', 'osu_score_reject'] and call.from_user.id not in ACCESS_USERS:
        await bot.answer(call.id, 'Вы не модератор если что')





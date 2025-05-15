from telebot.async_telebot import AsyncTeleBot
import tokens

bot = AsyncTeleBot(tokens.TG)

async def main(message):
    text = '''Привет!\n'''
    text += 'Это предложка канала @osutatarstan и чата @osutatar\n'
    text += '`/reg <Имя> <Год Рождения> <Город> <Ник>` - это регистрация, её можно пропустить\n'
    text += 'Чтобы отправлять скоры, просто скинь ссылку со скором по типу `https://osu.ppy.sh/scores/<айди скора>`\n'
    text += 'Разраб: @xbox202'
    await bot.reply_to(message, text, parse_mode='MARKDOWN')
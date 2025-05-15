async def isint(obj):
    try:
        obj = int(obj)
        return True
    except:
        return False

async def time(time: str):
    time.replace('Z', '')
    timesplit = time.split('T')
    date = timesplit[0].split('-')
    time = timesplit[1].split(':')
    year = date[0]
    month = date[1]
    day = date[2]
    hour = time[0]
    minute = time[1]
    second = time[2]
    datetime = {
        'year': year,
        'month': month,
        'day': day,
        'hour': hour,
        'min': minute,
        'sec': second
    }
    return datetime
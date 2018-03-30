from datetime import timedelta, datetime

def string_to_timedelta(datestr):
    t = datetime.strptime(datestr, '%H:%M:%S')
    return timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)

from datetime import datetime


def get_weekday(datetime_obj):
    return datetime_obj.strftime('%A')

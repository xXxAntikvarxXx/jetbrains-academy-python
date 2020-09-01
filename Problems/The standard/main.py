from datetime import datetime


def convert_to_standard(datetime_obj):
    return datetime_obj.strftime("%Y-%m-%d")

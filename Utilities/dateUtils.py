from datetime import date, timedelta
import calendar


def get_day_of_week():
    today_date = date.today()
    return calendar.day_name[today_date.weekday()]


def get_last_monday_date():
    today_date = date.today()
    day_gap = 0 - today_date.weekday()
    if day_gap >= 0:
        day_gap -= 7
    return today_date + timedelta(days=day_gap)


def check_new_week():
    if (get_last_monday_date() - date.today()).days >= -7:
        return False
    else:
        return True


def get_yesterday_day_of_week():
    yesterday = date.today() - timedelta(days=1)
    return calendar.day_name[yesterday.weekday()]

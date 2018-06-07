from datetime import date, timedelta
import calendar


# functions using dates

# returns the day of the week [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
def get_day_of_week():
    today_date = date.today()
    return calendar.day_name[today_date.weekday()]


# gives us the calendar day of the last monday, will be used to determine if we have started a new week
def get_last_monday_date():
    today_date = date.today()
    day_gap = 0 - today_date.weekday()
    if day_gap >= 0:
        day_gap -= 7
    return today_date + timedelta(days=day_gap)


# check if we have started a new week
def check_new_week():
    if (get_last_monday_date() - date.today()).days >= -7:
        return False
    else:
        return True


# dont think this is getting used at the moment... I had a plan for it, hmmm.
def get_yesterday_day_of_week():
    yesterday = date.today() - timedelta(days=1)
    return calendar.day_name[yesterday.weekday()]

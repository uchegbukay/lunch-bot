from Utilities import dataManipulation as dataUtils
from Utilities import dateUtils
import os.path

preferences = {}


# adds the days of the week to a file
def create_new_lunch_memory():
    with open('lunchMemory.txt', 'w') as f:
        f.write("Monday=\n")
        f.write("Tuesday=\n")
        f.write("Wednesday=\n")
        f.write("Thursday=\n")
        f.write("Friday=\n")


def get_previous_lunches():
    if dateUtils.check_new_week():
        create_new_lunch_memory()

    elif not os.path.isfile('lunchMemory.txt') or os.path.getsize('lunchMemory.txt') <= 0:
        create_new_lunch_memory()

    with open('lunchMemory.txt', 'r') as f:
        for line in f:
            line_array = dataUtils.remove_linefeed(line).split("=")
            if '=' in line:
                preferences[line_array[0]] = line_array[1]
    return preferences


# add a lunch to the file for today's day of the week
def add_lunch(place, past_lunches):
    day = dateUtils.get_day_of_week()

    with open('lunchMemory.txt', 'w') as f:
        for (k, v) in past_lunches.items():
            if day == k:
                f.write("%s=%s\n" % (day, place))
            else:
                f.write("%s=%s\n" % (k, v))

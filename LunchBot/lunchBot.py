from random import *
from LunchBot import preferenceLoader, memoryLoader, lunchLocations, dictionaryFilters


def lunch_bot():
    preferences = preferenceLoader.get_preferences()
    previous_lunches = memoryLoader.get_previous_lunches()

    lunch_locations = lunchLocations.get_locations()

    filtered_locations = dictionaryFilters.filter_locations(lunch_locations, preferences, previous_lunches)

    if not filtered_locations:
        print(
            '\nUnfortunately there are no lunch options for your preferences. Expand your horizon or don\'t be so picky.')
        exit(0)

    todays_lunch = ""
    while filtered_locations:
        todays_lunch = choice(list(filtered_locations))
        accept_lunch = input('How does ' + todays_lunch + ' sound for lunch today? (y/n)')
        if 'y' in accept_lunch.lower():
            memoryLoader.add_lunch(todays_lunch, previous_lunches)
            break
        else:
            del filtered_locations[todays_lunch]
            todays_lunch = ""

    if todays_lunch:
        print("\nGreat! lets head to %s. Can I recommend %s" % (
            todays_lunch, filtered_locations[todays_lunch]['recommendations']))
    else:
        print("\nI gave you all the options I could! You are on your own today.")

from random import *
import memoryLoader
import dictionaryFilters
import lunchLocations
import preferenceLoader


def lunch_bot():
    # grab our preferences and previous lunches from files, used to filter locations
    preferences = preferenceLoader.get_preferences()
    previous_lunches = memoryLoader.get_previous_lunches()

    # get our lunch locations
    lunch_locations = lunchLocations.get_locations()

    # given our lunch locations, preferences, and previous lunches get a narrowed down dictionary of possibilities
    filtered_locations = dictionaryFilters.filter_locations(lunch_locations, preferences, previous_lunches)

    # if no lunch locations exist after filtering....
    if not filtered_locations:
        print(
          '\nUnfortunately there are no lunch options for your preferences. Expand your horizon or don\'t be so picky.')
        # this exits the program without running anymore code
        exit(0)

    todays_lunch = ""
    # keep doing this logic until we run out of choices
    while filtered_locations:
        # 'list()' turns the dictionary into a list so we can randomly choose one
        todays_lunch = choice(list(filtered_locations))
        accept_lunch = input('How does ' + todays_lunch + ' sound for lunch today? (y/n)')
        if 'y' in accept_lunch.lower():
            memoryLoader.add_lunch(todays_lunch, previous_lunches)
            break  # if a lunch is selected break out of the while loop
        else:
            # if you dont want that lunch we will delete it from the choices and try again
            del filtered_locations[todays_lunch]
            todays_lunch = ""

    if todays_lunch:
        print("\nGreat! lets head to %s. Can I recommend %s" % (
            todays_lunch, filtered_locations[todays_lunch]['recommendations']))
    else:
        print("\nI gave you all the options I could! You are on your own today.")

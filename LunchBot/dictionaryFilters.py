def filter_locations(lunch_locations, preferences, previous_lunches):
    lunch_locations2 = {}
    final_lunch_locations = {}
    previous_places = {}

    for (pk, pv) in preferences.items():
        lunch_locations2 = {k: v for (k, v) in lunch_locations.items() if pk in v and v[pk] == pv}

    # switch the previous lunches around so we can use the place as a key to further filter lunch places
    for day, place in previous_lunches.items():
        previous_places[place] = day

    # get the lunch locations that we have not been to yet this week
    wanted = set(lunch_locations2) - set(previous_places)
    for wanted_key in wanted:
        final_lunch_locations[wanted_key] = lunch_locations2[wanted_key]

    return final_lunch_locations

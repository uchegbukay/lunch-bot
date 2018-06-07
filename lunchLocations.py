import yaml


def get_locations():

    with open('lunch_places.dat', 'r') as f:
        lunch_locations = f.read()
        lunch_locations = yaml.safe_load(lunch_locations)

    return lunch_locations

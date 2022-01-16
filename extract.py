"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
import os

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """
    Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A tuple of `NearEarthObject`s.
    """
    try:
        with open(neo_csv_path) as f:
            neos = csv.DictReader(f)
            return tuple(neos)
    except Exception as e:
        print('Something went wrong!', e)


def load_approaches(cad_json_path):
    """
    Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A tuple of `CloseApproach`es.
    """
    try:
        with open(cad_json_path) as f:
            reader = json.load(f)

            # Get the fields and data for the close approaches
            fields = reader.get('fields')
            data = reader.get('data')

            close_approaches = []
            for approach in data:
                # Create a close approach dictionary
                close_approach = {
                    fields[index]: value for index, value in enumerate(approach)}
                # Add it to the list of all close approaches
                close_approaches.append(close_approach)

        return tuple(close_approaches)
    except Exception as e:
        print('Something went wrong!', e)


# path = os.path.join(os.getcwd(), 'data/cad.json')
# print(len(load_approaches(path)))

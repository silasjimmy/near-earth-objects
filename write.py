"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )

    try:
        with open(filename, 'w') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in results:
                ca_data = row.serialize()
                neo_data = row.neo.serialize()

                data = {
                    'datetime_utc': ca_data.get('datetime_utc'),
                    'distance_au': ca_data.get('distance_au'),
                    'velocity_km_s': ca_data.get('velocity_km_s'),
                    'designation': neo_data.get('designation'),
                    'name': '' if neo_data.get('name') is None else neo_data.get('name'),
                    'diameter_km': neo_data.get('diameter_km'),
                    'potentially_hazardous': neo_data.get('potentially_hazardous')
                }
                writer.writerow(data)
    except Exception as e:
        print('Something went wrong!', e)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    try:
        data = []

        for result in results:
            ca_data = result.serialize()
            neo_data = result.neo.serialize()

            row = {
                'datetime_utc': ca_data.get('datetime_utc'),
                'distance_au': ca_data.get('distance_au'),
                'velocity_km_s': ca_data.get('velocity_km_s'),
                'neo': {
                    'designation': neo_data.get('designation'),
                    'name': '' if neo_data.get('name') is None else neo_data.get('name'),
                    'diameter_km': neo_data.get('diameter_km'),
                    'potentially_hazardous': neo_data.get('potentially_hazardous')
                }
            }

            data.append(row)

        with open(filename, 'w') as outfile:
            json.dump(data, outfile)
    except Exception as e:
        print('Something went wrong!', e)

# Explore Close Approaches of Near Earth Objects

In this project, you'll use Python - and the skills we've developed throughout this course - to search for and explore close approaches of near-Earth objects (NEOs), using data from NASA/JPL's Center for Near Earth Object Studies.

## Overview

THe project is a command-line tool to inspect and query a dataset of NEOs and their close approaches to Earth.
It reads data from both a CSV file and a JSON file, convert that data into structured Python objects, perform filtering operations on the data, limit the size of the result set, and write the results to a file in a structured format, such as CSV or JSON.

WHen you invoke the ```main.py``` script, you'll be able to inspect the properties of the near-Earth objects in the data set and query the data set of close approaches to Earth using any combination of the following filters:

- Occurs on a given date.
- Occurs on or after a given start date.
- Occurs on or before a given end date.
- Approaches Earth at a distance of at least (or at most) X astronomical units.
- Approaches Earth at a relative velocity of at least (or at most) Y kilometers per second.
- Has a diameter that is at least as large as (or at least as small as) Z kilometers.
- Is marked by NASA as potentially hazardous (or not).

## Understanding the Near-Earth Object Close Approach Datasets

This project contains two important data sets, and our first step will be to explore and understand the data containing within these structured files.

One dataset (`neos.csv`) contains information about semantic, physical, orbital, and model parameters for certain small bodies (asteroids and comets, mostly) in our solar system. The other dataset (`cad.json`) contains information about NEO close approaches - moments in time when the orbit of an astronomical body brings it close to Earth. NASA helpfully provides a [glossary](https://cneos.jpl.nasa.gov/glossary/) to define any unfamiliar terms you might encounter.

Importantly, these datasets come directly from NASA - we haven't dressed them up for you at all.


## Project Interface

Now that we understand the data with which we'll be working, let's dive into what our program will actually do

This project is driven by the `main.py` script. That means that you'll run `python3 main.py ... ... ...` at the command line to invoke the program that will call your code.

At a command line, you can run `python3 main.py --help` for an explanation of how to invoke the script.

There are three subcommands: `inspect`, `query`, and `interactive`. Let's take a look at the interfaces of each of these subcommands.

### `inspect`

The `inspect` subcommand inspects a single NEO, printing its details in a human-readable format. The NEO is specified with exactly one of the `--pdes` option (the primary designation) and the `--name` option (the IAU name). The `--verbose` flag additionally prints out, in a human-readable form, all known close approaches to Earth made by this NEO. Each of these options has an abbreviated version.

```
$ python3 main.py inspect ...
```

For an NEO to be found with the `inspect` subcommand, the given primary designation or IAU name must match the data exactly, so if an NEO is mysteriously missing, double-check the spelling and capitalization.

### `query`

The `query` subcommand is more significantly more advanced - a `query` generates a collection of close approaches that match a set of specified filters, and either displays a limited set of those results to standard output or writes the structured results to a file.

```
$ python3 main.py query ...
```

### `interactive`

There's a third useful subcommand named `interactive`. This subcommand first loads the database and then starts a command loop so that you can repeatedly run `inspect` and `query` subcommands on the database without having to wait to reload the data each time you want to run a new command, which saves an extraordinary amount of time.

```
$ python3 main.py interactive ...
```

To remind yourself of the full interface, you can run `python3 main.py <subcommand> --help`:

## Development Environments

This project requires Python 3.6+. To see the version of your environment's Python 3, run `python3 -V` at the command line. You should see: `Python 3.X.Y` where X >= 6.

### Local Development
First, clone the project to your local machine, and then navigate to the project directory (the one containing `main.py`).

### Testing
Run ```python3 -m unittest``` to check if everything runs correctly.

```
$ python3 -m unittest
.........................................................................
----------------------------------------------------------------------
Ran 73 tests in 3.666s

OK
```

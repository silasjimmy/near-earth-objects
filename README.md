# Explore close approaches of Near Earth Objects (NEO)
A Python program to inspect Near Earth Objects (NEOs), a project provided by Udacity's Intermediate Python Nanodegree program.

## Getting started

### Installation
Clone the project to your local machine.

## Usage
This project is driven by the ```main.py``` script. That means that you'll run python3 main.py ... ... ... at the command line to invoke the program that will call your code. To view available commands and how to use them, run:
```
python3 main.py --help
```

There are three subcommands: 

1. ```inspect``` -  inspects a single NEO, printing its details in a human-readable format.
2. ```query``` - generates a collection of close approaches that match a set of specified filters, and either displays a limited set of those results to standard output or writes the structured results to a file.
3. ```interactive``` - first loads the database and then starts a command loop so that you can repeatedly run inspect and query subcommands on the database without having to wait to reload the data each time you want to run a new command.

The ```help``` command is also available for use with the above subcommands.

### Testing
Run:
```
python3 -m unittest
```
to test if everything works correctly.
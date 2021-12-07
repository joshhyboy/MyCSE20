The JDM_Info class allows the user to play with different JDM cars. The user can add an infinite amount of cars and get any makes, models, or years when they want. The cars are identified by nicknames, so there may be two cars of identical make model and year. Nicknames cannot be identical and the program will not allow duplicate nicknames. The first time you enter a duplicate or blank name, the program will give the nickname "Bingo". After that, any blank names or duplicate names will result in the car not being added, an you will be taken back to the start of the shell. There are 5 makes and 2 models per make for a total of 10 car combos. The available makes and models are as follows:

Toyota:
-Supra
-AE86

Honda:
-NSX-R
-Civic

Acura:
-Integra
-RL

Nissan:
-Skyline
-240SX

Mazda:
-Miata
-RX-7

All of these are case-sensitive but typing in an incorrectly spelled make/model will not crash the program. Behaviors will be described per command below. Additionally, the only valid years for cars in the program are the years from 1990-1999.

The available commands can be printed via the "help" command, and will be printed upon opening the program.

Commands:

get_make
-Will ask the user for a car to get the make of, and will print the make if the nickname of an existing car is given

get_model
-Will ask the user for a car to get the model of, and will print the model if the nickname of an existing car is given

get_year
-Will ask the user for a car to get the year of, and will print the year if the nickname of an existing car is given

set_make
-Will ask the user for a car to set the make of, and if a valid make is given, the make will be changed. Next, the user will be asked for a new model, as their old model is no longer correct for the make. If the user enters "DEFAULT", then a random make will be assigned. If the user inputs a valid model for their new make, the program will successfully modify the model to the specified model. If the user makes a typo or enters an invalid model, the program will treat it as "DEFAULT" and notify the user that a random model was given.

set_model
-Will ask the user for a car to set the model of. If a valid model is given, the program will modify the model. Otherwise, the model will not be changed.

set_year
-Will ask the user for a car to set the year of. If a year between 1990 and 1999 is given, it will be changed to the specified year. Otherwise the year will not be changed.

quarter_mile
-Will ask the user for a car to run on the quarter mile. If the user provides the nickname of an existing car, the preset message for the make and model of that car will be printed, with random values for the time and top speed. Each car has a higher or lower range based loosely on real-world performance and Josh's personal bias.

add_car
-Will ask the user for a make, model, year, and nickname in that order. If an invalid make or nickname is given, no car will be added. If an invalid model or year is given, but a valid make and nickname is given, the program will give a random model for the make and the year 1995.

car_report
-This will ask the user for a nickname of a car. If a valid nickname is given, the string representation of that instance will be printed using the string magic method. Otherwise, an error message will be printed and the user will be taken back to the beginning of the shell

exit
-Exits the program by breaking the while loop.

help
-Prints available commands

To run the program, just run it through Powershell or CMD and you will be taken care of by the shell.

Author: Joshua Peterson
"""
Joshua Peterson
Teacher: Harik K
Assignment 10.1: Your Own Class

I did not use any online resources for this assignment.

"""

# Any global varIbles or imports here
import random # Import random for unique messaging when doing quarter mile

class JDMInfo():
    # First we define 3 helper functions for when we initialize the class

    # This class will verify that the model we give it is a valid model for the make
    def verify_model(self, other_model = None):
        # First we check if other_model was given a value. This means it was called outside of the object and the model under verification is not a class attribute 
        if other_model == None:
            # Iterate through the available models for the make of the currently relevant car
            for models in self.__available_cars[self.__make]:
                # If the model fits the current make of the car, return True so it may be used if we wish
                if self.__model == models:
                    return True
        else: # IF other_model was not given a value, we do the same thing but we are instead dealing with the class attribute. This is the case in __init__
            for models in self.__available_cars[self.__make]:
                if other_model == models:
                    return True
        # If we get trough everything and the model did not match any models, we return false
        return False 
    
    # This function works exactly the same as verify_model, but instead of iterating through the models of the makes, we just iterate through the makes in the available car dictionary
    def verify_make(self, other_make = None):
        if other_make == None:
            for makes in self.__available_cars.keys():
                if self.__make == makes:
                    return True
        else:
            for makes in self.__available_cars.keys():
                if other_make == makes:
                    return True
        return False 

    # This function is exactly like the last two but instead of iterating through the dictionary we iterate through the range of valid car years
    def verify_year(self,year):
        try:
            year = int(year) # Additionally, here we make sure we were not given a string
            for i in range(1990,2000):
                if year == i:
                    return True
            return False
        except ValueError:
            return False # If we were, we treat it as we would a year like 1665. We overwrite the value so we don't have to stop the program here

    def __init__(self, make=None, model=None, year=1995):

        # This is for user input. If year was left blank, we give it the default value of 1995
        if year == '' or str(year).split(' ') == '':
            year = 1995
        
        # Store init arguments as private attributes
        self.__make = make
        self.__model = model
        self.__year = year

        # Create a private attribute that contains the valid makes and models
        self.__available_cars = {
            "Toyota":["Supra", "AE86"],
            "Honda":["NSX-R", "Civic"],
            "Acura":["Integra", "RL"],
            "Nissan":["Skyline","240SX"],
            "Mazda":["Miata", "RX-7"]
        }
        # If no  valid make was given, we give it Honda by default so the program can continue
        if make == None or make.strip(' ') == '' or JDMInfo.verify_make(self) == False:
            print("You must pass in a valid car make argument. See README for more info. Default make given: Honda")
            self.__make = "Honda"

        # If no valid model was given, we give a random model in the list of models for the corresponding make
        if self.__model == None:
            self.__model = str(self.__available_cars[self.__make][random.randint(0,2)])

        # If a model was given but it is not part of the models for the corresponding make, we do the same as before
        elif JDMInfo.verify_model(self) == False:
            self.__model = str(self.__available_cars[self.__make][random.randint(0,2)])
        # Default year is 1995 in the case that the user doesn't give a valid type for year or a year is out of range
        if JDMInfo.verify_year(self=self, year=self.__year) == False:
            self.__year = 1995
    # This is used to give the default model for a new make, or to in general give the instance correct attributes.
    def re_init(self, instance):
        instance.__init__(self.__make,self.__model,self.__year)
    # The next methods are the required get_ methods
    def get_make(self):
        return(self.__make)

    def get_model(self):
        return(self.__model)
    
    def get_year(self):
        return(self.__year)
    # The next methods are the required set_ methods
    def set_make(self, new_make):
        if JDMInfo.verify_make(self,new_make) == True: # First we verify if the new make is valid
            self.__make = new_make # If it is we can modify the make and continue to new model
        else: # If it isn't we do nothing and let the user know that it didn't work
            print("Invalid make. Make has not been changed")

    def set_model(self, new_model):
        if JDMInfo.verify_model(self, new_model) == True: # First we verify if the model exists for the current make
            self.__model = new_model # If it is, we can set the model attribute
        else: # If it doesnt we set it to a randomly chosen model and notify user
            self.__model = self.__available_cars[self.__make][random.randint(0,2)]
            print("That car model is not valid for that make, model has been set to random model for corresponding make.")
            
    # Set year is the simplest, all the verification is done and we set it to the new year
    def set_year(self, new_year):
        if JDMInfo.verify_year(self, new_year) == True:
            self.__year = new_year
        else: # If it's wrong we let the user know where to find year guidelines
            print("Invalid year. See README for year guidelines")

    # This method is just simple and fun, we print a prewritten message based on the make and model of the car. This is the 'game' in the program
    def quarter_mile(self):
        make = self.__make
        model = self.__model
        year = self.__year
        # Each car has a range of speeds and times so that there is some variety. Most print the year if it grammatically fits
        if make == "Toyota" and model == "Supra":
            print(f"It's hot! This modded 1000WHP {year} Supra ran {random.randrange(7,10)} seconds quarter mile with a top speed of {random.randrange(160,175)} MPH!")
        elif make == "Toyota" and model == "AE86":
            print(f"Don't let the cute exterior fool you! This 450HP sleeper {year} AE86 gets a respectable {random.randrange(11,16)} second quarter mile with a top speed of {random.randrange(150,165)} MPH")
        elif make == "Honda" and model == "NSX-R":
            print(f"Rice cooker! {year} Honda NSX Type-R with aftermarket Twin Turbos drops a blazing {random.randrange(5,8)} second quarter mile with a top speed of {random.randrange(170, 185)} MPH!")
        elif make == "Honda" and model == "Civic":
            print(f"Loud and proud! This {year} Honda Civic has a Spoon engine putting out 560WHP, and laid down a surprising {random.randrange(8,11)} second quarter mile! Top speed: {random.randrange(150, 160)} MPH")
        elif make == "Acura" and model == "Integra":
            print(f"Rust bucket! This {year} Acura Integra has some work to do before it's a track star! With 230HP, this Integra ran a {random.randrange(14,17)} second quarter mile. Top speed: {random.randrange(120,135)}MPH")
        elif make == "Acura" and model == "RL":
            print(f"What's this sedan doing on the track? This {year} Acura RL ran a {random.randrange(13,16)} second quarter mile. Top speed: {random.randrange(130,140)}MPH")
        elif make == "Nissan" and model == "Skyline":
            print(f"The poster boy of JDM! This stunning {year} Nissan Skyline R32 ran a {random.randrange(9,12)} quarter mile. Top speed: {random.randrange(155,170)}MPH")
        elif make == "Nissan" and model == "240SX":
            print(f"The Skyline's cousin is nothing to sneeze at, with a {random.randrange(9,13)} on the quarter mile with a top speed of {random.randrange(145,160)}MPH")
        elif make == "Mazda" and model == "Miata":
            print(f"Cutie alert! This Miata only came for picture day, just look at the body kit! What's under the hood, no one knows but the driver. What we know is its blistering {random.randrange(10,12)} second quarter mile and top speed of {random.randrange(160,175)}MPH made the cute AE86 go home crying!")
        elif make == "Mazda" and model == "RX-7":
            print(f"Rambunctious Rotary! The gas-guzzling {year} Mazda RX-7 laid down a high-pitched {random.randrange(8,10)} seconds on the quarter mile with a top speed of {random.randrange(160,175)}MPH")

    # String magic method in case we need to print the attributes of the instance
    def __str__(self):
        return (f"Year: {self.__year}\nMake: {self.__make}\nModel: {self.__model}\n")


# This helper method assembles the nicknames from the car dictionary into a nice list for us to print to the user
def get_available_cars(cardict):
    final_str = ''
    for nickname in cardict.keys(): # Iterate only through the keys (names)
        final_str += str(nickname) + ", "
    return (final_str.strip(' ')).strip(',')

""" 
This helper function is what allows us to have infinite car instances

We utilize the nicknames given by the user as "variable names" so that we can use the same instance over and over with different attributes, stored inside the dictionary.
This is used several times throughout the program.

"""
def set_current_car(cardict, carname):
    # Create/re-initialize local variables and access the attributes we want to give from the dictionary
    current_make = cardict[carname]["Make"]
    current_model = cardict[carname]["Model"]
    current_year = cardict[carname]["Year"]    
    # Re-Create the instance using the same variable container, with the attributes from the dictionary
    current_car = JDMInfo(make=current_make,model=current_model,year=current_year)
    return current_car # Return the instance
# Verify if the nickname is in the avaiable nicknames, returns boolean
def verify_name(cardict, carname):
    for names in cardict.keys():
        if carname == str(names):
            return True
    return False
# Main fucntion, create a shell for the user to create cars
def main():
    # Create string of available commands
    available = "Available commands: get_make, get_model, get_year, set_make, set_model, set_year, quarter_mile, add_car, car_report, exit"
    # So we can use zip() to create our dictionaries as the user adds cars
    key_list = ["Make", "Model", "Year"]
    renamed = False # This is used for the program to detect if default name "Bingo" has already been used
    # This is the dictionary that stores all the user-craeted cars, start off with just my own car :-)
    car_dict = {
        "Zippy": {
            "Make": "Honda",
            "Model": "Civic",
            "Year": 1995
        }
    }
    # Set the current car instance to the only car we have
    current_car = set_current_car(car_dict,"Zippy")
    # Welcome the user
    print("\nWelcome to the JDMInfo shell!\n")
    print(available)
    # Now we enter the loop
    while True:
        # Get command from the user
        command = input("Command for car?\n>")

        # Check for each command:

        if command == "add_car":
            # Create local variables and get necessary inputs
            temp_list = []
            temp = None
            make = input("Car Make?\n>")
            model = input("Car Model?\n>")
            year = input("Year?\n>")
            nick = input("A Nickname for your car?\n>")
            # Make sure valid nickname was given
            if nick == '' and renamed == False:
                print("Aww come on?? No name? Good choice letting me name it.")
                nick = "Bingo"
                renamed = True # Set renamed to true so we don't make 2 Bingos
            elif nick == '' and renamed == True:
                print("You've used your free name, I'm only giving you one. No car added")
                continue # Next iteration pls
            if verify_name(car_dict,nick) == True: # Checks for duplicate names
                print(f"Name '{nick}' is taken. No car was added")
                continue
            # We create a list to correspond to our key list, so we can store this new car in the dictionary
            temp_list += [make]
            temp_list += [model]
            temp_list += [year]
            # The dictionary's key is the nickname given by the user, and the value is another dictionary containing the make, model, and year as key/value pairs
            car_dict[nick] = dict(zip(key_list, temp_list))

        elif command == "get_make":
            # What car does the user want to know the make of?
            car_name = input(f"Which car? Available cars: {get_available_cars(car_dict)}\n>")
            # Verify that name is valid
            if verify_name(car_dict, car_name) == True: # IF it is, create the car instance with the nickname and use the get_make method to get the private attribute
                current_car = set_current_car(car_dict,car_name)
                print(f"\n{car_name} is a {current_car.get_make()}\n")
            else: # Otherwise let the user know they done messed up, and go to next iteration
                print("That name does not match currently created cars. Please enter a valid name.")
                continue

        elif command == "get_model": # Exactly the same as get_make
            car_name = input(f"Which car? Available cars: {get_available_cars(car_dict)}\n>")
            
            if verify_name(car_dict, car_name) == True:
                current_car = set_current_car(car_dict,car_name)
                print(f"\n{car_name} is a {current_car.get_model()}\n")
            else:
                print("That name does not match currently created cars. Please enter a valid name.")
                continue

        elif command == "get_year": # Same as last two
            car_name = input(f"Which car? Available cars: {get_available_cars(car_dict)}\n>")
            
            if verify_name(car_dict, car_name) == True:
                current_car = set_current_car(car_dict,car_name)
                print(f"\n{car_name} was made in {current_car.get_year()}\n")
            else:
                print("That name does not match currently created cars. Please enter a valid name.")
                continue

        # Here's a funky one
        elif command == "set_make":
            # Get the car nickname. Should've made this a helper function.
            car_name = input(f"Which car? Available cars: {get_available_cars(car_dict)}\n>")

            # This maybe could've been a helper function too.
            if verify_name(car_dict, car_name) == True:
                current_car = set_current_car(car_dict,car_name)
            else:
                print("That name does not match currently created cars. Please enter a valid name.")
                continue
            # Now get the make that the user wants
            new_make = input("What make would you like to change your car to?\n>")
            if current_car.verify_make(new_make) == True: # If it's a valid make we now have to change the model
                new_model = input("You now must change the model, enter a new module or type DEFAULT and you will be given a random model for your make\n>")

                if new_model == "DEFAULT" or current_car.verify_model(new_model) == False: # If no valid model was given or user wants default, give random model for the car
                    current_car.set_make(new_make)
                    current_car.re_init(instance=current_car) # Re-init allows the object's __init__ to properly assign a new model

                    print(f"{car_name} is now a {current_car.get_year()} {current_car.get_make()} {current_car.get_model()}.")
                else: # Otherwise, the model is valid and we can assign it to the car
                    current_car.set_make(new_make)
                    current_car.set_model(new_model)

                    print(f"{car_name} is now a {current_car.get_year()} {current_car.get_make()} {current_car.get_model()}.")
            else: # If a completely invalid make is given, we do nothing and change nothing
                print(f"{car_name} was not changed.")
            # Here we update the dictionary so that between object creations the attributes are not static.
            del car_dict[car_name] # First we delete the key/value pair for the nickname
            # Then we utilize the zip function to zip "Make" to current_car.get_make(), etc. 
            # Since we have the nickname stored as the user's input, and the latest attributes are stored in the object instance currently, we can delete and remake the dictionary value
            car_dict[car_name] = dict(zip([
                "Make", "Model", "Year"
            ],[
                current_car.get_make(), current_car.get_model(), current_car.get_year()
            ]))
        
        # This functions very similarly to the last function
        elif command == "set_model":
            # First we get the car name from the user
            car_name = input(f"Which car? Available cars: {get_available_cars(car_dict)}\n>")
            # Verify that the name is valid before continuing
            if verify_name(car_dict, car_name) == True:
                current_car = set_current_car(car_dict,car_name)
            else:
                print("That name does not match currently created cars. Please enter a valid name.")
                continue

            # Now we get the desired new model of the car
            new_model = input(f"What model would you like to change {car_name} to?\n>")
            if current_car.verify_model(new_model) == True: # Verify the model
                current_car.set_model(new_model)
                print(f"{car_name} is now a {current_car.get_year()} {current_car.get_make()} {current_car.get_model()}.")
            else: # If invalid, print that nothing was changed and go on to next iteration
                print(f"{car_name} was not changed. Please give a valid model")
                continue

            # Update dict
            del car_dict[car_name]
            car_dict[car_name] = dict(zip([
                "Make", "Model", "Year"
            ],[
                current_car.get_make(), current_car.get_model(), current_car.get_year()
            ]))

        # Works same as last two
        elif command == "set_year":
            # Get car name from user
            car_name = input(f"Which car? Available cars: {get_available_cars(car_dict)}\n>")

            if verify_name(car_dict, car_name) == True: # Verify name
                current_car = set_current_car(car_dict,car_name)
            else:
                print("That name does not match currently created cars. Please enter a valid name.")
                continue
            
            # Get new year from user
            new_year = input(f"What year would you like to change {car_name} to?\n>")
            if current_car.verify_year(new_year) == True: # Verify year
                current_car.set_year(new_year)
                print(f"{car_name} is now a {current_car.get_year()} {current_car.get_make()} {current_car.get_model()}.")
            else:
                print(f"{car_name} was not changed")

            # Update dictionary
            del car_dict[car_name]
            car_dict[car_name] = dict(zip([
                "Make", "Model", "Year"
            ],[
                current_car.get_make(), current_car.get_model(), current_car.get_year()
            ]))

        # This one is very simple, just a fun one for the kids
        elif command == "quarter_mile":
            # Get the car name in a sillier way
            car_name = input(f"Which car's burnin rubber tonight? Available cars: {get_available_cars(car_dict)}\n>")

            if verify_name(car_dict, car_name) == True: # Verify the name (in a wacky manner)
                current_car = set_current_car(car_dict,car_name)
            else:
                print("That name does not match currently created cars. Please enter a valid name.")
                continue
            # Just call the quarter mile function, and the message will print
            current_car.quarter_mile()

        # This one just prints the string representation of the desired car
        elif command == "car_report":
            car_name = input(f"Which car? Available cars: {get_available_cars(car_dict)}\n>")

            if verify_name(car_dict,car_name) == True: # Verify
                current_car = set_current_car(car_dict,car_name)
            else:
                print("That name does not match currently created cars. Please enter a valid name.")
                continue
            # We have a string magic method so this works out
            print(current_car)

        # Help me!
        elif command == "help":
            print(available)

        # All done
        elif command == "exit":
            break

# Call main
if __name__ == "__main__":
    main()
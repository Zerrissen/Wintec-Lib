'''
Author: Nathan Hines 21523561
Pledge of Honour: I pledge by honour that this program is solely my own work.
Description: Display a list of records
'''

import os
import csv
import numpy as np
from colorama import init, Fore

# Constants
ERROR = Fore.RED
OUT = Fore.YELLOW
RESET = Fore.RESET
INPUT_PRINTS = [f"{OUT}Enter Film ID: {RESET}", f"{OUT}Enter Movie Film Title: {RESET}", f"{OUT}Enter Film Budget (Mil): {RESET}", f"{OUT}Enter Film Box Office Rating: {RESET}"]
DEFAULT_LIST = np.array([['FM01', 'Stealth', 135, 80], ['FM02', 'Supernova', 90, 15], ['FM03', 'Robin Hood', 100, 85], ['FM04', 'Rollerball', 70, 26], ['FM05', 'Rust', 85, 20]])

# OS Dependant clear commands to clear the console, this means the program works with linux and macOS.
clearConsole = "clear"
if os.name in ('nt', 'dos'):
    clearConsole = "cls"

# Film Lists
newFilms = []

# Main menu, used to select the operation.
def main():
    os.system(clearConsole)
    print(f"{OUT}Welcome to Hines Film Database! How can we help?")
    print(f"\n\t1\tDisplay current film database")
    print(f"\t2\tAdd to current film database")
    print(f"\t3\tRemove from current film database")
    print(f"\t4\tExit Application")
    while True:
        try:
            value = int(input(f"\n{OUT}Enter your choice (1-4): {RESET}"))
        except ValueError:
            print(f"{ERROR}Error: input was not a valid choice. Try again.{RESET}")
            continue
        if value == 1:
            display()
            # Loop used to pause the menu until the user is ready to move on.
            while True:
                try:
                    input(f"\n{OUT}Press enter to clear and return to menu.{RESET}")
                except Exception as e:
                    print(f"{ERROR}Error: {RESET}{str(e)}")
                    continue
                os.system(clearConsole)
                break
            main()
        if value == 2:
            add()
            main()
        if value == 3:
            remove()
            # Loop used to pause the menu until the user is ready to move on.
            while True:
                try:
                    input(f"\n{OUT}Press enter to clear and return to menu.{RESET}")
                except Exception as e:
                    print(f"{ERROR}Error: {RESET}{str(e)}")
                    continue
                os.system(clearConsole)
                break
            main()
        if value == 4:
            print(f"{OUT}Saving database and closing program. Thank you!{RESET}")
            save(open_db())
            os._exit(0)

# Function to add entries to the film database.
def add():
    # Begin string inputs.
    stringInputsDone = [False, False]
    for i in range(len(INPUT_PRINTS) - 2):
        while sum(stringInputsDone) != len(stringInputsDone):
            if stringInputsDone[i] == False:
                try:
                    value = input(INPUT_PRINTS[i])
                except Exception as e:
                    print(f"Error: {str(e)}")
                    continue
                while True:
                    try:
                        ask = input(f"{OUT}Do you wish to add this value to the current film? (y/n): {RESET}").lower().strip()
                    except Exception as e:
                        print(f"{ERROR}Error: {str(e)}{RESET}")
                        continue
                    if ask == "y":
                        newFilms.append(value)
                        print
                        stringInputsDone[i] = True
                        break
                    if ask == "n":
                        break
            else:
                break

    # Begin integer inputs - done in a seperate loop to catch errors more efficiently using ValueError.
    intInputsDone = [False, False]
    for i in range(len(INPUT_PRINTS) - 2):
        while sum(intInputsDone) != len (intInputsDone):
            if intInputsDone[i] == False:
                try:
                    value = int(input(INPUT_PRINTS[i + 2]))
                except ValueError:
                    print(f"{ERROR}Error: input was not a valid number. Try again.{RESET}")
                while True:
                    try:
                        ask = input(f"{OUT}Do you wish to add this value to the current film? (y/n): {RESET}").lower().strip()
                    except Exception as e:
                        print(f"Error: {str(e)}{RESET}")
                        continue
                    if ask == "y":
                        newFilms.append(value)
                        intInputsDone[i] = True
                        break
                    if ask == "n":
                        break
                    else:
                        print(f"{ERROR}Error: Unknown input. Try again.{RESET}")
                        continue
            else:
                break

    # Add the new entry to the database.
    A = np.row_stack([open_db(), newFilms])
    filmList = A
    save(filmList)
    display()

    # Ask user if they want to continue adding films.
    while True:
        try:
            value = input(f"\n{OUT}Continue adding? (y/n){RESET}").lower().strip()
        except Exception as e:
            print(f"{ERROR}Error: {str(e)}{RESET}")
            continue
        if value == "y":
            add()
        elif value == "n":
            break
        else:
            print(f"{ERROR}Error: Unknown input. Exiting to menu.{RESET}")
            break

# Function to display the film database.
def display():
    filmID, movieTitle, movieBudget, boxRating = "Film ID", "Movie Title", "Movie Budget", "Box Office Rating"
    print(f"\n{RESET}{filmID:<10}{movieTitle:<15} {movieBudget:<15} {boxRating}")    
    print("-----------------------------------------------------------")
    for film in open_db():
        print(f"{film[0]:<15}{film[1]:<15} {film[2]:<15} {film[3]}{RESET}")

# Function to remove entries from the film database.
def remove():
    # Display current database.
    display()
    while True:
        try:
            # Use filmID as a "primary key" of sorts to identify films.
            idToRemove = input(f"\n{OUT}Please enter the Film ID of the film you wish to remove: {RESET}").strip()
        except Exception as e:
            print(f"{ERROR}Error: {str(e)}{RESET}")
            continue
        while True:
            try:
                # Check the user actually wants to remove the item.
                value = input(f"{OUT}Are you sure you want to remove item \'{RESET}{idToRemove}{OUT}\' from the database? (y/n): ").lower().strip()
            except Exception as e:
                print(f"{ERROR}Error: {str(e)}{RESET}")
                continue
            if value == "y":
                # Checks that the ID exists
                if any(idToRemove in i for i in open_db()[:,0]):
                    # Delete the entry and create the updated list.
                    A = np.delete(open_db(), np.where(open_db() == value)[0], axis=0)
                    filmList = A
                    save(filmList)
                    break
                else:
                    print(f"{ERROR}Error: Item not in list. Try again.{RESET}")
                    break
            elif value == "n":
                break
            else:
                print(f"{ERROR}Error: Unknown input. Exiting to menu.{RESET}")
                break
        break
    
    # Ask to continue removing or return to menu.
    while True:
            try:
                value = input(f"\n{OUT}Continue removing? (y/n){RESET}").lower().strip()
            except Exception as e:
                print(f"{ERROR}Error: {str(e)}{RESET}")
                continue
            if value == "y":
                remove()
            elif value == "n":
                break
            else:
                print(f"{ERROR}Error: Unknown input. Exiting to menu.{RESET}")
                break

# Read the database and return it as a 2d array to be used in program.
def open_db():
    with open("filmDB.csv", 'r', newline='') as filmDB:
        csvReader = csv.reader(filmDB)
        filmList = np.array(list(csvReader))
        return filmList

# Save filmList to a file for long term storage.
def save(filmList):
    open_db()
    with open("filmDB.csv", "w+", newline='') as filmDB:
        csvWriter = csv.writer(filmDB, delimiter=",")
        csvWriter.writerows(filmList)

# Driver code in the event that the program is run as a module.
if __name__ == '__main__':

    # Create DB using default films if not already created.
    if os.path.exists("filmDB.csv"):
        pass
    else:
        print(f"{OUT}Initializing database with default films...")
        with open("filmDB.csv", 'w+', newline='') as filmDB:
            csvWriter = csv.writer(filmDB, delimiter=",")
            csvWriter.writerows(DEFAULT_LIST)
        print(f"\n{OUT}Complete! Please re-run the display function.")

    # Initiates filmList.
    with open("filmDB.csv", 'r', newline='') as filmDB:
        csvReader = csv.reader(filmDB)
        filmList = np.array(list(csvReader))
    
    init()
    main()
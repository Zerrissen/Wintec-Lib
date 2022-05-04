'''
Author: Nathan Hines 21523561
Pledge of Honour: I pledge by honour that this program is solely my own work.
Description: Display a list of records and allow some added functionality
'''

import numpy as np
import pandas as pd
import csv
import os
import platform
import gc
from colorama import init, Fore
from time import sleep

# Module used to test memory usage
import psutil
not_my_data = set(dir()) # Stores built-in variables

# Constants
ERROR = Fore.RED
INP = Fore.YELLOW
RESET = Fore.RESET
GOOD = Fore.GREEN
TITLE = Fore.MAGENTA
HASH = f"{RESET}[{INP}#{RESET}] "
MINUS = f"{RESET}[{ERROR}-{RESET}] "
PLUS = f"{RESET}[{GOOD}+{RESET}] "

DEFAULT_LIST = pd.DataFrame([['FM01','Stealth', 135, 80], ['FM02','Supernova', 90, 15], ['FM03','Robin Hood', 100, 85], ['FM04','Rollerball', 70, 26], ['FM05','Rust', 85, 20]], columns=['Film ID', 'Film Name', 'Film Budget', 'Box Office Rating'])

def run_checks_and_start():
    # Check for operating system and use dependant commands.
    if platform.system() == 'Windows':
        clearConsole = 'cls'
    else:
        clearConsole = 'clear'
    # Check if database already exists. If not, create one.
    if os.path.exists('filmDB.csv'):
        pass
    else:
        generate_default('active')
    if os.path.exists('filmDB_archive.csv'):
        pass
    else:
        generate_default('archive')
    # Begin main function, and pass console command while we're at it.
    main_menu(clearConsole)

# Main menu, allows access to other functions.
def main_menu(*args):
    clearConsole = str(args).replace("'", "")
    clearConsole = clearConsole.replace(",", "")
    os.system(str(clearConsole))
    print(f'''{TITLE}
██╗  ██╗██╗███╗   ██╗███████╗███████╗    ██████╗ ██████╗ 
██║  ██║██║████╗  ██║██╔════╝██╔════╝    ██╔══██╗██╔══██╗
███████║██║██╔██╗ ██║█████╗  ███████╗    ██║  ██║██████╔╝
██╔══██║██║██║╚██╗██║██╔══╝  ╚════██║    ██║  ██║██╔══██╗
██║  ██║██║██║ ╚████║███████╗███████║    ██████╔╝██████╔╝
╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝    ╚═════╝ ╚═════╝ \n{RESET}''')
    print(f"Welcome to Hines Film Database! How can we help?")
    print(f"\n\t1\tDisplay current film database")
    print(f"\t2\tSearch for an item in the film database")
    print(f"\t3\tAdd to current film database")
    print(f"\t4\tRemove from current film database")
    print(f"\t5\tRestore from archive database")
    print(f"\t6\tExit Application")
    while True:
        try:
            value = int(input(f"\n{HASH}Enter your choice (1-6): "))
        except ValueError:
            print(f"{MINUS}{ERROR}Error: input was not a valid choice. Try again.{RESET}")
            continue
        if value == 1:
            display()
            pause()
            del value; gc.collect() # gc.collect() calls the python garbage collector. Always called alongside del keyword.
            break
        if value == 2:
            search()
            pause()
            del value; gc.collect()
            break
        if value == 3:
            add_item()
            pause()
            del value; gc.collect()
            break
        if value == 4:
            remove_item()
            pause()
            del value; gc.collect()
            break
        if value == 5:
            restore_item()
            pause()
            del value; gc.collect()
            break
        if value == 6:
            print(f"\n{HASH}Saving database and closing program...")
            save('full')
            print(f"{HASH}Closing program.")
            del value; gc.collect()
            sleep(2)
            # Exit program
            os._exit(0)
    main_menu(clearConsole)

# Function to display the film database with formatted output.
def display(*arg):
    if len(arg) == 0:
        titleColumn, budgetColumn, boxOfficeColumn = read_database('active').columns
        print(f'\n{"Film ID":<10}{titleColumn:<15}{budgetColumn:<15}{boxOfficeColumn}')
        print('---------------------------------------------------------')
        for (filmID, title, budget, boxOffice) in read_database('active').itertuples(index=True):
            print(f'{filmID:<10}{title:<15}{budget:<15}{boxOffice}')
        print('')
    elif arg[0] == 'archive':
        titleColumn, budgetColumn, boxOfficeColumn = read_database('archive').columns
        print(f'\n{"Film ID":<10}{titleColumn:<15}{budgetColumn:<15}{boxOfficeColumn}')
        print('---------------------------------------------------------')
        for (filmID, title, budget, boxOffice) in read_database('archive').itertuples(index=True):
            print(f'{filmID:<10}{title:<15}{budget:<15}{boxOffice}')
        print('')
    
    del titleColumn, budgetColumn, boxOfficeColumn, title, budget, boxOffice, filmID, arg; gc.collect()

# Function to search for a row using the index.
def search():
    while True:
        # Get item to search
        try:
            value = input(f"{HASH}Enter the ID of the film you wish to search: ").upper().strip()
        except Exception as e:
            print(f"{MINUS}{ERROR}Error: "+str(e)+f"{RESET}")
            del e; gc.collect()
            continue
        try:
            # Display searched item
            titleColumn, budgetColumn, boxOfficeColumn = read_database('active').columns
            print(f'\n{"Film ID":<10}{titleColumn:<15}{budgetColumn:<15}{boxOfficeColumn}')
            print('---------------------------------------------------------')
            for (filmID, title, budget, boxOffice) in read_database('active').loc[[value]].itertuples(index=True):
                print(f'{filmID:<10}{title:<15}{budget:<15}{boxOffice}')
        except KeyError:
            print(f"{MINUS}{ERROR}Error: Item not in list. Try again.{RESET}")
            continue
        break

    del value, titleColumn, budgetColumn, boxOfficeColumn, title, budget, boxOffice, filmID; gc.collect()

# Function to add an item to the database.
def add_item():
    # Generate new ID and append it to a list for usage as Film ID
    newItems = [gen_new_film_id()]
    inputPrints = list(read_database('active').columns.values.tolist())
    inputsDone = [False, False, False]
    # Error catching input loop
    for i in range(len(inputPrints)):
        while sum(inputsDone) != len(inputsDone):
            if inputsDone[i] == False:
                try:
                    if i == 0:
                        value = input(f"{HASH}Please enter the value for \'" + inputPrints[i]+ "\': ")
                    elif i == 1:
                        value = int(input(f"{HASH}Please enter the value for \'" + inputPrints[i]+ "\': "))
                        if value < 0:
                            print(f"{MINUS}{ERROR}Error: \'{RESET}"+inputPrints[i]+f"{ERROR}\' Cannot be less than 0. Try again{RESET}")
                            continue
                    elif i == 2:
                        value = int(input(f"{HASH}Please enter the value for \'" + inputPrints[i]+ "\': "))
                        if value > 100:
                            print(f"{MINUS}{ERROR}Error: \'{RESET}"+inputPrints[i]+f"{ERROR}\' Cannot be greater than 100. Try again{RESET}")
                            continue
                        elif value < 0:
                            print(f"{MINUS}{ERROR}Error: \'{RESET}"+inputPrints[i]+f"{ERROR}\' Cannot be less than 0. Try again{RESET}")
                            continue
                except Exception as e:
                    if e.__class__.__name__ == "ValueError":
                        print(f"{MINUS}{ERROR}Error: \'{RESET}"+str(value)+f"{ERROR}\' is not a valid number. Try again{RESET}")
                        del e; gc.collect()
                        continue
                    else:
                        print(f"{MINUS}{ERROR}Error: "+str(e)+f"{RESET}")
                        del e; gc.collect()
                        continue
                newItems.append(value)
                inputsDone[i] = True
                break
            else:
                break
    save('add', list(newItems))
    print(f"\n{PLUS}Item Added!")
    sort_items()

    del newItems, inputPrints, inputsDone, value, i; gc.collect()

# Function to generate and return a new ID based on the largest known index.
def gen_new_film_id():
    # Get databases and merge the FilmID columns.
    df1 = read_database('active')
    df2 = read_database('archive')

    df1 = df1.reset_index()
    df2 = df2.reset_index()

    df1 = np.array(df1)
    df2 = np.array(df2)
    mergedList = np.concatenate((df1[:,0], df2[:,0]))

    # Iterate through list and store the ID numbers only.
    for i in range(len(mergedList)):
        numFilter = filter(str.isdigit, mergedList[i])
        numString = "".join(numFilter)
        mergedList[i] = int(numString)
    
    # Get the highest number and +1 to it, giving a new ID.
    newID = np.amax(mergedList) + 1
    newID = f'FM{newID:02d}'


    del df1, df2, mergedList, numFilter, numString, i; gc.collect()

    return newID

# Function that allows the user to archive any single entry.
def remove_item():
    display()
    while True:
        try:
            idToRemove = input(f"{HASH}Enter the ID of the film you wish to archive\n{HASH}Leave blank to cancel.\n{HASH}Film to remove: ").upper().strip()
        except Exception as e:
            print(f"{MINUS}{ERROR}Error: "+str(e)+f"{RESET}")
            del e; gc.collect()
            continue
        if idToRemove == "":
            break
        else:
            df1 = read_database('active')
            df1 = df1.reset_index()
            df1 = df1.values
            if any (idToRemove in i for i in df1[:,0]):
                while True:
                    try:
                        value = input(f"{HASH}Are you sure you want to archive the film with ID {idToRemove}? (y/n): ").lower().strip()
                    except Exception as e:
                        print(f"{MINUS}{ERROR}Error: "+str(e)+f"{RESET}")
                        del e; gc.collect()
                        continue
                    if value == "y":
                        # Read the database and convert it to a numpy array for manipulation
                        # Save the entry to the archive
                        itemToArchive = np.copy(df1[np.where(df1 == idToRemove)[0]])
                        # Convert back to dataframe
                        itemToArchive = pd.DataFrame(itemToArchive, columns=['Film ID', 'Film Name', 'Film Budget', 'Box Office Rating'])
                        itemToArchive = itemToArchive.set_index(['Film ID'])
                        save('archive', itemToArchive)
                        # Remove the entry from the database and save.
                        df1 = np.delete(df1, np.where(df1 == idToRemove)[0], axis=0)
                        save('full', df1, 'full')
                        print(f"\n{MINUS}Item removed!")
                        break
                    else:
                        break
                del value, itemToArchive, df1; gc.collect()
                break
            else:
                print(f"{MINUS}{ERROR}\nError: Item does not exist. Try again.{RESET}\n")
                del df1, idToRemove; gc.collect()
                continue

    sort_items()
    del idToRemove; gc.collect()

# Function to reverse the archive.
def restore_item():
    display('archive')
    while True:
        try:
            idToRemove = input(f"{HASH}Enter the ID of the film you wish to restore: ").upper().strip()
        except Exception as e:
            print(f"{MINUS}{ERROR}Error: "+str(e)+f"{RESET}")
            del e; gc.collect()
            continue
        while True:
            try:
                value = input(f"{HASH}Are you sure you want to restore the film with ID {idToRemove}? (y/n): ").lower().strip()
            except Exception as e:
                print(f"{MINUS}{ERROR}Error: "+str(e)+f"{RESET}")
                del e; gc.collect()
                continue
            if value == "y":
                # Read the database and convert it to a numpy array for manipulation
                df1 = read_database('archive')
                df1 = df1.reset_index()
                df1 = df1.values
                if any(idToRemove in i for i in df1[:,0]):
                    # Save the entry to the active
                    itemToArchive = np.copy(df1[np.where(df1 == idToRemove)[0]])
                    # Convert back to dataframe
                    itemToArchive = pd.DataFrame(itemToArchive, columns=['Film ID', 'Film Name', 'Film Budget', 'Box Office Rating'])
                    itemToArchive = itemToArchive.set_index(['Film ID'])
                    save('active', itemToArchive)
                    # Remove the entry from the archive and save.
                    df1 = np.delete(df1, np.where(df1 == idToRemove)[0], axis=0)
                    save('full', df1, 'archive')
                    print(f"\n{PLUS}Item restored!")
                    del itemToArchive, df1; gc.collect()
                    break
            else:
                break
        break
    
    sort_items()
    del idToRemove, value; gc.collect()

# Function to generate default database for first program running or database deletion.
def generate_default(*arg):
    if arg[0] == 'active':
        print(f"{HASH}Film Database File not found. Generating default...")
        DEFAULT_LIST.to_csv('filmDB.csv', index=False, header=True, mode='w+')
        print(f"{PLUS}Film Database File generated!\n")
        sleep(1)
    elif arg[0] == 'archive':
        print(f"{HASH}Film Database Archive File not found. Generating default...")
        headers = ["Film ID", "Film Name", "Film Budget", "Box Office Rating"]
        with open('filmDB_archive.csv', 'a') as filmDBArchive:
            csvWriter = csv.writer(filmDBArchive)
            csvWriter.writerow(headers)
        print(f"{PLUS}Film Database Archive File generated!\n")
        del headers, filmDBArchive, csvWriter; gc.collect()
        sleep(1)
    del arg; gc.collect()

# Function to open the database and return its current structure, used during database modification and reading.
def read_database(*args):
    if args[0] == 'active':
        filmList = pd.read_csv('filmDB.csv', header=0, index_col=0)
    elif args[0] == 'archive':
        filmList = pd.read_csv('filmDB_archive.csv', header=0, index_col=0)
    
    del args; gc.collect()
    return filmList

# Function to sort items by their Film ID.
def sort_items():
    df1 = read_database('active')
    df2 = read_database('archive')
    df1 = df1.sort_index()
    df2 = df2.sort_index()
    df1 = df1.reset_index()
    df2 = df2.reset_index()
    df1 = df1.values
    df2 = df2.values
    save('full', df1, 'full')
    save('full', df2, 'archive')

    del df1, df2; gc.collect()

# Function to save whatever dataframe is parsed.
def save(*args):
    # If wanting a full save
    if args[0] == 'full':
        # Check if data has been parsed. If not, then re-write the current active database.
        if len(args) == 3:
            if args[2] == 'full':
                if os.path.exists('filmDB.csv'):
                    newItems = pd.DataFrame(list(args[1]), columns=["Film ID", "Film Name", "Film Budget", "Box Office Rating"])
                    newItems.to_csv('filmDB.csv', index=False, header=True, mode='w')
                    del newItems; gc.collect()
                else:
                    print(f"{MINUS}{ERROR}Error: \'{RESET}filmDB.csv{ERROR}\' not found. Closing without saving.")
            elif args[2] == 'archive':
                if os.path.exists('filmDB_archive.csv'):
                    restoredItems = pd.DataFrame(list(args[1]), columns=["Film ID", "Film Name", "Film Budget", "Box Office Rating"])
                    restoredItems.to_csv('filmDB_archive.csv', index=False, header=True, mode='w')
                    del restoredItems; gc.collect()
                else:
                    print(f"{MINUS}{ERROR}Error: \'{RESET}filmDB_archive.csv{ERROR}\' not found. Closing without saving.")
        else:
            if os.path.exists('filmDB.csv'):
                read_database('active').to_csv('filmDB.csv', index=True, header=True, mode='w')
                print(f"{PLUS}Database saved!")
            else:
                print(f"{MINUS}{ERROR}Error: \'{RESET}filmDB.csv{ERROR}\' not found. Closing without saving.")
            if os.path.exists('filmDB_archive.csv'):
                read_database('archive').to_csv('filmDB_archive.csv', index=True, header=True, mode='w')
                print(f"{PLUS}Archive saved!")
            else:
                print(f"{MINUS}{ERROR}Error: \'{RESET}filmDB_archive.csv{ERROR}\' not found. Closing without saving.")

    # If wanting to add a new item
    elif args[0] == 'add':
        if os.path.exists('filmDB.csv'):
            newItems = list(args[1])
            with open("filmDB.csv", "a", newline='\n') as filmDB:
                csvWriter = csv.writer(filmDB)
                csvWriter.writerow(newItems)
            del newItems, csvWriter, filmDB; gc.collect()
        else:
            print(f"{MINUS}{ERROR}Error: \'{RESET}filmDB.csv{ERROR}\' not found. Closing without saving.")

    # If wanting to archive an item
    elif args[0] == 'archive':
        if os.path.exists('filmDB_archive.csv'):
            itemsToArchive = pd.DataFrame(args[1], columns=["Film Name", "Film Budget", "Box Office Rating"])
            itemsToArchive = itemsToArchive.reset_index()
            itemsToArchive.to_csv('filmDB_archive.csv', index=False, header=False, mode='a')
            del itemsToArchive; gc.collect()
        else:
            print(f"{MINUS}{ERROR}Error: \'{RESET}filmDB_archive.csv{ERROR}\' not found. Closing without saving.")

    # If wanting to restore an item
    elif args[0] == 'active':
        if os.path.exists('filmDB.csv'):
            itemsToArchive = pd.DataFrame(args[1], columns=["Film Name", "Film Budget", "Box Office Rating"])
            itemsToArchive = itemsToArchive.reset_index()
            itemsToArchive.to_csv('filmDB.csv', index=False, header=False, mode='a')    
            del itemsToArchive; gc.collect()
        else:
            print(f"{MINUS}{ERROR}Error: \'{RESET}filmDB.csv{ERROR}\' not found. Closing without saving.")

    del args; gc.collect()

# Function used to wait for user input to return from their current activity and return to the menu.
def pause():
    while True:
        try:
            input(f"\n{HASH}Press enter to clear and return to menu.")
        except Exception as e:
            print(f"{MINUS}{ERROR}Error: "+str(e)+f"{RESET}")
            del e; gc.collect()
            continue
        break


# Driver code in the event program is run as a module.
if __name__ == '__main__':
    init()
    run_checks_and_start()
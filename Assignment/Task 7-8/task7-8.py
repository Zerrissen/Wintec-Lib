'''
Author: Nathan Hines 21523561
Pledge of Honour: I pledge by honour that this program is solely my own work.
Description: Display a list of records and allow some added functionality
'''

# Attempt to import modules and throw error if they aren't installed.
try:
    import numpy as np
    import pandas as pd
    import csv
    import os
    import platform
    import sys
    from getpass import getpass
    from colorama import init, Fore, Style
    from time import sleep
except ModuleNotFoundError as e:
    print(e)
    print('Run \'python3 -m pip install -r requirements.txt\' to install all required modules.')
    exit() # use the python built-in method of exiting as sys hasn't been imported here. Messy exit but works.

# Custom exceptions
class LessThanZeroError(Exception):
    pass
class ArgumentTooBigError(Exception):
    pass

# Constants
BRIGHT = Style.BRIGHT
RESET = Fore.RESET + Style.RESET_ALL
BLUE = Fore.BLUE + Style.BRIGHT
RED = Fore.RED
YEL = Fore.YELLOW
GREEN = Fore.GREEN
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
TITLE = f'''{Fore.MAGENTA}
██╗  ██╗██╗███╗   ██╗███████╗███████╗    ██████╗ ██████╗
██║  ██║██║████╗  ██║██╔════╝██╔════╝    ██╔══██╗██╔══██╗
███████║██║██╔██╗ ██║█████╗  ███████╗    ██║  ██║██████╔╝
██╔══██║██║██║╚██╗██║██╔══╝  ╚════██║    ██║  ██║██╔══██╗
██║  ██║██║██║ ╚████║███████╗███████║    ██████╔╝██████╔╝
╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝    ╚═════╝ ╚═════╝\n{RESET}'''
HASH = f'{RESET}[{YEL}#{RESET}] '
MINUS = f'{RESET}[{RED}-{RESET}] '
ERROR = f'{RESET}[{RED}!{RESET}] '
PLUS = f'{RESET}[{GREEN}+{RESET}] '
DEFAULT_LIST = pd.DataFrame([['FM01','Stealth', 135, 80], ['FM02','Supernova', 90, 15], ['FM03','Robin Hood', 100, 85], ['FM04','Rollerball', 70, 26], ['FM05','Rust', 85, 20]], columns=['Film ID', 'Film Name', 'Film Budget', 'Box Office Rating'])

# Main menu, allows access to other functions.
def main_menu():
    try:
        os.system(clearConsole)
        print(TITLE)
        print(f'Welcome to Hines Film Database! How can we help?')
        print(f'\n\t[{BLUE}1{RESET}]\tDisplay current film database')
        print(f'\t[{BLUE}2{RESET}]\tSearch for an item in the film database')
        print(f'\t[{BLUE}3{RESET}]\tAdd to current film database')
        print(f'\t[{BLUE}4{RESET}]\tRemove from current film database')
        print(f'\t[{BLUE}5{RESET}]\tRestore from archive database')
        print(f'\t[{BLUE}6{RESET}]\tDisplay help and program info')
        print(f'\t[{BLUE}99{RESET}]\tExit Application')
        while True:
            try:
                value = input(f'\n{HASH}Enter your choice (1-99): {BRIGHT}')
                if len(value) > 2 and value.isnumeric():
                    raise ArgumentTooBigError
                # Implicitly convert value, otherwise except statement ignores creation of value.
                value = int(value)
            except ArgumentTooBigError:
                print(f'{ERROR}{RED}Error: \'{RESET}{value}{RED}\' has too many characters. Try again.{RESET}')
                continue
            except ValueError:
                if value == '':
                    pause()
                    break
                else:
                    print(f'{MINUS}{RED}Error: \'{RESET}{value}{RED}\' is invalid input. Try again.{RESET}')
                    continue
            if value == 1:
                # Other functions have the 'clearConsole' command and 'TITLE' print built-in.
                # Display is called in other functions, hence implicit use.
                os.system(str(clearConsole))
                print(TITLE)
                print(f'{HASH}Database Display selected!')
                display()
                pause()
                break
            elif value == 2:
                search_for_film()
                pause()
                break
            elif value == 3:
                add_item()
                pause()
                break
            elif value == 4:
                remove_item()
                pause()
                break
            elif value == 5:
                restore_item()
                pause()
                break
            elif value == 6:
                help_and_info()
                pause()
                break
            # '99' is used here so that the user has to give intent to exit, following Nielsen's 10 Heuristics.
            elif value == 99:
                print(f'\n{HASH}Saving database and closing program...')
                save('full')
                print(f'{HASH}Closing program.')
                sleep(2)
                # Exit program
                sys.exit(0)
            # Fallback 'else' in event input is a valid integer but not valid choice.
            else:
                raise ValueError
        # Restart function outside of while loop
        main_menu()

    # Catch keyboard interrupt (ctrl+c) at any stage in the program, and exit cleanly without lots of traceback messages.
    except KeyboardInterrupt:
        print(f'\n{ERROR}{RED}Error: Keyboard Interrupt detected. Shutting down.')

# Function to display the film database with formatted output.
def display(*arg):
    # Display the active database.
    if len(arg) == 0:
        titleColumn, budgetColumn, boxOfficeColumn = read_database('active').columns
        print(f"\n{RESET}{'Film ID':<10}{titleColumn:<15}{budgetColumn:<15}{boxOfficeColumn}")
        print('---------------------------------------------------------')
        for (filmID, title, budget, boxOffice) in read_database('active').itertuples(index=True):
            print(f'{filmID:<10}{title:<15}{budget:<15}{boxOffice}')
        # Decide whether difference is a profit or a loss.
        if get_budget_loss('active') < 0:
            print('\nTotal Profit: $' + str(abs(get_budget_loss('active'))) + 'M\n')
        else:
            print('\nTotal budget loss: $' + str(get_budget_loss('active')) + 'M\n')
    # Display the archive database.
    elif arg[0] == 'archive':
        titleColumn, budgetColumn, boxOfficeColumn = read_database('archive').columns
        print(f"\n{RESET}{'Film ID':<10}{titleColumn:<15}{budgetColumn:<15}{boxOfficeColumn}")
        print('---------------------------------------------------------')
        for (filmID, title, budget, boxOffice) in read_database('archive').itertuples(index=True):
            print(f'{filmID:<10}{title:<15}{budget:<15}{boxOffice}')
        # Decide whether difference is a profit or a loss.
        if get_budget_loss('archive') < 0:
            print('\nTotal Profit: $' + str(abs(get_budget_loss('archive'))) + 'M\n')
        else:
            print('\nTotal budget loss: $' + str(get_budget_loss('archive')) + 'M\n')

# Function to search for a row using the index.
def search_for_film():
    os.system(str(clearConsole))
    print(TITLE)
    print(f'{HASH}Search Database selected!\n')
    while True:
        # Flags used to check whether the search value is an ID or a film name.
        isID = False
        foundByName = False
        total = 0
        # Get item to search
        try:
            value = input(f'{HASH}Enter the ID or Film Name you wish to search\n{HASH}Leave blank to cancel.\n{HASH}Search Value (ID format FMxx): {BRIGHT}').upper().strip()
        except Exception as e:
            print(f'{ERROR}{RED}Error: '+str(e)+f'{RESET}')
            continue
        # Check if value is blank and cancel search if it is.
        if value == '':
            break
        else:
            try:
                # Check whether the search is a valid ID or not.
                isID = value in read_database('active').index
                # If not a valid ID, start searching by name. Will KeyError if not a valid name either.
                filmByName = read_database('active')['Film Name'].str.contains(value, regex=False, case=False)
                filmByName = filmByName[filmByName].index.values
                if len(filmByName) == 0:
                    raise KeyError
                else:
                    foundByName = True

                # Get and print columns and seperator
                titleColumn, budgetColumn, boxOfficeColumn = read_database('active').columns
                print(f'\n{RESET}{"Film ID":<10}{titleColumn:<15}{budgetColumn:<15}{boxOfficeColumn}')
                print('---------------------------------------------------------')
                # If found by both ID and name
                if isID == True and foundByName == True:
                    # Make sure that the film name isn't the same as it's own ID! otherwise it might print both....
                    if not value in filmByName:
                        # Print all the ID found films first
                        for (filmID, title, budget, boxOffice) in read_database('active').loc[[value]].itertuples(index=True):
                            print(f'{filmID:<10}{title:<15}{budget:<15}{boxOffice}')
                        # Print all the name found films second
                        for i in range(len(filmByName)):
                            for (filmID, title, budget, boxOffice) in read_database('active').loc[[filmByName[i]]].itertuples(index=True):
                                print(f'{filmID:<10}{title:<15}{budget:<15}{boxOffice}')
                        # Update the total budget loss/profit
                        for i in range(len(filmByName)):
                            total += get_budget_loss('search', filmByName[i])
                        total += get_budget_loss('search', value)
                        # If this isn't a loss, but actually a profit
                        if total < 0:
                            print('\nTotal Proft: $' + str(abs(total)) + 'M\n')
                        else:
                            print('\nTotal budget loss: $' + str(total)+'M\n')

                    # if BOTH the ID and the name ARE the same, then only print one of them
                    else:
                        for (filmID, title, budget, boxOffice) in read_database('active').loc[[value]].itertuples(index=True):
                            print(f'{filmID:<10}{title:<15}{budget:<15}{boxOffice}')
                        if get_budget_loss('search', value) < 0:
                            print('\nFilm Proft: $' + str(abs(get_budget_loss('search', value))) + 'M\n')
                        else:
                            print('\nFilm budget loss: $' + str(get_budget_loss('search', value))+'M\n')

                # If only found by ID
                elif isID == True and foundByName == False:
                    for (filmID, title, budget, boxOffice) in read_database('active').loc[[value]].itertuples(index=True):
                        print(f'{filmID:<10}{title:<15}{budget:<15}{boxOffice}')
                        if get_budget_loss('search', value) < 0:
                            print('\nFilm Proft: $' + str(abs(get_budget_loss('search', value))) + 'M\n')
                        else:
                            print('\nFilm budget loss: $' + str(get_budget_loss('search', value))+'M\n')

                # If only found by name
                else:
                    for i in range(len(filmByName)):
                        for (filmID, title, budget, boxOffice) in read_database('active').loc[[filmByName[i]]].itertuples(index=True):
                            print(f'{filmID:<10}{title:<15}{budget:<15}{boxOffice}')
                    for i in range(len(filmByName)):
                        total += get_budget_loss('search', filmByName[i])
                    if total < 0:
                        print('\nTotal Proft: $' + str(abs(total)) + 'M\n')
                    else:
                        print('\nTotal budget loss: $' + str(total)+'M\n')

            except KeyError:
                print(f'\n{ERROR}{RED}Error: Item not in database. Try again.{RESET}\n')
                continue
            break

# Function to add an item to the database.
def add_item():
    os.system(clearConsole)
    print(TITLE)
    print(f'{HASH}Add New Film selected!')
    # Generate new ID and append it to a list for usage as Film ID
    newItems = [gen_new_film_id()]
    inputPrints = list(read_database('active').columns.values.tolist())
    inputsDone = [False, False, False]
    # Error catching input loop
    for i in range(len(inputPrints)):
        while sum(inputsDone) != len(inputsDone):
            # Check if we've already gotten a valid input here
            if inputsDone[i]:
                break
            # If we don't have a valid input yet, go ahead and ask for it!
            try:
                if i == 0:
                    value = input(f'{HASH}Please enter the value for \'' + inputPrints[i]+ f'\': {BRIGHT}')
                elif i == 1:
                    value = int(input(f'{HASH}Please enter the value for \'' + inputPrints[i]+ f'\': {BRIGHT}'))
                    if value < 0:
                        raise LessThanZeroError
                elif i == 2:
                    value = int(input(f'{HASH}Please enter the value for \'' + inputPrints[i]+ f'\':{BRIGHT} '))
                    if value < 0:
                        raise LessThanZeroError
            except LessThanZeroError:
                print(f'{ERROR}{RED}Error: \'{RESET}'+inputPrints[i]+f'{RED}\' Cannot be less than 0. Try again{RESET}')
                continue
            except ValueError:
                print(f'{ERROR}{RED}Error: \'{RESET}'+str(value)+f'{RED}\' is not a valid number. Try again{RESET}')
                continue
            newItems.append(value)
            inputsDone[i] = True
            break  # Doesn't require 'else' statement. Can implicitly break here.
    save('add', list(newItems))
    print(f'\n{PLUS}Item Added!')
    sort_items()

# Function to generate and return a new ID based on the largest known index.
def gen_new_film_id(*args):
    # If the currentID.txt file is missing, merge databases and create a new one (slow but necessary)
    if any(args):
        print(f'{HASH}ID File not found. Generating a new one... THIS MAY TAKE TIME DEPENDING ON DB SIZE')
        # Get databases and merge the FilmID columns.
        dataframe1 = read_database('active')
        dataframe2 = read_database('archive')

        dataframe1 = dataframe1.reset_index()
        dataframe2 = dataframe2.reset_index()

        dataframe1 = np.array(dataframe1)
        dataframe2 = np.array(dataframe2)
        mergedList = np.concatenate((dataframe1[:,0], dataframe2[:,0]))

        # Iterate through list and store the ID numbers only.
        for i in range(len(mergedList)):
            numFilter = filter(str.isdigit, mergedList[i])
            numString = ''.join(numFilter)
            mergedList[i] = int(numString)

        # Get the highest number and +1 to it, giving a new ID.
        currentID = np.amax(mergedList)
        try:
            with open('currentID.txt', 'w') as file:
                file.write(str(currentID))
        except FileNotFoundError:
            print(f'{ERROR}{RED}Error: File not found. Restart program to generate a new one.')
        except OSError:
            print(f'{ERROR}{RED}Error: Encountered unknown error when attempting to read file.')

        print(f'{PLUS}ID File generated!\n')
        sleep(1)

    # If the currentID.txt file is available, just use this! WAY faster during program use!
    else:
        try:
            with open('currentID.txt', 'r') as file:
                data = file.read()
        except FileNotFoundError:
            print(f'{ERROR}{RED}Error: File not found. Restart program to generate a new one.')
        except PermissionError:
            print(f'{ERROR}{RED}Error: Insufficient permission to read file.')
        except OSError:
            print(f'{ERROR}{RED}Error: Encountered unknown error when attempting to read file.')

        # Get the highest number and +1 to it, giving a new ID.
        newID = int(data) + 1
        try:
            with open('currentID.txt', 'w') as file:
                file.write(str(newID))
            newID = f'FM{newID:02d}'
        except PermissionError:
            print(f'{ERROR}{RED}Error: Insufficient permission to write file.')
        except OSError:
            print(f'{ERROR}{RED}Error: Encountered unknown error when attempting to read file.')
        return newID

# Function that allows the user to archive any single entry.
def remove_item():
    itemFound = False
    while True:
        os.system(clearConsole)
        print(TITLE)
        print(f'{HASH}Film Removal selected!')
        display()
        # Get an ID and throw an exception if there's an unexpected error
        try:
            idToRemove = input(f'{HASH}Enter the ID of the film you wish to archive\n{HASH}Leave blank to cancel.\n{HASH}Film to remove (Format FMxx): {BRIGHT}').upper().strip()
        except Exception as e:
            print(f'{ERROR}{RED}Error: '+str(e)+f'{RESET}')
            continue
        # If idToRemove is blank then break, otherwise continue
        if idToRemove == '':
            break
        dataframe1 = read_database('active')
        dataframe1 = dataframe1.reset_index()
        dataframe1 = dataframe1.values
        try:
            for i in dataframe1[:,0]:
                if i == idToRemove:
                    itemFound = True
                    while True:
                        try:
                            value = input(f'{HASH}Are you sure you want to archive the film with ID {idToRemove}? (y/n): {BRIGHT}').lower().strip()
                        except Exception as e:
                            print(f'{ERROR}{RED}Error: '+str(e)+f'{RESET}')
                            continue
                        if value == 'y':
                            # Read the database and convert it to a numpy array for manipulation
                            # Save the entry to the archive
                            itemToArchive = np.copy(dataframe1[np.where(dataframe1 == idToRemove)[0]])
                            # Convert back to dataframe
                            itemToArchive = pd.DataFrame(itemToArchive, columns=['Film ID', 'Film Name', 'Film Budget', 'Box Office Rating'])
                            itemToArchive = itemToArchive.set_index(['Film ID'])
                            save('archive', itemToArchive)
                            # Remove the entry from the database and save.
                            dataframe1 = np.delete(dataframe1, np.where(dataframe1 == idToRemove)[0], axis=0)
                            save('full', dataframe1, 'full')
                            print(f'\n{MINUS}Item removed!')
                            break
                        break  # Doesn't require 'else' statement. Can implicitly break here.
            if itemFound == False:
                raise KeyError
        except KeyError:
            print(f'\n{ERROR}{RED}Error: Item \'{RESET}{idToRemove}{RED}\' does not exist. Try again.{RESET}\n')
            sleep(2)
            continue
        break
    sort_items()

# Function to reverse the archive.
def restore_item():
    os.system(clearConsole)
    print(TITLE)
    print(f'{HASH}Film Restoration selected!')
    display('archive')
    while True:
        try:
            idToRemove = input(f'{HASH}Enter the ID of the film you wish to restore\n{HASH}Leave blank to cancel\n{HASH}ID to restore (format FMxx): {BRIGHT}').upper().strip()
        except Exception as e:
            print(f'{ERROR}{RED}Error: '+str(e)+f'{RESET}')
            continue
        if idToRemove == '':
            break
        while True:
            try:
                value = input(f'{HASH}Are you sure you want to restore the film with ID {idToRemove}? (y/n): {BRIGHT}').lower().strip()
            except Exception as e:
                print(f'{ERROR}{RED}Error: '+str(e)+f'{RESET}')
                continue
            if value == 'y':
                # Read the database and convert it to a numpy array for manipulation
                dataframe1 = read_database('archive')
                dataframe1 = dataframe1.reset_index()
                dataframe1 = dataframe1.values
                if any(idToRemove in i for i in dataframe1[:,0]):
                    # Save the entry to the active
                    itemToArchive = np.copy(dataframe1[np.where(dataframe1 == idToRemove)[0]])
                    # Convert back to dataframe
                    itemToArchive = pd.DataFrame(itemToArchive, columns=['Film ID', 'Film Name', 'Film Budget', 'Box Office Rating'])
                    itemToArchive = itemToArchive.set_index(['Film ID'])
                    save('active', itemToArchive)
                    # Remove the entry from the archive and save.
                    dataframe1 = np.delete(dataframe1, np.where(dataframe1 == idToRemove)[0], axis=0)
                    save('full', dataframe1, 'archive')
                    print(f'\n{PLUS}Item restored!')

                    break
            else:
                break
        break

    sort_items()

# Function that displays information and help.
def help_and_info():
    os.system(clearConsole)
    print(TITLE)
    print(f'{HASH} Help and Info selected!')
    print('\n! About Info !')
    print('This program was developed by Wintec student Nathan Hines.\nThe program is a proof of concept for file I/O and csv database management.')
    print(f'All my programs are stored privately on my GitHub until submission.')
    print(f'\n! Help !')
    print('Just follow any prompts and give input where directed to operate this program.')
    print('You may exit the program at any stage by using the shortuct \'Ctrl+C\'.\nBe aware that this will not save the database on exit, but will be much quicker.')
    print('\nThe program is designed in such a way that all records are NOT permanently deleted,\nrather they are archived in the archive file.')
    print('Unless you edit the files themselves, you will not lose any added records\nas per good database management!')
    print('\n! Links !')
    print(f'GitHub: {CYAN}https://github.com/zerrissen/{RESET}\nEmail: {CYAN}nathin18@student.wintec.ac.nz{RESET}')

# Function to generate default database for first program running or database deletion.
def generate_default(*arg):
    if arg[0] == 'active':
        try:
            print(f'{HASH}Film Database File not found. Generating default...')
            DEFAULT_LIST.to_csv('filmDB.csv', index=False, header=True, mode='w+')
        except PermissionError:
            print(f'{ERROR}{RED}Error: Insufficient permissions to write file.')
        except OSError:
            print(f'{ERROR}{RED}Error: Unknown error when attempting to access file.')
        print(f'{PLUS}Film Database File generated!\n')
        sleep(1)

    elif arg[0] == 'archive':
        print(f'{HASH}Film Database Archive File not found. Generating default...')
        headers = ['Film ID', 'Film Name', 'Film Budget', 'Box Office Rating']
        try:
            with open('filmDB_archive.csv', 'w') as filmDBArchive:
                csvWriter = csv.writer(filmDBArchive)
                csvWriter.writerow(headers)
        except PermissionError:
            print(f'{ERROR}{RED}Error: Insufficient permissions to write file.')
        except OSError:
            print(f'{ERROR}{RED}Error: Unknown error when attempting to access file.')
        print(f'{PLUS}Film Database Archive File generated!\n')
        sleep(1)

# Function to open the database and return its current structure, used during database modification and reading.
def read_database(*args):
    try:
        if args[0] == 'active':
            filmList = pd.read_csv('filmDB.csv', header=0, index_col=0)
        elif args[0] == 'archive':
            filmList = pd.read_csv('filmDB_archive.csv', header=0, index_col=0)
    except FileNotFoundError:
        print(f'{ERROR}{RED}Error: File not found. Restart program to generate a new one.')
    except PermissionError:
            print(f'{ERROR}{RED}Error: Insufficient permissions to write to file.')

    return filmList

# Function to sort items by their Film ID.
def sort_items():
    dataframe1 = read_database('active')
    dataframe2 = read_database('archive')
    dataframe1 = dataframe1.sort_index()
    dataframe2 = dataframe2.sort_index()
    dataframe1 = dataframe1.reset_index()
    dataframe2 = dataframe2.reset_index()
    dataframe1 = dataframe1.values
    dataframe2 = dataframe2.values
    save('full', dataframe1, 'full')
    save('full', dataframe2, 'archive')

# Function to get budgets, box office ratings, and budget loss of films.
def get_budget_loss(*args):
    if args[0] == 'active':
        totalBudget = read_database('active')['Film Budget'].sum()
        totalBoxOffice = read_database('active')['Box Office Rating'].sum()
        totalBudgetLoss = totalBudget - totalBoxOffice
        return totalBudgetLoss

    elif args[0] == 'archive':
        totalBudget = read_database('archive')['Film Budget'].sum()
        totalBoxOffice = read_database('archive')['Box Office Rating'].sum()
        totalBudgetLoss = totalBudget - totalBoxOffice
        return totalBudgetLoss

    elif args[0] == 'search':
        value = args[1]
        filmBudget = read_database('active')['Film Budget'].loc[[value]].sum()
        filmBoxOffice = read_database('active')['Box Office Rating'].loc[[value]].sum()
        filmBudgetLoss = filmBudget - filmBoxOffice
        return filmBudgetLoss
    else:
        print(f'{ERROR}{RED}Error: Invalid parameters parsed.{RESET}')

# Function to save whatever dataframe is parsed.
def save(*args):
    # If wanting a full save
    if args[0] == 'full':
        # Check if data has been parsed. If not, then re-write the current active database.
        if len(args) == 3:
            if args[2] == 'full':
                try:
                    if os.path.exists('filmDB.csv'):
                        newItems = pd.DataFrame(list(args[1]), columns=['Film ID', 'Film Name', 'Film Budget', 'Box Office Rating'])
                        newItems.to_csv('filmDB.csv', index=False, header=True, mode='w')
                    else:
                        raise FileNotFoundError
                except FileNotFoundError:
                    print(f'{ERROR}{RED}Error: \'{RESET}filmDB.csv{RED}\' not found. Closing without saving.')
                except PermissionError:
                    print(f'{ERROR}{RED}Error: Insufficient permissions to write to file.')
                except OSError:
                    print(f'{ERROR}{RED}Error: Unknown error when attempting to write to file.')
            elif args[2] == 'archive':
                try:
                    if os.path.exists('filmDB_archive.csv'):
                        restoredItems = pd.DataFrame(list(args[1]), columns=['Film ID', 'Film Name', 'Film Budget', 'Box Office Rating'])
                        restoredItems.to_csv('filmDB_archive.csv', index=False, header=True, mode='w')
                    else:
                        raise FileNotFoundError
                except FileNotFoundError:
                    print(f'{ERROR}{RED}Error: \'{RESET}filmDB_archive.csv{RED}\' not found. Closing without saving.')
                except PermissionError:
                    print(f'{ERROR}{RED}Error: Insufficient permissions to write to file.')
        else:
            try:
                if os.path.exists('filmDB.csv'):
                    read_database('active').to_csv('filmDB.csv', index=True, header=True, mode='w')
                    print(f'{PLUS}Database saved!')
                else:
                    raise FileNotFoundError
            except FileNotFoundError:
                print(f'{ERROR}{RED}Error: \'{RESET}filmDB.csv{RED}\' not found. Closing without saving.')
            except PermissionError:
                print(f'{ERROR}{RED}Error: Insufficient permissions to write to file.')
            try:
                if os.path.exists('filmDB_archive.csv'):
                    read_database('archive').to_csv('filmDB_archive.csv', index=True, header=True, mode='w')
                    print(f'{PLUS}Archive saved!')
                else:
                    raise FileNotFoundError
            except FileNotFoundError:
                print(f'{ERROR}{RED}Error: \'{RESET}filmDB_archive.csv{RED}\' not found. Closing without saving.')
            except PermissionError:
                print(f'{ERROR}{RED}Error: Insufficient permissions to write to file.')

    # If wanting to add a new item
    elif args[0] == 'add':
        try:
            if os.path.exists('filmDB.csv'):
                newItems = list(args[1])
                with open('filmDB.csv', 'a', newline='\n') as filmDB:
                    csvWriter = csv.writer(filmDB)
                    csvWriter.writerow(newItems)
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print(f'{ERROR}{RED}Error: \'{RESET}filmDB.csv{RED}\' not found. Closing without saving.')
        except PermissionError:
            print(f'{ERROR}{RED}Error: Insufficient permissions to write to file.')
        except OSError:
            print(f'{ERROR}{RED}Error: Unknown error when attempting to write to file.')

    # If wanting to archive an item
    elif args[0] == 'archive':
        try:
            if os.path.exists('filmDB_archive.csv'):
                itemsToArchive = pd.DataFrame(args[1], columns=['Film Name', 'Film Budget', 'Box Office Rating'])
                itemsToArchive = itemsToArchive.reset_index()
                itemsToArchive.to_csv('filmDB_archive.csv', index=False, header=False, mode='a')
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print(f'{ERROR}{RED}Error: \'{RESET}filmDB_archive.csv{RED}\' not found. Closing without saving.')
        except PermissionError:
            print(f'{ERROR}{RED}Error: Insufficient permissions to write to file.')

    # If wanting to restore an item
    elif args[0] == 'active':
        try:
            if os.path.exists('filmDB.csv'):
                itemsToArchive = pd.DataFrame(args[1], columns=['Film Name', 'Film Budget', 'Box Office Rating'])
                itemsToArchive = itemsToArchive.reset_index()
                itemsToArchive.to_csv('filmDB.csv', index=False, header=False, mode='a')
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print(f'{ERROR}{RED}Error: \'{RESET}filmDB.csv{RED}\' not found. Closing without saving.')
        except PermissionError:
            print(f'{ERROR}{RED}Error: Insufficient permissions to write to file.')

# Function used to wait for user input to return from their current activity and return to the menu.
def pause():
    while True:
        try:
            getpass(f'\n{HASH}Press enter to clear and return.')
        except Exception as e:
            print(f'{ERROR}{RED}Error: '+str(e)+f'{RESET}')
            continue
        break

# Driver code in the event program is run as a module.
if __name__ == '__main__':
    init()

    # Check operating system and declare respective commands.
    if platform.system() == 'Windows':
        clearConsole = 'cls'
    else:
        clearConsole = 'clear'

    # Check if files already exist. If not, create them.
    if os.path.exists('filmDB.csv'):
        pass
    else:
        generate_default('active')
    if os.path.exists('filmDB_archive.csv'):
        pass
    else:
        generate_default('archive')
    if os.path.exists('currentID.txt'):
        pass
    else:
        gen_new_film_id('missing')

    # Begin main function.
    main_menu()
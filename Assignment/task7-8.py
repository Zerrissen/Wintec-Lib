'''
Author: Nathan Hines 21523561
Pledge of Honour: I pledge by honour that this program is solely my own work.
Description: Display a list of records and allow some functionality
'''

from re import M
import numpy as np
import pandas as pd
import csv
import os
import platform

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
    main(clearConsole)

# Main menu, allows access to other functions.
def main(*args):
    clearConsole = str(args).replace("'", "")
    os.system(str(clearConsole))
    print(f"Welcome to Hines Film Database! How can we help?")
    print(f"\n\t1\tDisplay current film database")
    print(f"\t2\tAdd to current film database")
    print(f"\t3\tRemove from current film database")
    print(f"\t4\tRestore from archive database")
    print(f"\t5\tExit Application")
    while True:
        try:
            value = int(input(f"\nEnter your choice (1-4): "))
        except ValueError:
            print(f"Error: input was not a valid choice. Try again.")
            continue
        if value == 1:
            display()
            pause()
            break
        if value == 2:
            add_item()
            pause()
            break
        if value == 3:
            remove_item()
            pause()
            break
        if value == 4:
            restore_item()
            pause()
            break
        if value == 5:
            print(f"Saving database and closing program. Thank you!")
            save('full')
            os._exit(0)
    main(clearConsole)

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

# Function to search for a row using the index.
def search():
    while True:
        # Get item to search
        try:
            value = input("Enter the ID of the film you wish to see: ").upper().strip()
        except Exception as e:
            print("Error: "+str(e))
            continue
        try:
            # Display searched item
            titleColumn, budgetColumn, boxOfficeColumn = read_database('active').columns
            print(f'{"Film ID":<10}{titleColumn:<15}{budgetColumn:<15}{boxOfficeColumn}')
            print('---------------------------------------------------------')
            for (filmID, title, budget, boxOffice) in read_database('active').loc[[value]].itertuples(index=True):
                print(f'{filmID:<10}{title:<15}{budget:<15}{boxOffice}')
        except KeyError:
            print("Error: Item not in list. Try again.")
            continue
        break

    del value

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
                        value = input("Please enter the value for \'" + inputPrints[i]+ "\': ")
                    else:
                        value = int(input("Please enter the value for \'" + inputPrints[i]+ "\': "))
                except Exception as e:
                    if e.__class__.__name__ == "ValueError":
                        print("Error: \'"+str(value)+"\' is not a valid number. Try again")
                        continue
                    else:
                        print(f"Error: {str(e)}")
                newItems.append(value)
                inputsDone[i] = True
                break
            else:
                break
    save('add', list(newItems))
    print("\nItem Added!")
    sort_items()
    # Delete variables from memory to improve performance.
    del newItems
    del inputPrints
    del inputsDone
    del value

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

    # Delete variables from memory to improve performance if the databases are large.
    del df1
    del df2
    del mergedList

    return newID

# Function that allows the user to archive any single entry.
def remove_item():
    display()
    while True:
        try:
            idToRemove = input("Enter the ID of the film you wish to archive: ").upper().strip()
        except Exception as e:
            print(f"Error: {str(e)}")
            continue
        while True:
            try:
                value = input(f"Are you sure you want to archive the film with ID {idToRemove}? (y/n): ").lower().strip()
            except Exception as e:
                print(f"Error: {str(e)}")
                continue
            if value == "y":
                # Read the database and convert it to a numpy array for manipulation
                df1 = read_database('active')
                df1 = df1.reset_index()
                df1 = df1.values
                if any(idToRemove in i for i in df1[:,0]):
                    # Save the entry to the archive
                    itemToArchive = np.copy(df1[np.where(df1 == idToRemove)[0]])
                    # Convert back to dataframe
                    itemToArchive = pd.DataFrame(itemToArchive, columns=['Film ID', 'Film Name', 'Film Budget', 'Box Office Rating'])
                    itemToArchive = itemToArchive.set_index(['Film ID'])
                    save('archive', itemToArchive)
                    # Remove the entry from the database and save.
                    df1 = np.delete(df1, np.where(df1 == idToRemove)[0], axis=0)
                    save('full', df1, 'full')
                    print("\nItem removed!")
                    del itemToArchive
                    del df1
                    break
            else:
                break
        break

    sort_items()
    # Delete variables from memory to improve performance whilst they are not being used.
    del idToRemove
    del value

# Function to reverse the archive
def restore_item():
    display('archive')
    while True:
        try:
            idToRemove = input("Enter the ID of the film you wish to restore: ").upper().strip()
        except Exception as e:
            print(f"Error: {str(e)}")
            continue
        while True:
            try:
                value = input(f"Are you sure you want to restore the film with ID {idToRemove}? (y/n): ").lower().strip()
            except Exception as e:
                print(f"Error: {str(e)}")
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
                    print("\nItem restored!")
                    del itemToArchive
                    del df1
                    break
            else:
                break
        break
    
    sort_items()
    # Delete variables from memory to improve performance whilst they are not being used.
    del idToRemove
    del value

# Function to generate default database for first program running or database deletion.
def generate_default(*arg):
    if arg[0] == 'active':
        DEFAULT_LIST.to_csv('filmDB.csv', index=False, header=True, mode='w+')
    elif arg[0] == 'archive':
        headers = ["Film ID", "Film Name", "Film Budget", "Box Office Rating"]
        with open('filmDB_archive.csv', 'a') as filmDBArchive:
            csvWriter = csv.writer(filmDBArchive)
            csvWriter.writerow(headers)

# Function to open the database and return its current structure, used during database modification and reading.
def read_database(*args):
    if args[0] == 'active':
        filmList = pd.read_csv('FilmDB.csv', header=0, index_col=0)
    elif args[0] == 'archive':
        filmList = pd.read_csv('FilmDB_archive.csv', header=0, index_col=0)
    return filmList

# Function to sort items by their Film ID
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

# Function to save whatever dataframe is parsed.
def save(*args):
    # If wanting a full save
    if args[0] == 'full':
        # Check if data has been parsed. If not, then re-write the current active database.
        if len(args) == 3:
            if args[2] == 'full':
                newItems = pd.DataFrame(list(args[1]), columns=["Film ID", "Film Name", "Film Budget", "Box Office Rating"])
                newItems.to_csv('filmDB.csv', index=False, header=True, mode='w')
                del newItems
            elif args[2] == 'archive':
                restoredItems = pd.DataFrame(list(args[1]), columns=["Film ID", "Film Name", "Film Budget", "Box Office Rating"])
                restoredItems.to_csv('filmDB_archive.csv', index=False, header=True, mode='w')
                del restoredItems
        else:
            read_database('active').to_csv('filmDB.csv', index=True, header=True, mode='w')
            read_database('archive').to_csv('filmDB_archive.csv', index=True, header=True, mode='w')

    # If wanting to add a new item
    elif args[0] == 'add':
        newItems = list(args[1])
        with open("filmDB.csv", "a", newline='\n') as filmDB:
            csvWriter = csv.writer(filmDB)
            csvWriter.writerow(newItems)
        del newItems

    # If wanting to archive an item
    elif args[0] == 'archive':
        itemsToArchive = pd.DataFrame(args[1], columns=["Film Name", "Film Budget", "Box Office Rating"])
        itemsToArchive = itemsToArchive.reset_index()
        itemsToArchive.to_csv('filmDB_archive.csv', index=False, header=False, mode='a')
        del itemsToArchive

    # If wanting to restore an item
    elif args[0] == 'active':
        itemsToArchive = pd.DataFrame(args[1], columns=["Film Name", "Film Budget", "Box Office Rating"])
        itemsToArchive = itemsToArchive.reset_index()
        itemsToArchive.to_csv('filmDB.csv', index=False, header=False, mode='a')
        del itemsToArchive

    del args

# Function used to wait for user input to return from their current activity and return to the menu.
def pause():
            while True:
                try:
                    input(f"\nPress enter to clear and return to menu.")
                except Exception as e:
                    print(f"Error: {str(e)}")
                    continue
                break
# Driver code in the event program is run as a module.
if __name__ == '__main__':
    run_checks_and_start()
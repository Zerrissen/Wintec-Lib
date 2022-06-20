'''
Author: Nathan Hines 21523561
Pledge of Honour: I pledge by honour that this program is solely my own work.
Description: Display a list of records
'''

# Main function that controls the calling of other functions
def main():
    filename = 'data.txt'
    print_records(read_data(filename))
    print(f'\nTotal Average Area: {get_average_area(read_data(filename))}\n')
    search_by_colour(read_data(filename))

# Function to read the file 'data.txt' and return contents as a list
def read_data(filename):
    data = []
    try:
        with open(filename) as file:
            for line in file.readlines():
                data.append(line.strip('\n').split(','))
            return data
    except Exception:
        print("Oops, something went wrong! I won't tell you what though because this is just a mock.")

# Function that allows the user to search for a record by colour
def search_by_colour(data):
    flag = False # Boolean used for a print statement in case no record is found
    try:
        colourToSearch = input("Enter a colour to search for: ")
    except Exception:
        print("Oops, something went wrong! I won't tell you what though because this is just a mock.")

    for i in range(len(data)):
        if data[i][2] == colourToSearch:
            found_rec = data[i]
            flag = True
    # If the record was found then complete calculations
    if flag == True:
        width = float(found_rec[0])
        length = float(found_rec[1])
        area = width * length
        perimeter = (width + length) * 2

        print(f'{found_rec[2]} rectangle found:')
        print(f'Area: {area:.1f}')
        print(f'Perimeter: {perimeter:.1f}')
    # Otherwise, print no record found
    else:
        print(f'No record for {colourToSearch} found.')

# Function that calculates and returns the average area of all rectangle records
def get_average_area(data):
    rectangleAreas = []
    for i in range(len(data)):
        rectangleAreas.append((float(data[i][0])) * float(data[i][1]))

    totalArea = sum(rectangleAreas) / len(data)
    return totalArea

# Function that prints all records in a neat format
def print_records(data):
    widthTitle, lengthTitle, colourTitle = "Width", "Length", "Colour"

    print(f"{widthTitle:<10}{lengthTitle:<10} {colourTitle}")
    print("--------------------------------")
    for record in data:
        print(f"{record[0]:<10} {record[1]:<10} {record[2]}")

# Driver code in the event the program is imported as a module
if __name__ == '__main__':
    main()
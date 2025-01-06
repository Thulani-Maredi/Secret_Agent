# program to read or write amount of rainfall
# mrdthu003
# 10/09/2024

import os

# Display menu
while True:
    # Show options
    print("1. Enter rainfall.")
    print("2. Read rainfall.")
    print("3. Quit.")
    
    # Get user option
    option = input("Select an option:\n")

    if option == '1':
        # Enter rainfall data
        city = input("Enter the city name:\n").strip().lower().replace(" ", "")
        
        # Validate year
        while True:
            year = input("Enter the year:\n")
            if year.isdigit() and len(year) == 4:
                break
            print("Sorry, that's not a valid value.")  # error message for invalid input
        
        # Collect monthly rainfall values
        months = []
        for i in range(12):
            while True:
                value = input("Enter a value for month number {}:\n".format(i + 1))
                try:
                    float(value)  # make sure it's a valid number
                    months.append(value)  # store the valid value
                    break
                except ValueError:
                    print("Sorry, that's not a valid value.")  # error message for invalid number
        
        # Save data to a file with format city_year.dat
        filename = "{}_{}.dat".format(city, year)
        with open(filename, 'w') as file:
            file.write("\n".join(months))  # write all months data into the file
        print("Wrote '{}'.".format(filename))  # confirmation message

    elif option == '2':
        # Read rainfall data
        city = input("Enter the city name:\n").strip().lower().replace(" ", "")
        
        # Validate year input
        while True:
            year = input("Enter the year:\n")
            if year.isdigit() and len(year) == 4:
                break
            print("Sorry, that's not a valid value.")  # error message for invalid input
        
        # Filename format city_year.dat
        filename = "{}_{}.dat".format(city, year)
        print("Reading '{}'...".format(filename))
        if not os.path.exists(filename):
            print("Sorry, file not found.")  # error if file doesn't exist
        else:
            with open(filename, 'r') as file:
                data = file.readlines()  # read all lines from file
            
            invalid_values = 0  # counter for invalid values
            valid_values = 0    # counter for valid values
            valid_sum = 0.0     # sum of valid rainfall values
            
            # Process each month's rainfall data
            for i, value in enumerate(data):
                value = value.strip()  # remove any extra spaces
                try:
                    rainfall = float(value)  # convert to float
                    valid_sum += rainfall  # add valid value to sum
                    valid_values += 1  # count valid value
                except ValueError:
                    print("Data for month {} is invalid: '{}'.".format(i, value))  # message for invalid value
                    invalid_values += 1  # count invalid value
            
            # Show results
            print("Invalid values: {}.".format(invalid_values))
            print("Valid values: {}.".format(valid_values))
            if valid_values > 0:
                print("Average of valid values: {:.2f}.".format(valid_sum / valid_values))  # calculate and show average
    
    elif option == '3':
        # Quit the program
        print("Okay, bye.")  # goodbye message
        break  # exit the loop
    
    else:
        print("Invalid option.")  # message for invalid menu option

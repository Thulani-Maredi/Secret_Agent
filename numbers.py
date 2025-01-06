# Fixing code to run properly
# mrdthu003
# 13 September 2024


num_list = []
# Repeat multiple times until user gets correct file name and print error message if not
while True:
    try:
        filename = input('Enter a filename: ') 
        file = open(filename, 'r')
        break # if file name correct break loop
    except IOError:
        print("Error: Problem opening the file. Please try again.") 
    except Exception as e:
        print('ERROR: Some unknown error occurred: {e}')
    


line = file.readline()
count = 0 # fixing the initial step to 0
while len(line) > 0:
    try: # check if there are non integer in file
        num = int(line)
        num_list.append(num)
        line = file.readline()
        count += 1
    except ValueError:
        print("ERROR: Value not integer found inside file. Skipping line")
        line = file.readline() # reads next line
file.close()

print('Read {} value'.format(count), end='')
if count != 1: # replace is not with !=
    print('s.')
else:
    print('.')

index = input("Enter an index (or '[q]uit' to exit): ")
while index.lower() != 'q': # fixes for both upper and lower cases
    try: # check if input is a digit else print error
        index = int(index)
        print('Num at position', index, 'is', num_list[index])
    except ValueError:
        print('ERROR: An integer value should be entered')
    except IndexError:
        print('ERROR: An integer value out of range')
    except Exception as e:
        print('ERROR: Some unknown error occurred: {e}')   
    index = input("Enter an index (or '[q]uit' to exit): ")
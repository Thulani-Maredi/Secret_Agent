# Program to collect information
# mrdthu003
# 09 August 2024

# Collect the necessary information in the raw data from BEGIN to END
def get_block(data):
    start = data.index('BEGIN')
    end = data.index('END')
    info = data[start:end+3]
    return info

# Collect the location by using indexing to locate where it will be and using slicing to collect
def location(block):
    start = block.index(',')
    end = block.index('END')
    location = block[start+7:end-1]
    location = location[::-1]
    return location.title()

# Collect temperature using index function and slicing then make it a float
def temperature(block):
    start = block.find('BEGIN')
    end = block.index('_')
    temp = block[start+6:end]
    temp = float(temp)
    return temp

# Collect the x coordinate using index function and slicing
def x_coordinate(block):
    start = block.find(':')
    end = block.index(',')
    x_co = block[start+1:end]
    return x_co

# Collect the y coordinate using index function and slicing
def y_coordinate(block):
    start = block.index(',')
    end =  block.find(' ', start)
    y_co = block[start+1:end]
    return y_co

# Collect the pressure using index function and slicing then make it a float
def pressure(block):
    start = block.index('_')
    end = block.index(':')
    pressure = block[start+1:end]
    pressure = float(pressure)
    return pressure

def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location: '+ location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()

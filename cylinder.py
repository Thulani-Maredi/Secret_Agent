# program to calculate the volume of a cylinder
# mrdthu003
# 09 august 2024


import math

# calculating the area of a circle by using a math fucntion
def circle_area(diameter):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area

# Calculating the volume of the cylinder using previous area function
def cylinder_volume(diameter, height):
    area = circle_area(diameter)
    volume =  area * height
    return volume

# Using main function to collect data and print all the information about the cylinder
def main():
    diameter = int(input('Enter diameter:\n'))
    height = int(input('Enter height:\n'))
    volume = cylinder_volume(diameter, height)
    print(f'The volume of the cylinder is {volume:.2f}')
    
if __name__=='__main__':
    main()

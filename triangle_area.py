#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: November 2019
# This calulates the area of a triangle
#  from another function


def areaTriangle(base, height):
    # This program calculates the area of a triangle from diffrent functions
    # process
    area = base * height / 2
    # output
    print("The area is", area)
    
    
def main():
    # This program calculates the area of a triangle from diffrent functions
    # prevents crashing
    while True:
        # input
        base_as_string = input("Enter the base of the triangle: ")
        height_as_string = input("Enter the height of the triangle: ")
        print()

        # process
        try:
            # converts string to int
            base_as_int = int(base_as_string)
            height_as_int = int(height_as_string)
            
            # calls areaTriangle function
            areaTriangle(base_as_int, height_as_int)

        # prevents crashing
        except ValueError:
            print("Invalid Input")
            print()
            continue

        # breaks out of loop
        else:
            break


if __name__ == "__main__":
    main()

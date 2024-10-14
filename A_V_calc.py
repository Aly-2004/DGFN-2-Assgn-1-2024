#A_V_calc.py

#By Alyousef Soliman 100883692
#This program is strictly my own work. Any material
#beyond course learning materials that is taken from
#the Web or other sources is properly cited, giving
#credit to the original author(s).


#Function to calculate the area of a rectangle
def area_rectangle(length, width):
    """
    Function to calculate the area of a rectangle.
    Formula: length * width
    Returns the area rounded to 1 decimal place.
    """
    return round(length * width, 1)

#Function to calculate the area of a circle
def area_circle(radius):
    """
    Function to calculate the area of a circle.
    Formula: pi * radius^2
    Returns the area rounded to 1 decimal place.
    """
    import math
    return round(math.pi * radius ** 2, 1)

#Function to calculate the volume of a cube
def volume_cube(side_length):
    """
    Function to calculate the volume of a cube.
    Formula: side_length^3
    Returns the volume rounded to 1 decimal place.
    """
    return round(side_length ** 3, 1)

#Function to calculate the volume of a cylinder
def volume_cylinder(radius, height):
    """
    Function to calculate the volume of a cylinder.
    Formula: pi * radius^2 * height
    Returns the volume rounded to 1 decimal place.
    """
    import math
    return round(math.pi * radius ** 2 * height, 1)

#Function to calculate the area of a triangle
def area_triangle(base, height):
    """
    Function to calculate the area of a triangle.
    Formula: (1/2) * base * height
    Returns the area rounded to 1 decimal place.
    """
    return round(0.5 * base * height, 1)

#Main function to handle the menu and user interaction
def main():
    simplified = False  #Default mode
    while(True):
        #Level 0: Main menu for quitting or toggling views
        print("\nA/V Calculator Menu")
        print("Enter Q/q to quit")
        print("Enter S/s to change to simplified view or D/d for default view")
        print("1. Calculate Area of Rectangle")
        print("2. Calculate Area of Circle")
        print("3. Calculate Volume of Cube")
        print("4. Calculate Volume of Cylinder")
        print("5. Calculate Area of Triangle")

        choice = input("Choose an option: ").lower()
        
        if(choice == 'q'):
            break
        elif(choice == 's'):
            simplified = True
            print("Simplified mode activated.")
            continue
        elif(choice == 'd'):
            simplified = False
            print("Default mode activated.")
            continue
        elif(choice not in ['1', '2', '3', '4', '5']):
            print("Invalid option. Please select again.")
            continue

        #Collect inputs based on the user's choice of calculation
        if(choice == '1'):  #Area of Rectangle
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            result = area_rectangle(length, width)
            if(simplified):
                print(f"{length} * {width} = {result} (length * width)")
            else:
                print(f"Area of rectangle: {result} m^2")

        elif(choice == '2'):  #Area of Circle
            radius = float(input("Enter radius: "))
            result = area_circle(radius)
            if(simplified):
                print(f"π * {radius}^2 = {result} (pi * radius^2)")
            else:
                print(f"Area of circle: {result} m^2")

        elif(choice == '3'):  #Volume of Cube
            side_length = float(input("Enter side length: "))
            result = volume_cube(side_length)
            if(simplified):
                print(f"{side_length}^3 = {result} (side^3)")
            else:
                print(f"Volume of cube: {result} m^3")

        elif(choice == '4'):  #Volume of Cylinder
            radius = float(input("Enter radius: "))
            height = float(input("Enter height: "))
            result = volume_cylinder(radius, height)
            if(simplified):
                print(f"π * {radius}^2 * {height} = {result} (pi * radius^2 * height)")
            else:
                print(f"Volume of cylinder: {result} m^3")

        elif(choice == '5'):  #Area of Triangle
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            result = area_triangle(base, height)
            if(simplified):
                print(f"0.5 * {base} * {height} = {result} (1/2 * base * height)")
            else:
                print(f"Area of triangle: {result} m^2")

if(__name__ == "__main__"):
    main()

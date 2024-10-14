#test_A_V_calc.py

#By Alyousef Soliman 100883692
#This program is strictly my own work. Any material
#beyond course learning materials that is taken from
#the Web or other sources is properly cited, giving
#credit to the original author(s).

#Import the A_V_calc.py functions
from A_V_calc import area_rectangle, area_circle, volume_cube, volume_cylinder, area_triangle

#PyTest test cases for the area_rectangle function
def test_area_rectangle():
    """
    Test cases for the area_rectangle function.
    Using different lengths and widths for the tests.
    """
    assert area_rectangle(5, 3) == 15.0  #Test case 1
    assert area_rectangle(7.5, 4.2) == 31.5  #Test case 2
    assert area_rectangle(0, 10) == 0.0  #Test case 3

#PyTest test cases for the area_circle function
def test_area_circle():
    """
    Test cases for the area_circle function.
    Using different radii for the tests.
    """
    assert area_circle(3) == 28.3  # Test case 1
    assert area_circle(5) == 78.5  # Test case 2
    assert area_circle(0) == 0.0  # Test case 3

#PyTest test cases for the volume_cube function
def test_volume_cube():
    """
    Test cases for the volume_cube function.
    Using different side lengths for the tests.
    """
    assert volume_cube(3) == 27.0  #Test case 1
    assert volume_cube(1.5) == 3.4  #Test case 2
    assert volume_cube(0) == 0.0  #Test case 3

#PyTest test cases for the volume_cylinder function
def test_volume_cylinder():
    """
    Test cases for the volume_cylinder function.
    Using different radius and height values for the tests.
    """
    assert volume_cylinder(2, 5) == 62.8  #Test case 1
    assert volume_cylinder(3, 10) == 282.7  #Test case 2
    assert volume_cylinder(0, 10) == 0.0  #Test case 3

#PyTest test cases for the area_triangle function
def test_area_triangle():
    """
    Test cases for the area_triangle function.
    Using different base and height values for the tests.
    """
    assert area_triangle(10, 5) == 25.0  #Test case 1
    assert area_triangle(6.5, 3.2) == 10.4  #Test case 2
    assert area_triangle(0, 5) == 0.0  #Test case 3

#Run the tests
if( __name__ == "__main__"):
    test_area_rectangle()
    test_area_circle()
    test_volume_cube()
    test_volume_cylinder()
    test_area_triangle()

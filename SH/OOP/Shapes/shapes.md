# Object-Oriented Programming: Shapes - C++

### Objective

Design a hierarchy of classes to represent different types of shapes. Implement a base class called `Shape` with the following pure virtual functions:

```
class Shape {
public:
    virtual double getArea() const = 0;
    virtual double getPerimeter() const = 0;
    virtual void display() const = 0;
};
```



### Class Details

Now, derive the following classes from `Shape`:

1. `Rectangle`: Represents rectangles. It should have member variables for width and height, and should implement the pure virtual functions to calculate area and perimeter accordingly.
2. `Circle`: Represents circles. It should have a member variable for radius, and should implement the pure virtual functions to calculate area and perimeter accordingly.
   1. Methods
      * getArea()
      * getPreimeter()
      * display()
3. `Triangle`: Represents triangles. It should have member variables for the lengths of its three sides, and should implement the pure virtual functions to calculate area and perimeter accordingly.
   1. Child Classes
      * Isoceles
      * Right Triangle

Write a C++ program to demonstrate the usage of these classes. Create objects of each class, set their dimensions, and display their properties.


**Rectangle**

Member variables:

* `width`: representing the width of the rectangle (integer)
* `height`: representing the height of the rectangle (integer)

Methods:

* `Rectangle()`: default constructor to initialize width and height to 0
* `Rectangle(int w, int h)`: parameterized constructor to initialize width and height with the given values
* `int getWidth()`: a method to get the width of the rectangle
* `int getHeight()`: a method to get the height of the rectangle
* `void setWidth(int w)`: a method to set the width of the rectangle
* `void setHeight(int h)`: a method to set the height of the rectangle
* `int getArea()`: a method to calculate and return the area of the rectangle
* `int getPerimeter()`: a method to calculate and return the perimeter of the rectangle
* `void display()`: a method to display the width, height, area, and perimeter of the rectangle


### Sample Output

```
Rectangle:
Width: 5
Height: 3
Area: 15
Perimeter: 16

Circle:
Radius: 4
Area: 50.2655
Perimeter: 25.1327

Triangle:
Side 1: 3
Side 2: 4
Side 3: 5
Area: 6
Perimeter: 12

```

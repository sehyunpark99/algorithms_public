#include <string>
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

class Shape {
public:
    Shape(int width, int height) : w(width), h(height) {}; // Constructor
    virtual double calc_area() = 0; // Pure Virtual Function
    string get_name() { return "Shape"; };

protected:
    double w;
    double h;
};

class Rectangle : public Shape {
public:
    Rectangle(int width, int height) : Shape(width, height) {}; // Constructor
    double calc_area() {
        return w * h;
    }
    string get_name() {
        return "Rectangle";
    }
};


class Square : public Rectangle {
public:
    Square(int width) : Rectangle(width, width) {}; // Constructor
    double calc_area() {
        return Rectangle::calc_area();
    }
    string get_name() {
        return "Square";
    }
};

class Triangle : public Shape {
public:
    Triangle(int side1, int side2, int side3) : a(side1), b(side2), c(side3), Shape(0, 0) {}; // Constructor

    virtual double calc_area() {
        if (a + b <= c || a + c <= b || b + c <= a)
            return -1;
        // Calculate the area using Heron's formula
        double s = (a + b + c) / 2;
        return sqrt(s * (s - a) * (s - b) * (s - c));
    }
    string get_name() {
        return "Triangle";
    }

protected:
    double a; // Side 1
    double b; // Side 2
    double c; // Side 3

};

class RightTriangle : public Triangle {
public:
    RightTriangle(int side1, int side2) : Triangle(side1, side2, sqrt(side1 * side1 + side2 * side2)) {};
    double calc_area() {
        if (a + b <= c || a + c <= b || b + c <= a) {
            return -1;
        }
        double sides[3] = { a, b, c };
        std::sort(sides, sides + 3);
        return 0.5 * sides[0] * sides[1];
    }
    string get_name() {
        return "Right Triangle";
    }
};


int main() {
    Rectangle rectangle(5, 3);
    Square square(4);
    Triangle triangle(3, 4, 5);
    RightTriangle rightTriangle(3, 4);

    std::cout << rectangle.get_name() << std::endl;
    std::cout << rectangle.calc_area() << std::endl;

    std::cout << square.get_name() << std::endl;
    std::cout << square.calc_area() << std::endl;

    std::cout << triangle.get_name() << std::endl;
    std::cout << triangle.calc_area() << std::endl;

    std::cout << rightTriangle.get_name() << std::endl;  // Output: RightTriangle
    std::cout << rightTriangle.calc_area() << std::endl;  // Output: 6
    std::cout << "\n";
    return 0;
};

#include <iostream>
#include <cmath>

class Shape {
public:
    virtual double getArea() const = 0;
    virtual double getPerimeter() const = 0;
    virtual void display() const = 0;
    virtual ~Shape() {}; // Destrcutor
};

class Rectangle : public Shape {
private:
    double width;
    double height;
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    double getArea() const override {
        return width * height;
    }
    double getPerimeter() const override {
        return 2 * (width + height);
    }
    void display() const override {
        std::cout << "Rectangle:\nWidth: " << width << "\nHeight: " << height
                  << "\nArea: " << getArea() << "\nPerimeter: " << getPerimeter() << std::endl;
    }
};

class Circle : public Shape {
private:
    double radius;
public:
    Circle(double r) : radius(r) {}
    double getArea() const override {
        return M_PI * radius * radius;
    }
    double getPerimeter() const override {
        return 2 * M_PI * radius;
    }
    void display() const override {
        std::cout << "Circle:\nRadius: " << radius << "\nArea: " << getArea()
                  << "\nPerimeter: " << getPerimeter() << std::endl;
    }
};

// class Triangle : public Shape {
// private:
//     double side1, side2, side3;
// public:
//     Triangle(double s1, double s2, double s3) : side1(s1), side2(s2), side3(s3) {}
//     double getArea() const override {
//         double s = (side1 + side2 + side3) / 2;
//         return sqrt(s * (s - side1) * (s - side2) * (s - side3));
//     }
//     double getPerimeter() const override {
//         return side1 + side2 + side3;
//     }
//     void display() const override {
//         std::cout << "Triangle:\nSide 1: " << side1 << "\nSide 2: " << side2 << "\nSide 3: " << side3
//                   << "\nArea: " << getArea() << "\nPerimeter: " << getPerimeter() << std::endl;
//     }
// };

class Triangle : public Shape {
protected:
    double base;
    double height;

public:
    Triangle(double b, double h) : base(b), height(h) {};
    void display() const override {
        std::cout << "Triangle:\nBase: " << base << "\nHeight: " << height 
                  << "\nArea: " << getArea() << "\nPerimeter: " << getPerimeter() << std::endl;
    }
};

class IsoscelesTriangle : public Triangle {
private:
    double side;

public:
    IsoscelesTriangle(double b, double h, double s) : Triangle(b, h), side(s) {}

    double area() const override {
        return 0.5 * base * height;
    }

    double perimeter() const override {
        return 2 * side + base;
    }

    void display() const override {
        std::cout << "Isosceles Triangle:\n";
        std::cout << "Base: " << base << "\n";
        std::cout << "Height: " << height << "\n";
        std::cout << "Side: " << side << "\n";
        std::cout << "Area: " << area() << "\n";
        std::cout << "Perimeter: " << perimeter() << "\n";
    }
};

class RightTriangle : public Triangle {
private:
    double hypotenuse;

public:
    RightTriangle(double b, double h) : Triangle(b, h) {
        hypotenuse = sqrt(base * base + height * height);
    }

    double area() const override {
        return 0.5 * base * height;
    }

    double perimeter() const override {
        return base + height + hypotenuse;
    }

    void display() const override {
        std::cout << "Right Triangle:\n";
        std::cout << "Base: " << base << "\n";
        std::cout << "Height: " << height << "\n";
        std::cout << "Hypotenuse: " << hypotenuse << "\n";
        std::cout << "Area: " << area() << "\n";
        std::cout << "Perimeter: " << perimeter() << "\n";
    }
};

class IsoscelesTriangle : public Shape {
private:
    double base;
    double height;
    double side;

public:
    IsoscelesTriangle(double b, double h, double s) : base(b), height(h), side(s) {}

    double area() const override {
        return 0.5 * base * height;
    }

    double perimeter() const override {
        return 2 * side + base;
    }

    void display() const override {
        std::cout << "Isosceles Triangle:\n";
        std::cout << "Base: " << base << "\n";
        std::cout << "Height: " << height << "\n";
        std::cout << "Side: " << side << "\n";
        std::cout << "Area: " << area() << "\n";
        std::cout << "Perimeter: " << perimeter() << "\n";
    }
};

class RightTriangle : public Shape {
private:
    double base;
    double height;
    double hypotenuse;

public:
    RightTriangle(double b, double h) : base(b), height(h) {
        hypotenuse = sqrt(base * base + height * height);
    }

    double area() const override {
        return 0.5 * base * height;
    }

    double perimeter() const override {
        return base + height + hypotenuse;
    }

    void display() const override {
        std::cout << "Right Triangle:\n";
        std::cout << "Base: " << base << "\n";
        std::cout << "Height: " << height << "\n";
        std::cout << "Hypotenuse: " << hypotenuse << "\n";
        std::cout << "Area: " << area() << "\n";
        std::cout << "Perimeter: " << perimeter() << "\n";
    }
};


int main() {
    Rectangle rectangle(5, 3);
    Circle circle(4);
    Triangle triangle(3, 4, 5);
    IsoscelesTriangle triangle(4, 4, 3);
    RightTriangle rightTriangle(3, 4);

    rectangle.display();
    std::cout << std::endl;
    circle.display();
    std::cout << std::endl;
    triangle.display();
    std::cout << "\n";
    rightTriangle.display();

    return 0;
}






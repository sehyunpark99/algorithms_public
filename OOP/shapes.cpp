#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <stdbool.h>
#include <cmath>
using namespace std;

class Shape{
    public: 
        Shape() {}; // Constructor
        virtual double getArea() = 0;
        virtual double getPerimeter() = 0;
        virtual void display() = 0;
        // virtual ~Shape() = 0;
};

class Rectangle:public Shape{
    public:
        Rectangle(int w, int h): Shape(), height(h), width(w) {}; // Constructor
        double getArea(){
            double area = width * height;
            return area;
        }
        double getPerimeter(){
            double per = 2*height + 2*width;
            return per;
        }
        void display(){
            cout << "Width: " << width << endl;
            cout << "Height: " << height << endl;
            cout << "Area: " << getArea() << endl;
            cout << "Perimeter: " << getPerimeter() << endl;
        }
        int getWidth(){return width;};
        int getHeight(){return height;};
        void setWidth(int w){width = w;};
        void setHeight(int h){height = h;};
    protected:
        int height;
        int width;
};

class Triangle: public Shape{
    public:
        Triangle(int w, int h, int s): Shape(), side1(w), side2(h), side3(s) {};
        double getArea(){
            double semi = (side1+side2+side3) / 2;
            double area = sqrt(semi*(semi-side1)*(semi-side2)*(semi-side3));
            return area;
        }
        double getPerimeter(){
            double per = side1+side2+side3;
            return per;
        }
        void display(){
            cout << "Side 1: " << side1 << endl;
            cout << "Side 2: " << side2 << endl;
            cout << "Side 3: " << side3 << endl;
            cout << "Area: " << getArea() << endl;
            cout << "Perimeter: " << getPerimeter() << endl;
        }

    protected:
        int side1;
        int side2;
        int side3;
};

class IsoscelesTriangle: public Triangle{
    public:
        IsoscelesTriangle(int w, int h, int s): Triangle(w, h, s) {};
        double getArea(){
            double semi = (side1+side2+side3) / 2;
            double area = sqrt(semi*(semi-side1)*(semi-side2)*(semi-side3));
            return area;
        }
        double getPerimeter(){
            double per = side1+side2+side3;
            return per;
        }
        void display(){
            cout << "Side 1: " << side1 << endl;
            cout << "Side 2: " << side2 << endl;
            cout << "Side 3: " << side3 << endl;
            cout << "Area: " << getArea() << endl;
            cout << "Perimeter: " << getPerimeter() << endl;
        }
};

class RightTriangle: public Triangle{
    public:
        RightTriangle(int w, int h): Triangle(w, h, h) {};
        double getArea(){
            double area = 0.5*side2*side1;
            return area;
        }
        double getPerimeter(){
            double hyp = sqrt(side1*side1 + side2*side2);
            double per = side1+side2+hyp;
            return per;
        }
        void display(){
            cout << "Side 1: " << side1 << endl;
            cout << "Side 2: " << side2 << endl;
            cout << "Area: " << getArea() << endl;
            cout << "Perimeter: " << getPerimeter() << endl;
        }
};


class Circle: public Shape{
    public:
        Circle(int rad): Shape(), radius(rad) {};
        double getArea(){
            double area = 3.14 * radius*radius;
            return area;
        }
        double getPerimeter(){
            double per = 2*3.14*radius; // pi 사용 알아두기
            return per;
        }
        void display(){
            cout << "Radius: " << radius << endl;
            cout << "Area: " << getArea() << endl;
            cout << "Perimeter: " << getPerimeter() << endl;
        }
    protected:
        int radius;
};




int main() {
    Rectangle rectangle(5, 3);
    Circle circle(4);
    Triangle triangle(3, 4, 5);
    IsoscelesTriangle isocletriangle(4, 4, 3);
    RightTriangle rightTriangle(3, 4);

    rectangle.display();
    std::cout << std::endl;
    circle.display();
    std::cout << std::endl;
    triangle.display();
    std::cout << "\n";
    rightTriangle.display();
    std::cout << "\n";
    isocletriangle.display();


    return 0;
}
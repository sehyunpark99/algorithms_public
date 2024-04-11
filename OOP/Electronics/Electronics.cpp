#include <iostream>
#include <string>
#include <vector>
using namespace std;

// My code cannot receive int as an input => was becuase of AddGPU (should not define it as pure virtual function)
// You should use pure virtual functions in C++ when you want to define a function in a base 
// class that must be implemented in derived classes, 
// but you do not want to provide a default implementation in the base class.


class Electronics {
public:
    Electronics(double size_input) : size(size_input) {} // Constructor
    virtual ~Electronics() = 0; // Pure virtual destructor
    double GetSize() { return size; };
    void SetSize(double size_new) { size = size_new; };
    virtual void PrintSelf() = 0; // Pure virtual function
    virtual void AddGPU(Electronics* aGPU) {}; // Default implementation for Electronics 

protected:
    double size; // Member Variable
    double price;
};

Electronics::~Electronics() {} // Destructor definition

class TV : public Electronics {
public:
    TV(double size) : Electronics(size) { price = size * 1.8; } // Constructor
    void PrintSelf() override {
        cout << "It is a TV, Size=" << size << ", Price=" << price << endl;
    }
};

class Computer : public Electronics {
public:
    Computer(double size) : Electronics(size) { price = size * 0.6; } // Constructor
    void PrintSelf() override {
        cout << "It is a Computer, Size=" << size << ", Price=" << price << endl;
    }
};

class Laptop : public Computer {
public:
    Laptop(double size) : Computer(size), total_price(price) {} // Constructor
    void PrintSelf() override {
        cout << "It is a Laptop with " << gpu_list.size() << " GPU(s), Size=" << size << ", Price=" << price << ", Total Price=" << total_price << endl;
    }
    void AddGPU(Electronics* aGPU) override {
        if (gpu_list.empty()) { // For laptop without GPU
            price *= 2;
            total_price = price;
        }
        gpu_list.push_back(aGPU);
        total_price += aGPU->GetSize() * 0.6; // since the parent is computer
    };

protected:
    double total_price;
    vector<Electronics*> gpu_list;
};

class Cellphone : public Electronics {
public:
    Cellphone(double size) : Electronics(size) { price = size * 0.7; } // Constructor
    void PrintSelf() override {
        cout << "It is a Cellphone, Size=" << size << ", Price=" << price << endl;
    }
};

int main() {
    cout << "[CASE 0]" << endl;
    Electronics* e01 = new TV(500);
    Electronics* e02 = new Cellphone(180);
    Laptop* e03 = new Laptop(390);
    e01->PrintSelf();
    e02->PrintSelf();
    e03->PrintSelf();
    delete e01;
    delete e02;
    delete e03;
    cout << "=============================================================================" << endl;

    cout << "[CASE 1]" << endl;
    Electronics* e11 = new TV(710);
    Electronics* e12 = new Cellphone(110);
    Laptop* e13 = new Laptop(360);
    Computer* GPU11 = new Computer(70);
    e13->AddGPU(GPU11);
    e11->PrintSelf();
    e12->PrintSelf();
    e13->PrintSelf();
    delete e11;
    delete e12;
    delete e13;
    delete GPU11;
    cout << "=============================================================================" << endl;

    cout << "[CASE 2]" << endl;
    Electronics* e21 = new TV(560);
    Electronics* e22 = new Cellphone(200);
    Laptop* e23 = new Laptop(230);
    Computer* GPU21 = new Computer(10);
    Computer* GPU22 = new Computer(80);
    e23->AddGPU(GPU21);
    e23->AddGPU(GPU22);
    e21->PrintSelf();
    e22->PrintSelf();
    e23->PrintSelf();
    delete e21;
    delete e22;
    delete e23;
    delete GPU21;
    delete GPU22;
    cout << "=============================================================================" << endl;

    return EXIT_SUCCESS;
}


/*
Output
[CASE 0]
It is a TV, Size=500, Price=900
It is a Cellphone, Size=180, Price=126
It is a Laptop with 0 GPU(s), Size=390, Price=234, Total Price=234
=============================================================================
[CASE 1]
It is a TV, Size=710, Price=1278
It is a Cellphone, Size=110, Price=77
It is a Laptop with 1 GPU(s), Size=360, Price=432, Total Price=474
=============================================================================
[CASE 2]
It is a TV, Size=560, Price=1008
It is a Cellphone, Size=200, Price=140
It is a Laptop with 2 GPU(s), Size=230, Price=276, Total Price=330
=============================================================================
*/
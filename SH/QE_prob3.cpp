// #pragma once
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <stdbool.h>
#include <cmath>
#include <algorithm>
using namespace std;


class Animal {
protected:
    int aniNum = 0;
    string name;
    int weight;

public:
    Animal() {aniNum += 1;};
    virtual string get_name(){
        name = "Animal";
        return name;
    };
    virtual int get_weight(){
        weight = 0;
        return weight;
    };
    ~Animal() {
        aniNum -= 1;
        cout << "Number of animals" << aniNum << endl;
    }
};

class Dog: public Animal{
    public: 
        Dog(): Animal() {aniNum += 1;};
        string get_name(){
            name = "Dog";
            return name;
        }
        int get_weight(){
            weight = 10;
            return weight;
        }
        // Destructor
        virtual ~Dog() {
            aniNum -= 1;
            cout << "Number of animals" << aniNum << endl;
        }
};

class Pug: public Animal{
    public: 
        Pug(): Animal() {aniNum += 1;};
        string get_name(){
            name = "Pug";
            return name;
        }
        int get_weight(){
            weight = 20;
            return weight;
        }
        // Destructor
        virtual ~Pug() {
            aniNum -= 1;
            cout << "Number of animals" <<  aniNum << endl;
        }
};

int main() {
    Animal* animals[] = {
        new Animal(),
        new Dog(),
        new Pug()
    };
    
    for (auto& a : animals) {
        cout << "Name:  " << a->get_name() << ", " << "Weight:   " <<  a->get_weight() << "kg" << endl;
    }

    for (auto& a : animals) {
        delete a;
    }
    return 0;

}

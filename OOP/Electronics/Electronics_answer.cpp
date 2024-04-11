#include <iostream>
#include <vector>

using namespace std;

class Electronics {
    public:
        double size;
        double price;

        Electronics(double size_input) {
            size = SetSize(size_input);
        }

        double GetSize() const {
            return size;
        }

        double SetSize(double size_new){
            return size_new;
        }

        virtual void PrintSelf() {};
        virtual void AddGPU(Electronics* gpu) {};
};

class TV : public Electronics {
    public:
        TV(double size_input) : Electronics(size_input) {
            price = size_input * 1.8;
        }
        
        void PrintSelf() override {
            cout << "It is a TV, Size=" << size << ", Price=" << price << endl;
        }
};

class Computer : public Electronics {
    public:
        Computer(double size_input) : Electronics(size_input) {
            price = size_input * 0.6;
        }

        void PrintSelf() override {
            cout << "It is a Computer, Size=" << size << ", Price=" << price << endl;
        }
};

class Cellphone : public Electronics {
    public:
        Cellphone(double size_input) : Electronics(size_input) {
            price = size * 0.7;
        }

        void PrintSelf() override {
            cout << "It is a Cellphone, Size=" << size << ", Price=" << price << endl;
        }
};

class Laptop : public Computer {
    private:
        vector<Electronics*> gpu_list;
        double price_incl_gpu;

    public:
        Laptop(double size) : Computer(size) {
            price_incl_gpu = price;
        }

        void AddGPU(Electronics* gpu) override {
            if (gpu_list.size() == 0) {
                price = price * 2;
                price_incl_gpu = price;
            }
            gpu_list.push_back(gpu);
            price_incl_gpu = price_incl_gpu + gpu->GetSize() * 0.6;
        }

        void PrintSelf() override {
            cout << "It is a Laptop with " << gpu_list.size() << " GPU(s), Size=" << size << ", Price=" << price <<", Total Price=" << price_incl_gpu << endl;
        }
};

int main() {
    cout << "[CASE 0]" << endl;
    Electronics* e01 = new TV(500);
    Electronics* e02 = new Cellphone(180);
    Laptop * e03 = new Laptop(390);
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
    Laptop * e13 = new Laptop(360);
    Computer * GPU11 = new Computer(70);
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
    Laptop * e23 = new Laptop(230);
    Computer * GPU21 = new Computer(10);
    Computer * GPU22 = new Computer(80);
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
#pragma once

class Bear { 
    public:
    Bear(float aWeight);            // Constructor

    void SetWeight(float aWeight) {weight = aWeight;};  // Weight
    float GetWeight(void) {return(weight);};          // accessors 
    virtual float Aggressiveness(void) {return(weight*1);}; 
    virtual void PrintSelf(void);  

    protected: 
    float weight;     
};

//----Subclass--//
class Polar: public Bear {
    public:
    Polar(float aWeight);
    virtual float Aggressiveness(void);
    virtual void PrintSelf(void);
};

class Grizzly: public Bear {
    public:
    Grizzly(float aWeight);
    virtual float Aggressiveness(void);
    virtual void PrintSelf(void);
};

class Black: public Bear {
    public:
    Black(float aWeight);
    virtual float Aggressiveness(void);
    virtual void PrintSelf(void);
};

class Black_Momma: public Black { 
    public:    
    Black_Momma(float aWeight); 

    void AddCub(Black *aCub); 
    virtual float Aggressiveness(void); 
    float TotalAggressiveness(void); 

    protected: 
    Black *cub;
    int cub_num;
    float cub_aggressiveness; 

    public: 
    virtual void PrintSelf(void); 
}; 

#include <stdio.h> 
#include "NewBear.h"

//--Constructor--//
Bear::Bear(float aWeight) {
    weight = aWeight;
};

Polar::Polar(float aWeight): Bear(aWeight) {
    weight = aWeight;
};

Grizzly::Grizzly(float aWeight): Bear(aWeight) {
    weight = aWeight;
};

Black::Black(float aWeight): Bear(aWeight) {
    weight = aWeight;
};

//--Aggressiveness--//

float Polar:: Aggressiveness(void){
        return(weight*1);
    }; 

float Grizzly:: Aggressiveness(void){
        return(weight*0.9);
    }; 

float Black:: Aggressiveness(void){
        return(weight*0.7);
    }; 

//--Printself--//
void Bear::PrintSelf() {
        printf("I am a bear, Weight=%g, Aggressiveness=%g\n", weight, Aggressiveness());
    };

void Polar::PrintSelf() {
        printf("I am Polar bear, Weight=%g, Aggressiveness=%g\n", weight, Aggressiveness());
    };

void Grizzly::PrintSelf() {
        printf("I am Grizzly bear, Weight=%g, Aggressiveness=%g\n", weight, Aggressiveness());
    };

void Black::PrintSelf() {
        printf("I am Blak bear, Weight=%g, Aggressiveness=%g\n", weight, Aggressiveness());
    };

//---For Black Bear---//
/*** Constructor ***/ 
Black_Momma::Black_Momma(float aWeight) 
              : Black(aWeight) // pass along to the Bear constructor 
{    
	cub = NULL; 
    cub_num=0;
    cub_aggressiveness=0;
}

/*** Accessors ***/ 
void Black_Momma::AddCub(Black *aCub) {
    cub = aCub;
    if (cub_num < 2)
        cub_num++;
        cub_aggressiveness += cub->Aggressiveness();
} 

/*** Aggressiveness ***/ 
float Black_Momma::Aggressiveness(void) { 
    return(Black::Aggressiveness() * 2); 
}

/* The totalAggressiveness is just the mom's aggressiveness + the cub's. */ 
float Black_Momma::TotalAggressiveness(void) { 
    return(Aggressiveness() + cub_aggressiveness); 
} 

void Black_Momma::PrintSelf(void) { 
    printf("I am Black Mommabear with %d cub(s), Weight=%g, Aggressiveness=%g, Total Aggressiveness=%g\n", cub_num, weight, Aggressiveness(), TotalAggressiveness()); 
} 

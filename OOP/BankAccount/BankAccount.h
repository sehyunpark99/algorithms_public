#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

class Account{
    public:
        Account(string id, double bal, string owner); // Constructor
        // Member Functions
        void deposit(double amount);
        bool withdraw(double amount);
        double getBalance() const;
        virtual void displayAccount() = 0; // Virtual pure function

    protected:
        // Member Variables
        string accountID; 
        double balance; 
        string ownerName; 
        // Destructor
        virtual ~Account() {
            cout << "Destructor called for account " << accountID << endl;
        }
};

class CheckingAccount: public Account{
    public:
        CheckingAccount(string id, double bal, string owner, double f); // Constructor
    protected:
        //Additional member variable
        double fee;
    public:
        // Overridden Member Functions
        void deposit(double amount);
        bool withdraw(double amount);
};

class SavingsAccount: public Account{
    public:
        SavingsAccount(string id, double bal, string owner, double rate);
    protected:
        // Additional member variable
        double interestRate;
    public:
        void applyInterest();
};

class Bank{
    protected:
        vector<Account*> accounts;
    public:
        void addAccount(Account* account);
        void displayAllAccounts();
        // Destructor
        virtual ~Bank();
};
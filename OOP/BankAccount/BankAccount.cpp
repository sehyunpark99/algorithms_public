// #pragma once
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <stdbool.h>
// #include <BankAccount.h>
using namespace std;
// g++ -std=c++11 -o BankAccount.exe BankAccount.cpp -lstdc++


// Header
class Account{
    public:
        Account(string id, double bal, string owner):accountID(id), balance(bal), ownerName(owner){}; // Constructor
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
        CheckingAccount(string id, double bal, string owner, double f):Account(id, bal, owner), fee(f){}; // Constructor
    protected:
        //Additional member variable
        double fee;
    public:
        // Overridden Member Functions
        void deposit(double amount);
        bool withdraw(double amount);
        void displayAccount(){
            cout << "Account Type: Checking Account" << endl;
            Account::displayAccount();
        }
};

class SavingsAccount: public Account{
    public:
        SavingsAccount(string id, double bal, string owner, double rate):Account(id, bal, owner), interestRate(rate){};
    protected:
        // Additional member variable
        double interestRate;
    public:
        void applyInterest();
        void displayAccount(){
            cout << "Account Type: Savings Account" << endl;
            Account::displayAccount();
        };
};

// Bank는 constructor 필요없는건가? -> accounts have its own default constructor
class Bank{
    protected:
        vector<Account*> accounts;
    public:
        void addAccount(Account* account);
        void displayAllAccounts();
        // Destructor
        virtual ~Bank(){};
};

// Accessors
void Account::deposit(double amount){
    balance += amount;
};
bool Account::withdraw(double amount){
    if(amount>balance){
        return false;
    }
    else{
        balance -= amount;
        return true;
    }
};
double Account::getBalance() const{
    return balance;
};
// Display what details of the account? you mean the member variables?
void Account::displayAccount(){
    cout << "Account ID: " << accountID << endl;
    cout << "Owner Name: " << ownerName << endl;
    cout << "Balance: " << balance << endl;
};

// Accessors for CheckingAccount
void CheckingAccount::deposit(double amount){
    balance += (amount-fee);
};
bool CheckingAccount::withdraw(double amount){
    if(balance>(amount+fee)){
        balance -= (amount+fee);
        return true;
    }
    return false;
};

// Constructor for SavingsAccount [Try to build constructor inside the class definition]
// SavingsAccount::SavingsAccount(string id, double bal, string owner, double rate){
//     accountID = id;
//     balance = bal;
//     ownerName = owner; 
//     interestRate = rate;
// };
void SavingsAccount::applyInterest(){
    balance *= (1+interestRate); 
};

// Constructor for Bank
void Bank::addAccount(Account* account){
    accounts.push_back(account);
};
// The auto keyword in C++ is used for type inference, which means that the compiler 
// automatically deduces the data type of a variable based on the initializer expression.
void Bank::displayAllAccounts(){
    for (const auto& acc : accounts) {
            acc->displayAccount();
            cout << "=============================" << endl;
        }
};

int main() {
    Bank bank;

    Account* acc1 = new CheckingAccount("C123", 1000.0, "Alice", 5.0);
    Account* acc2 = new SavingsAccount("S456", 2000.0, "Bob", 0.05);

    bank.addAccount(acc1);
    bank.addAccount(acc2);

    // Deposit and withdraw
    acc1->deposit(500.0);
    acc1->withdraw(200.0);

    acc2->deposit(1000.0);
    acc2->withdraw(500.0);

    // Apply interest
    SavingsAccount* savingsAcc = dynamic_cast<SavingsAccount*>(acc2);
    if (savingsAcc) {
        savingsAcc->applyInterest();
    }

    // Display all accounts
    bank.displayAllAccounts();

    return 0;
}
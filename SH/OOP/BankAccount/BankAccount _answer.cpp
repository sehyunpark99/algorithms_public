#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Account {
protected:
    string accountId;
    double balance;
    string ownerName;

public:
    Account(string id, double bal, string owner) : accountId(id), balance(bal), ownerName(owner) {}

    void deposit(double amount) {
        balance += amount;
    }

    bool withdraw(double amount) {
        if (amount > balance) return false;
        balance -= amount;
        return true;
    }

    double getBalance() const {
        return balance;
    }

    string getAccountId() const {
        return accountId;
    }

    virtual void displayAccount() {
        cout << "Account ID: " << accountId << ", Owner: " << ownerName << ", Balance: $" << balance << endl;
    }
};

class CheckingAccount : public Account {
private:
    double fee;

public:
    CheckingAccount(string id, double bal, string owner, double f) : Account(id, bal, owner), fee(f) {}

    void deposit(double amount) {
        balance += (amount - fee);
    }

    bool withdraw(double amount) {
        if (amount + fee > balance) return false;
        balance -= (amount + fee);
        return true;
    }

    void displayAccount() override {
        cout << "Checking ";
        Account::displayAccount();
        cout << "Transaction Fee: $" << fee << endl;
    }
};

class SavingsAccount : public Account {
private:
    double interestRate;

public:
    SavingsAccount(string id, double bal, string owner, double rate) : Account(id, bal, owner), interestRate(rate) {}

    void applyInterest() {
        balance += (balance * interestRate);
    }

    void displayAccount() override {
        cout << "Savings ";
        Account::displayAccount();
        cout << "Interest Rate: " << interestRate * 100 << "%" << endl;
    }
};

class Bank {
private:
    vector<Account*> accounts;

public:
    void addAccount(Account* account) {
        accounts.push_back(account);
    }

    void displayAllAccounts() {
        for (auto& account : accounts) {
            account->displayAccount();
        }
    }

    // 소멸자: 동적 할당된 모든 Account 객체를 해제
    ~Bank() {
        for (auto& account : accounts) {
            delete account;
        }
    }
};

int main() {
    // 테스트 코드 작성
    Bank bank;
    bank.addAccount(new CheckingAccount("CHK123", 1000, "Jeongsik Pyo", 2.5));
    bank.addAccount(new SavingsAccount("SAV456", 1500, "Seongsik Pyo", 0.03));

    bank.displayAllAccounts();
}

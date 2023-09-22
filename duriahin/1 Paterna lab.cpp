#include <iostream>
#include <string>
#include <fstream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

class Operator; // Forward declaration

class Bill {
public:
    double limitingAmount;
    double currentDebt;

    Bill(double limitingAmount) : limitingAmount(limitingAmount), currentDebt(0.0) {}

    bool check(double amount) {
        return currentDebt + amount <= limitingAmount;
    }

    void add(double amount) {
        currentDebt += amount;
    }

    void pay(double amount) {
        currentDebt -= amount;
    }

    void changeTheLimit(double amount) {
        limitingAmount = amount;
    }
};

class Customer {
public:
    int ID;
    std::string name;
    int age;
    Operator* operatorPtr; // �������� �� ���������
    Bill bill;
    double limitingAmount;

    Customer() : ID(0), name(""), age(0), operatorPtr(nullptr), bill(0.0), limitingAmount(0.0) {}

    Customer(int id, const std::string& name, int age, double limitingAmount)
        : ID(id), name(name), age(age), limitingAmount(limitingAmount), operatorPtr(nullptr), bill(limitingAmount) {}

    void talk(int minutes, Customer& other);
    void message(int quantity, Customer& other);
    void connection(double amount);

    // Getter and setter methods for Customer fields
    int getAge() const {
        return age;
    }

    void setAge(int newAge) {
        age = newAge;
    }

    Operator* getOperator() {
        return operatorPtr;
    }

    Bill& getBill() {
        return bill;
    }

    double getLimitingAmount() const {
        return limitingAmount;
    }

    void setLimitingAmount(double amount) {
        limitingAmount = amount;
    }
};

class Operator {
public:
    int ID;
    double talkingCharge;
    double messageCost;
    double networkCharge;
    int discountRate;

    Operator() : ID(0), talkingCharge(0.0), messageCost(0.0), networkCharge(0.0), discountRate(0) {}

    Operator(int id, double talkingCharge, double messageCost, double networkCharge, int discountRate)
        : ID(id), talkingCharge(talkingCharge), messageCost(messageCost), networkCharge(networkCharge), discountRate(discountRate) {}

    double calculateTalkingCost(int minute, Customer& customer) {
        // calculate the cost of the call
        double cost = minute * talkingCharge;

        // apply a discount, if there is one
        if (customer.getAge() < 18) {
            cost -= cost * (discountRate / 100.0);
        }

        return cost;
    }

    double calculateMessageCost(int quantity, Customer& sender, Customer& receiver) {
        // calculate the cost of sending messages
        double cost = quantity * messageCost;

        // apply a discount if both clients have the same operator
        if (sender.getOperator()->ID == receiver.getOperator()->ID) {
            cost -= cost * (discountRate / 100.0);
        }

        return cost;
    }

    double calculateNetworkCost(double amount) {
        return amount * networkCharge;
    }

    // Getter and setter methods for Operator fields
    double getTalkingCharge() const {
        return talkingCharge;
    }

    void setTalkingCharge(double charge) {
        talkingCharge = charge;
    }

    double getMessageCost() const {
        return messageCost;
    }

    void setMessageCost(double cost) {
        messageCost = cost;
    }

    double getNetworkCharge() const {
        return networkCharge;
    }

    void setNetworkCharge(double charge) {
        networkCharge = charge;
    }

    int getDiscountRate() const {
        return discountRate;
    }

    void setDiscountRate(int rate) {
        discountRate = rate;
    }
};

void Customer::talk(int minutes, Customer& other) {
    double cost = operatorPtr->calculateTalkingCost(minutes, other);
    if (bill.check(cost)) {
        bill.add(cost);
        std::cout << name << " talking with " << other.name << " during " << minutes << " minutes per " << cost << " units." << std::endl;
    }
    else {
        std::cout << "The call could not be made: there are not enough funds in the account." << std::endl;
    }
}

void Customer::message(int quantity, Customer& other) {
    double cost = operatorPtr->calculateMessageCost(quantity, *this, other);
    if (bill.check(cost)) {
        bill.add(cost);
        std::cout << name << " sends " << quantity << " messages to " << other.name << " for " << cost << " units." << std::endl;
    }
    else {
        std::cout << "Failed to send messages: insufficient funds in account." << std::endl;
    }
}

void Customer::connection(double amount) {
    double cost = operatorPtr->calculateNetworkCost(amount);
    if (bill.check(cost)) {
        bill.add(cost);
        std::cout << name << " uses the Internet for " << amount << " MB for " << cost << " units." << std::endl;
    }
    else {
        std::cout << "Could not connect to the Internet: insufficient funds in the account." << std::endl;
    }
}

int main() {
    // ������� JSON � �����
    std::ifstream input("info.json");
    json data;
    input >> data;

    // �������� �볺��� �� ��������� � JSON
    Customer customers[2]; // ����� �볺���
    Operator operators[2]; // ����� ���������

    // ������� �볺��� � JSON � ������ �� �� ������ customers
    for (int i = 0; i < 2; i++) {
        int id = data["customers"][i]["id"];
        std::string name = data["customers"][i]["name"];
        int age = data["customers"][i]["age"];
        double limit = data["customers"][i]["limit"];

        customers[i] = Customer(id, name, age, limit);
    }

    // ������� ��������� � JSON � ������ �� �� ������ operators
    for (int i = 0; i < 2; i++) {
        int id = data["operators"][i]["id"];
        double talkingCharge = data["operators"][i]["talkingCharge"];
        double messageCost = data["operators"][i]["messageCost"];
        double networkCharge = data["operators"][i]["networkCharge"];
        int discountRate = data["operators"][i]["discountRate"];

        operators[i] = Operator(id, talkingCharge, messageCost, networkCharge, discountRate);
    }

    std::cout << "Customers:" << std::endl;
    for (const auto& customer : customers) {
        std::cout << "ID: " << customer.ID << ", Name: " << customer.name << ", Age: " << customer.age << ", Limit: " << customer.limitingAmount << std::endl;
    }

    // �������� ������ ���������
    std::cout << "Operators:" << std::endl;
    for (const auto& oper : operators) {
        std::cout << "ID: " << oper.ID << ", Talking Charge: " << oper.talkingCharge << ", Message Cost: " << oper.messageCost << ", Network Charge: " << oper.networkCharge << ", Discount Rate: " << oper.discountRate << std::endl;
    }

    std::cout << "\n";

    // ����������, �� � ���������� ��� �볺��� � ����� customers
    if (sizeof(customers) / sizeof(customers[0]) >= 2) {
        Customer& customer1 = customers[0];
        Customer& customer2 = customers[1];

        // ������������ ��������� �� ��������� ��� �볺���
        customer1.operatorPtr = &operators[0];
        customer2.operatorPtr = &operators[1];

        // �������� �������� �� ����� �볺����� � ������ ����
        customer1.talk(10, customer2);
        customer1.message(5, customer2);
        customer1.connection(200);
        customer1.bill.pay(50);
        customer1.operatorPtr->setTalkingCharge(0.15);
        customer1.limitingAmount = 200;

        std::cout << "\n";
        
        customer2.talk(5, customer1);
        customer2.message(3, customer1);
        customer2.connection(100);
        customer2.bill.pay(30);
        customer2.operatorPtr->setTalkingCharge(0.18);
        customer2.limitingAmount = 300;
    }
    else {
        std::cout << "Error: There should be at least two customers in the JSON data." << std::endl;
        return 1; // �������
    }

    return 0;
}


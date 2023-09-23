namespace Program
{
    internal class Program
    {
        class Customer
        {
            int ID;
            string name;
            int age;
            Operator[] operators;
            Operator currentOperator;
            Bill[] bills;
            Bill currentBill;
            double limit;
            public Customer(int ID, string name, int age, Operator[] operators, Bill[] bills)
            {
                this.ID = ID;
                this.name = name;
                this.age = age;
                this.operators = operators;
                this.bills = bills;
                this.limit = limitingAmount;
            }
            void talk(int minute, Customer other)
            {
                global::System.Console.WriteLine($"{this.name} is talking to {other.name} for {minute}min");
                currentBill.add(currentOperator.calculateTalkingCost(minute, other));
            }
            void message(int quantity, Customer other)
            {
                global::System.Console.WriteLine($"{this.name} is sending {quantity} messages to {other.name}");
                currentBill.add(currentOperator.calculateMessageCost(quantity, this, other));
            }
            void connect(int amount)
            {
                global::System.Console.WriteLine($"{this.name} is connected and can use {amount}Mb of data");
                currentBill.add(currentOperator.calculateNetworkCost(amount));
            }
            void setAge(int age)
            {
                this.age=age;
            }
            int getAge()
            {
                return this.age;
            }
            void setOperators(Operator operators_)
            {
                operators = operator_;
            }
            Operator[] getOperators()
            {
               return operators;
            }
            Operator getCurrentOperator()
            {
                return currentOperator;
            }
            void setCurrentOperator(int ID)
            {
                foreach (var item in operators)
                {
                    if (item.ID == ID)
                    {
                        currentOperator=item;
                        break;
                    }
                }
            }
            void setBills(Bill[] bill)
            {
                this.bills=bill;
            }
            Bill[] getBills()
            {
                return this.bills;
            }
            Bill getCurrentBills()
            {
                return currentBill
            }
            void getCurrentDebt()
            {
                global::System.Console.WriteLine($"Your debt is {currentBill.getCurrentDebt()}");
            }
            void setCurrentBill(int limit)
            {
                foreach (var item in bills)
                {
                    if (item.getLimitingAmount() == limit)
                    {
                        setCurrentBill = item;
                        break;
                    }
                }
            }
        }
        class Operator
        {
            int ID;
            double talkingCharge;
            double messageCost;
            double networkCharge;
            int discountRate;

            public Operator(int ID, double talkingCharge, double messageCost, double networkCharge, int discountRate)
            {
                this.ID = ID;
                this.talkingCharge = talkingCharge;
                this.messageCost = messageCost;
                this.networkCharge = networkCharge;
                this.discountRate = discountRate;
            }
            double calculateTalkingCost(int minute, Customer customer)
            {
                if (discountRate > 0 && (customer.age<18||customer.age>65))
                {
                    return minute * (talkingCharge * (discountRate / 100));
                }
                else
                {
                    return minute * talkingCharge;
                }
            }
            double calculateMessageCost(double quantity, Customer customer1, Customer customer2)
            {
                if (discountRate > 0)
                {
                    if(customer1.operators.ID)
                    return quantity * (messageCost * (discountRate / 100));
                }
                else
                {
                    return quantity * messageCost;
                }
            }
            double calculateNetworkCost(double amount)
            {
                if (discountRate > 0)
                {
                    return amount * (networkCharge * (discountRate / 100));
                }
                else
                {
                    return amount * networkCharge;
                }
            }
            void setTalkingCharge(double cost)
            {
                talkingCharge = cost;
            }
            double getTalkingCharge()
            {
                return talkingCharge;
            }
            void setMessageCharge(double cost)
            {
                messageCost = cost;
            }
            double getMessageCharge()
            {
                return messageCost;
            }
            void setNetworkCharge(double cost)
            {
                networkCharge = cost;
            }
            double getNetworkCharge()
            {
                return networkCharge;
            }
        }
        class Bill
        {
            double limitingAmount;
            double currentDebt = 0;

            public Bill(double limitingAmount)
            {
                this.limitingAmount = limitingAmount;
            }

            bool check(double amount)
            {
                if (amount <= limitingAmount)
                    return true;
                else 
                    return false;
            }
            void add(double amount)
            {
                currentDebt += amount; 
            }
            void pay(double amount)
            {
                currentDebt -= amount;
            }
            void changeTheLimit(double amount)
            {
                limitingAmount = amount;
            }
            void getLimitingAmount()
            {
                return limitingAmount;
            }
            void getCurrentDebt()
            {
                return currentDebt;
            }
        }
        static void Main(string[] args)
        {
            Operator life = new Operator(1, 0.5, 0.3, 5, 10);
            Operator kyivstar = new Operator(2, 0.7, 0.5, 2, 5);
            Operator mts = new Operator(3, 1, 0.3, 6, 12);
            Operator[] operators = { life, kyivstar, mts };

            Bill bill1 = new Bill(100);
            Bill bill2 = new Bill(10);
            Bill bill3 = new Bill(15);
            Bill bill4 = new Bill(1);
            Bill[] bills = { bill1, bill2, bill3 };

            Customer customer1 = new Customer(1, "Vasia", 22, operators, bills);
            Customer customer2 = new Customer(2, "Andrew", 16, operators, bills);
            Customer customer3 = new Customer(3, "Bob", 70, operators, bills);
            Customer customer4 = new Customer(4, "Taras", 35, operators, bills);
            Customer customer5 = new Customer(5, "Dude", 42, operators, bills);

            customer1.setCurrentOperator(2);
            customer1.setCurrentBill(bill2);
            customer1.talk(3, customer4);
            customer1.message(5, customer4);
            customer1.getCurrentDebt();

        }
    }
}
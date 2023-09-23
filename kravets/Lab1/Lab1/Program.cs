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
            Operator currentOperator = new Operator();
            Bill[] bills;
            Bill currentBill = new Bill();
            public Customer(int ID, string name, int age, Operator[] operators, Bill[] bills)
            {
                this.ID = ID;
                this.name = name;
                this.age = age;
                this.operators = operators;
                this.bills = bills;
              
            }
            public void talk(int minute, Customer other)
            {
                global::System.Console.WriteLine($"{this.name} is talking to {other.name} for {minute}min");
                currentBill.add(currentOperator.calculateTalkingCost(minute, other));
            }
            public void message(int quantity, Customer other)
            {
                global::System.Console.WriteLine($"{this.name} is sending {quantity} messages to {other.name}");
                currentBill.add(currentOperator.calculateMessageCost(quantity, this, other));
            }
            public void connect(int amount)
            {
                global::System.Console.WriteLine($"{this.name} is connected and can use {amount}Mb of data");
                currentBill.add(currentOperator.calculateNetworkCost(amount));
            }
            public void setAge(int age)
            {
                this.age = age;
            }
            public int getAge()
            {
                return this.age;
            }
            public void setOperators(Operator[] operators_)
            {
                operators = operators_;
            }
            public Operator[] getOperators()
            {
                return operators;
            }
            public Operator getCurrentOperator()
            {
                return currentOperator;
            }
            public void setCurrentOperator(int ID)
            {
                foreach (var item in operators)
                {
                    if (item.getId() == ID)
                    {
                        currentOperator = item;
                        break;
                    }
                }
            }
            public void setBills(Bill[] bill)
            {
                this.bills = bill;
            }
            public Bill[] getBills()
            {
                return this.bills;
            }
            public Bill getCurrentBills()
            {
                return currentBill;
            }
            public void getCurrentDebt()
            {
                global::System.Console.WriteLine($"Your debt is {Math.Round(currentBill.getCurrentDebt(), 2)}");
            }
            public void setCurrentBill(int limit)
            {
                foreach (var item in bills)
                {
                    if (item.getLimitingAmount() == limit)
                    {
                        currentBill = item;
                        break;
                    }
                }
            }
            public void payBill(double amount)
            {
                currentBill.pay(amount);
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
            public Operator()
            {

            }
            public int getId()
            {
                return ID;
            }
            public double calculateTalkingCost(int minute, Customer customer)
            {
                if (discountRate > 0 && (customer.getAge() < 18 || customer.getAge() > 65))
                {
                    return minute * (talkingCharge * (discountRate / 100));
                }
                else
                {
                    return minute * talkingCharge;
                }
            }
            public double calculateMessageCost(double quantity, Customer customer1, Customer customer2)
            {
                if (discountRate > 0)
                {
                    if (customer1.getCurrentOperator().getId()==customer2.getCurrentOperator().getId())
                        return quantity * (messageCost * (discountRate / 100));
                }
                else
                {
                    return quantity * messageCost;
                }
                return 0;
            }
            public double calculateNetworkCost(double amount)
            {
                    return amount * networkCharge;   
            }
            public void setTalkingCharge(double cost)
            {
                talkingCharge = cost;
            }
            public double getTalkingCharge()
            {
                return talkingCharge;
            }
            public void setMessageCharge(double cost)
            {
                messageCost = cost;
            }
            public double getMessageCharge()
            {
                return messageCost;
            }
            public void setNetworkCharge(double cost)
            {
                networkCharge = cost;
            }
            public double getNetworkCharge()
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
            public Bill()
            {

            }

            public bool check(double amount)
            {
                if (amount <= limitingAmount)
                    return true;
                else
                    return false;
            }
            public void add(double amount)
            {
                currentDebt += amount;
            }
            public void pay(double amount)
            {
                currentDebt -= amount;
            }
            public void changeTheLimit(double amount)
            {
                limitingAmount = amount;
            }
            public double getLimitingAmount()
            {
                return limitingAmount;
            }
            public double getCurrentDebt()
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
            customer1.setCurrentBill(2);
            customer1.talk(3, customer4);
            customer1.message(5, customer4);
            customer1.connect(2);
            customer1.getCurrentDebt();
            customer1.payBill(2);
            customer1.getCurrentDebt();

        }
    }
}
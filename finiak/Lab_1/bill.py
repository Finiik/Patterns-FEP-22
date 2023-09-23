class Bill:
    
    def __init__(self, limit: float = 300, op_id: int = 0) -> None: #конструктор
        self.limit = limit
        self.op_id = op_id
        self.currDebt =  0
        
    #def __str__(self) -> str:
    #  return f"Bill(limit={self.limit}, current_debt={self.current_debt}, customer_id={self.customer_id})"
        
    def checkDebt(self, amount: float) -> bool: #перевірка перевищення боргу
        return (self.currDebt + amount) <- self.limit
    
    def addDebt(self, amount: float) -> None: #додавання боргу
        self.currDebt += amount
        
    def payDebt(self, amount: float) -> None: #оплата боргу
        self.currDebt -= amount
        if self.currDebt < 0:
            self.currDebt = 0
            
    def change_lim(self, new_lim: float) -> None: #зміна ліміту
        self.limit = new_lim
        #print(f"Limit has been risen to {self.limit}")
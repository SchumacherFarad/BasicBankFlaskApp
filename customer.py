class Customer:
    def __init__(self,balance:float, iban:str, name:str,surname:str,password:str):
        self.balance = balance
        self.iban = iban
        self.name = name
        self.surname = surname
        self.password = password
    def deposit(self,money:float):
        self.balance += money
    def withdraw(self,money:float):
        if(money <= self.balance):
            self.balance -= money
    
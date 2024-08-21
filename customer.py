import csv
import os.path

class Customer:
    def __init__(self,balance:float, iban:str, name:str,surname:str,password:str):
        self.balance = balance
        self.iban = iban
        self.name = name
        self.surname = surname
        self.password = password
        self.transactions = []
    def deposit(self,money:float):
        self.balance += money
    def withdraw(self,money:float):
        if(money <= self.balance):
            self.balance -= money
    def readTransactions(self):
        self.transactions.clear()
        if os.path.isfile("./transactions/"+self.iban+".csv"):
            with open(("./transactions/"+self.iban+".csv"),"r") as read:
                csvFile = csv.reader(read)
                for lines in csvFile:
                    isfrom = (lines[0] == "FROM")
                    iban_transacted = lines[1]
                    money_transacted = lines[2]
                    date_transacted = lines[3]
                    self.transactions.append([isfrom,iban_transacted,money_transacted,date_transacted])
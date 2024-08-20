import csv
from customer import Customer
from worker import Worker

class Bank:
    def __init__(self):
        self.customers = []
        self.lastiban = 000000000000000000000000
    def readPeople(self,file:str):
        with open(file,"r") as read:
            csvFile= csv.reader(read)
            for lines in csvFile:
                isworker = (lines[0] == "Worker")
                iban = lines[1]
                if int(iban[2:]) >= self.lastiban:
                    self.lastiban = int(iban[2:])+1
                name = lines[2]
                surname = lines[3]
                balance = lines[4]
                password = lines[5]
                if isworker:
                    salary = lines[6]
                    to_be_added = Worker(balance, iban, name, surname, password, salary)
                    self.customers.append(to_be_added)
                else:
                    to_be_added = Customer(balance, iban, name, surname, password)
                    self.customers.append(to_be_added)
    def writePeople(self,file:str):
        with open(file, "w") as write:
            for person in self.customers:
                if isinstance(person, Worker):
                    write.write(f"Worker,{person.iban},{person.name},{person.surname},{person.balance},{person.password},{person.salary}\n")
                else:
                    write.write(f"Customer,{person.iban},{person.name},{person.surname},{person.balance},{person.password}\n")
    def addPerson(self, isworker:bool, name:str, surname:str, password:str, balance:float, salary:float = None):
        if isworker:
            lastibanlength = len(str(self.lastiban))
            to_be_added = Worker(balance, f"TR{(24-lastibanlength)*'0'}{self.lastiban}", name, surname, password, salary)
            self.customers.append(to_be_added)
            self.lastiban +=1
        else:
            lastibanlength = len(str(self.lastiban))
            to_be_added = Customer(balance, f"TR{(24-lastibanlength)*'0'}{self.lastiban}", name, surname, password)
            self.customers.append(to_be_added)
            self.lastiban +=1
    def transferMoney(self,fromiban:str, toiban:str, money:float):
        fromindex:int
        toindex:int
        for i in range(0,len(self.customers)):
            if self.customers[i].iban == fromiban:
                fromindex = i
            if self.customers[i].iban == toiban:
                toindex = i
        if self.customers[fromindex].balance >= money:
            self.customers[fromindex].withdraw(money)
            self.customers[toindex].deposit(money)
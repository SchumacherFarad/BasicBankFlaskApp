from customer import Customer

class Worker(Customer):
    def __init__(self, balance: float, iban: str, name: str, surname: str, password: str, salary : float):
        super().__init__(balance, iban, name, surname, password)
        self.salary = salary
    def giveRaise(self, percentage:float):
        self.salary += self.salary*percentage/100
    def getSalary(self):
        self.balance += self.salary
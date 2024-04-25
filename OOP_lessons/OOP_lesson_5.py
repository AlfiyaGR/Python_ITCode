class Employees:
    def get_paid(self):
        print(self.salary)


class Worker(Employees):
    def __init__(self, salary):
        self.salary = salary


class Manager(Employees):
    def __init__(self, salary):
        self.salary = salary


worker = Worker(1000)
manager = Manager(2000)

worker.get_paid()
manager.get_paid()

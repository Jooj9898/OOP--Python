class rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def area(self):
        area = self.width * self.length
        return area
    def perimeter(self):
        perimeter = self.width + self.length
        return perimeter

inst1 = rectangle(5,10)
print(inst1.perimeter())
print(inst1.area())

class bank_account():
    def __init__(self,IBAN, acc_no,funds,transactions):
        self.IBAN = IBAN
        self.acc_no = acc_no
        self.funds = funds
        self.transactions = transactions

    def withdraw(self, amount):
        self.funds = self.funds - amount
        self.transactions.append(-amount)
        if len(self.transactions) > 5:
            self.transactions.pop(0)
        return self.funds

    def deposit(self, amount):
        self.funds = self.funds + amount
        self.transactions.append(+amount)
        if len(self.transactions) > 5:
            self.transactions.pop(0)
        return self.funds
inst1 = bank_account('IE49AIBK', '12345',500,[])
print(inst1.withdraw(5))
print(inst1.deposit(10))
print(inst1.transactions)

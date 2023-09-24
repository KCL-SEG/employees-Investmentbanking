"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:

    def __init__(self, name, monthly_contract, hours, hourly_rate, contract_commission, pay_commission, bonus_commission):
        self.name = name
        self.monthly_contract = monthly_contract
        self.hours = hours
        self.hourly_rate = hourly_rate
        self.contract_commission  = contract_commission
        self.pay_commission = pay_commission
        self.bonus_commission = bonus_commission

    def get_pay(self):
        pay = 0
        total_contract_commission = 0
        total_contract_pay = 0

        if self.monthly_contract > 0 and self.contract_commission > 0 and self.pay_commission > 0:
            total_contract_commission = self.contract_commission * self.pay_commission
            pay = self.monthly_contract + total_contract_commission
            return pay

        elif self.monthly_contract > 0 and self.bonus_commission > 0:
            pay = self.monthly_contract + self.bonus_commission
            return pay

        elif self.monthly_contract > 0:
            pay = self.monthly_contract
            return pay
        
        elif self.hours > 0 and self.hourly_rate > 0 and self.contract_commission > 0 and self.pay_commission > 0:
            total_contract_pay = self.hourly_rate * self.hours
            total_contract_commission = self.contract_commission * self.pay_commission
            pay = total_contract_pay + total_contract_commission
            return pay
        
        elif self.hours > 0 and self.hourly_rate > 0 and self.bonus_commission > 0:
            total_contract_pay = self.hourly_rate * self.hours
            pay = total_contract_pay + self.bonus_commission
            return pay
        
        elif self.hours > 0 and self.hourly_rate > 0:
            pay = self.hourly_rate * self.hours
            return pay



    def __str__(self):
        # renee
        if self.monthly_contract > 0 and self.contract_commission > 0 and self.pay_commission > 0:
            return f'{self.name} works on a monthly salary of {self.monthly_contract} and receives a commission for {self.contract_commission} contract(s) at {self.pay_commission}/contract.  Their total pay is {self.get_pay()}.'

        # robbie
        elif self.monthly_contract > 0 and self.bonus_commission > 0:
            return f'{self.name} works on a monthly salary of {self.monthly_contract} and receives a bonus commission of {self.bonus_commission}.  Their total pay is {self.get_pay()}.'

        # billie
        elif self.monthly_contract > 0:
            return f'{self.name} works on a monthly salary of {self.monthly_contract}.  Their total pay is {self.get_pay()}.'
        
        # jan
        elif self.hours > 0 and self.hourly_rate > 0 and self.contract_commission > 0 and self.pay_commission > 0:
            return f'{self.name} works on a contract of {self.hours} hours at {self.hourly_rate}/hour and receives a commission for {self.contract_commission} contract(s) at {self.pay_commission}/contract.  Their total pay is {self.get_pay()}.'
        
        # ariel
        elif self.hours > 0 and self.hourly_rate > 0 and self.bonus_commission > 0:
            return f'{self.name} works on a contract of {self.hours} hours at {self.hourly_rate}/hour and receives a bonus commission of {self.bonus_commission}.  Their total pay is {self.get_pay()}.'

        # charlie
        elif self.hours > 0 and self.hourly_rate > 0:
            return f'{self.name} works on a contract of {self.hours} hours at {self.hourly_rate}/hour.  Their total pay is {self.get_pay()}.'

        

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 0, 0, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 100, 25, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 4, 200, 0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 150, 25, 3, 220, 0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 0, 0, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 120, 30, 0, 0, 600)

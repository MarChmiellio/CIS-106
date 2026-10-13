class Employee:
  def __init__ (self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@topgolf.com'
  def bonus(self, rate):
    b = float(rate) * float(self.pay)
    return b
emp1 = Employee('Michael', 'Chmiel', 60000.00)
print(emp1.email)
print(emp1.first)
print(emp1.last)
print(emp1.pay)
rate = float(input("Enter bonus rate (decimal): "))
bonus_amount = emp1.bonus(rate)
print("Emplyee Bonus:", bonus_amount)

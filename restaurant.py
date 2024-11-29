from menu import Menu

class Restaurant:       # employee add, delete eishb function korar jonne     
  def __init__(self, name):
    self.name = name    # restaurant name
    self.employees = []           # eta hocce amdr database
    self.menu = Menu()

  def add_employee(self, employee): #employee object pass kore dibo o just add korbe new object ta
  # Employee class er ekta object create hoye jabe
    self.employees.append(employee)
   

  def view_employee(self):
    print("Employee List!!")
    for emp in self.employees:
      print(emp.name, emp.email, emp.phone, emp.address)

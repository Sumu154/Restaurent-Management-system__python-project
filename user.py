from abc import ABC   # abstract base class


class User(ABC):
  def __init__(self, name, phone, email, address):
    self.name = name
    self.phone = phone
    self.email = email
    self.address = address


class Employee(User):
  def __init__(self, name, phone, email, address, age, designation, salary):
    super().__init__(name, phone, email, address)
    self.age = age
    self.designation = designation
    self.salary = salary


class Admin(User):
  def __init__(self, name, phone, email, address):
    super().__init__(name, phone, email, address)

  
  def add_employee(self, restaurant, employee):
    restaurant.add_employee(employee)

  def view_employee(self, restaurant):
    restaurant.view_employee()
  
  def add_view_item(self, restaurant, item):
    restaurant.menu.add_menu_item(item)

  def remove_item(self, restaurant, item):
    restaurant.menu.remove_item(item)

  


class Restaurant:       # employee add, delete eishb function korar jonne     
  def __init__(self, name):
    self.name = name    # restaurant name
    self.employees = []           # eta hocce amdr database
    self.menu = FoodItem()

  def add_employee(self, employee): #employee object pass kore dibo o just add korbe new object ta
  # Employee class er ekta object create hoye jabe
    self.employees.append(employee)
   

  def view_employee(self):
    print("Employee List!!")
    for emp in self.employees:
      print(emp.name, emp.email, emp.phone, emp.address)





class Menu:
  def __init__(self):
    self.items = []          # items er databse

  def add_menu_item(self, item):
    self.items.append(item)
  
  def find_item(self, item_name):
    for item in self.items:
      if item.name.lower() == item_name.lower():
        return item
    return None
  
  def remove_item(self, item_name):
    item = self.find_item(item_name)
    if item:
      self.items.remove(item)
      print("Item deleted")
    else:
      print("Items not found")

  def show_menu(self):
    print("****** Menu ******")
    print("name\tPrice\tQuantity")
    for item in self.items:
      print(f"{item.name}\t{item.price}\t{item.quantity}")



class FoodItem:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity
    


mn = Menu()
item= FoodItem('Pizza', 120, 10)
mn.add_menu_item(item)
mn.show_menu()
   

# emp = Employee('Sumaiya', 'sumaiya@gmail.com', 12345, 'Dhaka', 21, 'chef', 12000)
# print(emp.name)



# ad = Admin('Karim', 1234, 'karim@gmail.com', 'Dhaka')
# ad.add_employee('Sagor', 'sagor@gmail.com', '12123', 'Khulna', 21, 'Chef', 12300)
# ad.view_employee()

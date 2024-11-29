from foodItem import FoodItem
from menu import Menu
from orders import Order
from restaurant import Restaurant
from user import Customer, Admin, Employee


restu = Restaurant("mamar_restu")
def customer_menu():
  name = input("Enter your name: ")
  email = input("Enter your Email: ")
  phone = input("Enter your Phone: ")
  address = input("Enter your address: ")
  customer = Customer(name=name, email=email, phone=phone, address=address)

  while True:
    print(f"Welcome {customer.name}!!")
    print("1. View Menu")
    print("2. Add intem to cart")
    print("3. View cart")
    print("4. PayBill")
    print("5. Exit")


    ch = int(input("Enter your choice: "))
    if ch==1:
      customer.view_menu(restu)
    elif ch==2:
      item_name = input("Enter item name: ")
      item_quantity = int(input("ENter item quantity: "))
      customer.add_to_cart(restu, item_name, item_quantity)
    elif ch==3:
      customer.view_cart()
    elif ch==4:
      customer.pay_bill()
    elif ch==5:
      break
    else:
      print("Invalid choice")


def admin_menu():
  name = input("Enter your name: ")
  email = input("Enter your Email: ")
  phone = input("Enter your Phone: ")
  address = input("Enter your address: ")
  admin = Admin(name=name, email=email, phone=phone, address=address)

  while True:
    print(f"Welcome {admin.name}!!")
    print("1. Add New Item")
    print("2. Add new Employee")
    print("3. View Employee")
    print("4. View Items")
    print("5. Delete Item")
    print("6. Exit")


    ch = int(input("Enter your choice: "))
    if ch==1:
      item_name = input("Enter Item name: ")
      item_price = input("Enter Item Price: ")
      item_quantity = input("Enter Item Quantity: ")
      item = FoodItem(item_name, item_price, item_quantity)

      admin.add_new_item(restu, item)
    elif ch==2:
      name = input("Enter employee name: ")
      phone = input("Enter employee phone: ")
      email = input("Enter employee email: ")
      address = input("Enter employee address: ")
      age = input("Enter employee age: ")
      designation = input("Enter employee designation: ")
      salary = input("Enter employee salary: ")
      employee = Employee(name, email, phone, address, age, designation, salary)

      admin.add_employee(restu, employee)

    elif ch==3:
      admin.view_employee(restu)
    elif ch==4:
      admin.view_menu(restu)
    elif ch==5:
      item_name = input("Enter item name: ")
      admin.remove_item(restu, item_name)
    elif ch==6:
      break
    else:
      print("Invalid choice")



while True:
  print("*** Welcome ***")
  print("1. Customer")
  print("2. Admin")
  print("3. Exit")

  ch = int(input("Enter your choice: "))
  if ch==1:
    customer_menu()
  elif ch==2:
    admin_menu()
  elif ch==3:
      break
  else:
    print("Invalid choice")





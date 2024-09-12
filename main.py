from customer import Customer
from coffee import Coffee
from order import Order

# Creating of customers 
customer1 = Customer("Josh")
customer2 = Customer("Peter")
customer3 = Customer("Terence")

# Creating of coffee available
coffee1 = Coffee("Americano")
coffee2 = Coffee("Espresso")
coffee3 = Coffee("Cappuccino")


order1 = customer1.create_order(coffee1, 4.0)  #creatiing of orders for customer 1 
order2 = customer1.create_order(coffee2, 3.5)  


order3 = customer2.create_order(coffee3, 5.0)  # for customer 2 
order4 = customer2.create_order(coffee2, 3.5) 


order5 = customer3.create_order(coffee2, 4.0)  # for customer 3 

# customer orders
print(f"{customer1.name}'s Orders: {[order.coffee.name for order in customer1.orders()]}")
print(f"{customer2.name}'s Orders: {[order.coffee.name for order in customer2.orders()]}")
print(f"{customer3.name}'s Orders: {[order.coffee.name for order in customer3.orders()]}")


print(f"{coffee1.name} Customers: {[customer.name for customer in coffee1.customers()]}")
print(f"{coffee2.name} Customers: {[customer.name for customer in coffee2.customers()]}")
print(f"{coffee3.name} Customers: {[customer.name for customer in coffee3.customers()]}")

# Checking average price for each coffee 
print(f"Average price of {coffee1.name}: ${coffee1.average_price():.2f}")
print(f"Average price of {coffee2.name}: ${coffee2.average_price():.2f}")
print(f"Average price of {coffee3.name}: ${coffee3.average_price():.2f}")

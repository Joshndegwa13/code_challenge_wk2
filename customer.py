class Customer:
    def __init__(self, name):
        
        if isinstance(name, str) and 1 <= len(name) <= 15: #name that must be a string and have 1 to 15 char
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._orders = []

    # Property to get the customer's name
    @property
    def name(self):
        return self._name

    #  for Returning all orders for the customer
    def orders(self):
        return self._orders

    #  for returining all coffee ordered by the customers 
    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    # Creating  a new order for the customer
    def create_order(self, coffee, price):
        from order import Order  
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        return new_order

class Coffee:
    def __init__(self, name):
        
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Name must be a string with at least 3 characters.")
        self._orders = []

    # Property to get the coffee's name
    @property
    def name(self):
        return self._name

    # Returning  all orders for the coffee
    def orders(self):
        return self._orders

    # Returning all customers who have ordered this coffee
    def customers(self):
        return list(set(order.customer for order in self._orders))

    # total number of coffee orders 
    def num_orders(self):
        return len(self._orders)

    # Getting the average price of the coffee 
    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)

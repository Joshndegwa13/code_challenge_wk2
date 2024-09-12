class Order:
    def __init__(self, customer, coffee, price):
        
        if isinstance(price, (int, float)) and 1.0 <= price <= 10.0:
            self._price = float(price)
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")

        # Initializing customer and coffee attributes
        self._customer = customer
        self._coffee = coffee

        # Addoing  the order to customer and coffee order list
        customer._orders.append(self)
        coffee._orders.append(self)

       #method for returing the price 
    @property
    def price(self):
        return self._price

    # mehtod for returning the customer associated with the order 
    @property
    def customer(self):
        return self._customer

    # method for returininng the coffee associated with the order 
    @property
    def coffee(self):
        return self._coffee

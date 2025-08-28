class Customer:
    def __init__(self, name: str):
        self._name = None
        self.name = name  
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        # Must be str, 1–15 chars, otherwise ignore
        if isinstance(value, str) and (1 <= len(value) <= 15):
            self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)


class Coffee:
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass

    def orders(self):
        return self._orders

    def customers(self):
        return list({order.customer for order in self._orders})

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)


class Order:
    all = []  

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("Order customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("Order coffee must be a Coffee instance")
        if not isinstance(price, float):
            raise TypeError("Price must be a float")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price

        customer._orders.append(self)
        coffee._orders.append(self)
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        pass

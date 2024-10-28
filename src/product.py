class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description} {self.price} {self.quantity}')"

    def __str__(self):
        if self.__price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        sum_product = self.price * self.quantity + other.price * other.quantity
        print(type(sum_product))
        return sum_product

    @classmethod
    def new_product(cls, product):
        name = product["name"]
        description = product["description"]
        price = product["price"]
        quantity = product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


if __name__ == "__main__":
    product_1 = Product("tomato", "red tomato from Azerbaijan", 150, 10)
    product_2 = Product("cucumber", "cucumber from Azerbaijan", 100, 20)
    # print(product_1)
    product_3 = {
        "name": "Помидоры",
        "description": "Помидоры красные, вкусные, не дорого",
        "price": 180,
        "quantity": 10,
    }
    product_add = Product.new_product(product_3)
    # print(product_add)
    # product_2.price = 20
    # print(product_2)
    print(product_1 + product_2)

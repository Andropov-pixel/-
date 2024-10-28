from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        Category.category_count += 1
        Category.product_count += len(products)
        self.name = name
        self.description = description
        self.__products = products

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}')"

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return [
            f"Название продукта : {product.name}, цена : {product.price} рублей, Остаток: {product.quantity} штук."
            for product in self.__products
        ]

    @products.setter
    def products(self, new_products):
        self.__products = new_products


class Sort:
    def __init__(self, product_of_category):
        self.product = product_of_category
        self.index = 0

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index == len(self.product) - 1:
            raise StopIteration
        else:
            self.index += 1
            return self.product[self.index]


if __name__ == "__main__":
    product_1 = Product("tomato", "red tomato from Azerbaijan", 150, 10)
    product_2 = Product("cucumber", "cucumber from Azerbaijan", 100, 20)
    # print(product_1)
    category_1 = Category("products", "products for salad", [product_1, product_2])
    # print(category_1)
    product_3 = Product("lettuce", "fresh lettuce", 50, 15)
    category_1.add_product(product_3)
    # print(Category.category_count)
    # print(repr(category_1))
    cat = Sort([product_1, product_2])
    # print(cat.product)
    for prod in cat:
        print(prod)

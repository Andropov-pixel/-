class MixinLog:

    def __init__(self):
        # super().__init__()
        self.name = None
        self.description = None
        self.price = None
        self.quantity = None
        print(repr(self))

    # def __init__(self, name, description, price, quantity):
    #     self.name = name
    #     self.description = description
    #     self.__price = price
    #     self.quantity = quantity
    #     MixinLog.__init__(self)  # напрямую обращаемся к
    #     родителю в инициализацию и отдаём себя, как объект

    def __repr__(self):
        return (f"{self.__class__.__name__} ({self.name},"
                f" {self.description}, {self.price}, {self.quantity})")

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age


class Price:
    def __init__(self, currency: str, value: int) -> None:
        self.currency: str = currency
        self.value: int = value

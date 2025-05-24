class Jar:
    @classmethod
    def get_jar(cls):
        user_capacity = int(input("Define Jar's capacity: "))
        return cls(user_capacity)

    def __init__(self, capacity=12):
        if type(capacity) != int or capacity < 0:
            raise ValueError("Value Error!")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if type(n) != int or n < 0 or (n + self.size) > self.capacity:
            raise ValueError("Value Error!")
        self._size += n

    def withdraw(self, n):
        if type(n) != int or n < 0 or n > self.size:
            raise ValueError("Value Error!")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    my_jar = Jar.get_jar()
    my_jar.deposit(3)
    print(my_jar)
    my_jar.withdraw(1)
    print(my_jar)


if __name__ == "__main__":
    main()

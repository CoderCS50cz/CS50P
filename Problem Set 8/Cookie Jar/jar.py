class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("No coockies")
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return self._size * "🍪"


    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("Jar is over by cookies")
        self._size = self._size + n


    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Jar is out of cookies")
        self._size = self._size - n


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size

"""
cookies = Jar()
cookies.deposit(n = int(input("Adding cookie to the jar: ")))
cookies.withdraw(n = int(input("Withdraw cookie from the jar: ")))
print(cookies)
"""

# Implementation a hash table using proping
class PropingHashTable:
    class __Bucket:
        class __KeyValueData:
            def __init__(self, key, value):
                self.key = key
                self.value = value

        def __init__(self):
            self.pair = None

        def get(self, key):
            if self.pair:
                if self.pair.key == key:
                    return self.pair.value
                raise IndexError
            raise KeyError

        def set(self, key, value):
            if self.pair:
                if self.pair.key == key:
                    self.pair.value = value

                raise IndexError
            self.pair = self.__KeyValueData(key, value)

        def remove(self, key):
            if self.pair:
                if self.pair.key == key:
                    self.pair = None
                raise IndexError
            raise KeyError

        def __str__(self) -> str:
            if self.pair:
                return f"{self.pair.key}:{self.pair.value}"
            return ""

    def __init__(self, size):
        self.__size = size
        self.__table = [self.__Bucket() for _ in range(self.__size)]

    def __hash(self, key):
        return key % self.__size

    def set(self, key, value):
        hk = self.__hash(key)
        while hk < self.__size:
            try:
                self.__table[hk].set(key, value)
                return
            except IndexError:
                hk += 1
        else:
            raise OverflowError

    def get(self, key):
        hk = self.__hash(key)
        while hk < self.__size:
            try:
                return self.__table[hk].get(key)
            except IndexError:
                hk += 1
        else:
            raise KeyError

    def remove(self, key):
        hk = self.__hash(key)
        while hk < self.__size:
            try:
                self.__table[hk].remove(key)
                return
            except IndexError:
                hk += 1
        else:
            raise KeyError

    def print_table(self):
        print([str(x) for x in self.__table])



tht = PropingHashTable(10)
tht.set(2, "first value")
print(tht.get(2))

tht.set(12, "second value")
print(tht.get(12))

tht.set(9, "trird value")
print(tht.get(9))

tht.print_table()


# Implementation a hash table using chaining
class ChainingHashTable:
    class __Bucket:
        class __KeyValueData:
            def __init__(self, key, value):
                self.key = key
                self.value = value

        def __init__(self):
            self.__pairs = []

        def get(self, key):
            res = [pair for pair in self.__pairs if pair.key == key]
            if res:
                return res[0].value
            raise KeyError

        def set(self, key, value):
            res = [pair for pair in self.__pairs if pair.key == key]
            if res:
                res.value = value
                return
            self.__pairs.append(self.__KeyValueData(key, value))

        def remove(self, key):
            res = [pair for pair in self.__pairs if pair.key == key]
            if res:
                self.__pairs.remove(res[0])
                return
            raise KeyError

        def __str__(self) -> str:
            if self.__pairs:
                return "-".join([f"({pair.key}:{pair.value})" for pair in self.__pairs])

            return ""

    def __init__(self, size):
        self.__size = size
        self.__table = [self.__Bucket() for _ in range(self.__size)]

    def __hash(self, key):
        return key % self.__size

    def set(self, key, value):
        hk = self.__hash(key)
        self.__table[hk].set(key, value)

    def get(self, key):
        hk = self.__hash(key)
        return self.__table[hk].get(key)

    def remove(self, key):
        hk = self.__hash(key)
        return self.__table[hk].remove(key)

    def print_table(self):
        print([str(x) for x in self.__table])


tht = ChainingHashTable(10)
tht.set(2, "first value")
print(tht.get(2))

tht.set(12, "second value")
print(tht.get(12))

tht.set(9, "trird value")
print(tht.get(9))

tht.print_table()

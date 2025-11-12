from hash_function import poly_hash, djb2

class HashTableChaining:
    def __init__(self, size=8):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        return poly_hash(key) % self.size

    def insert(self, key, value):
        h = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[h]):
            if k == key:
                self.buckets[h][i] = (key, value)
                return
        self.buckets[h].append((key, value))
        self.count += 1

        # Проверяем, нужен ли ресайз
        if self.count / self.size > 0.7:
            self._resize()

    def _resize(self):
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        for bucket in old_buckets:
            for key, value in bucket:
                self.insert(key, value)

class HashTableLinear:
    def __init__(self, size=8):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return djb2(key) % self.size

    def insert(self, key, value):
        h = self._hash(key)
        for i in range(self.size):
            idx = (h + i) % self.size
            if self.table[idx] is None or self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return
        raise Exception("Таблица переполнена")
    
class HashTableDouble:
    def __init__(self, size=8):
        self.size = size
        self.table = [None] * size

    def _hash1(self, key):
        return poly_hash(key) % self.size

    def _hash2(self, key):
        return (djb2(key) % (self.size - 1)) + 1  # шаг не равен 0

    def insert(self, key, value):
        h1 = self._hash1(key)
        h2 = self._hash2(key)
        for i in range(self.size):
            idx = (h1 + i * h2) % self.size
            if self.table[idx] is None or self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return
        raise Exception("Таблица переполнена")

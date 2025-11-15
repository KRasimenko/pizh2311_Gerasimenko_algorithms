from hash_function import poly_hash, djb2

class HashTableChaining:
    def __init__(self, size=8, hash_func=poly_hash):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0
        self.hash_func = hash_func

    def _hash(self, key):
        return self.hash_func(key) % self.size

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
        self.count = 0
        for bucket in old_buckets:
            for key, value in bucket:
                h = self._hash(key)
                self.buckets[h].append((key, value))
                self.count += 1

    def find(self, key):
        """Поиск значения по ключу."""
        h = self._hash(key)
        for k, v in self.buckets[h]:
            if k == key:
                return v
        return None
# Средняя сложность O(1)
# Наихудшая слольность O(n)

class HashTableLinear:
    def __init__(self, size=8, hash_func=djb2):
        self.size = size
        self.table = [None] * size
        self.hash_func = hash_func

    def _hash(self, key):
        return self.hash_func(key) % self.size

    def insert(self, key, value):
        h = self._hash(key)
        for i in range(self.size):
            idx = (h + i) % self.size
            if self.table[idx] is None or self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return
        raise Exception("Таблица переполнена")
    
    def find(self, key):
        """Поиск элемента по ключу."""
        h = self._hash(key)
        for i in range(self.size):
            idx = (h + i) % self.size
            if self.table[idx] is None:
                return None
            if self.table[idx][0] == key:
                return self.table[idx][1]
        return None
# Средняя сложность O(1)
# Наихудшая слольность O(n)
    
class HashTableDouble:
    def __init__(self, size=8, hash_func1=poly_hash, hash_func2=djb2):
        self.size = size
        self.table = [None] * size
        self.hash_func1 = hash_func1
        self.hash_func2 = hash_func2

    def _hash1(self, key):
        return self.hash_func1(key) % self.size

    def _hash2(self, key):
        return (self.hash_func2(key) % (self.size - 1)) + 1  # шаг не равен 0

    def insert(self, key, value):
        h1 = self._hash1(key)
        h2 = self._hash2(key)
        for i in range(self.size):
            idx = (h1 + i * h2) % self.size
            if self.table[idx] is None or self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return
        raise Exception("Таблица переполнена")
    
    def find(self, key):
        """Поиск элемента по ключу."""
        h1 = self._hash1(key)
        h2 = self._hash2(key)
        for i in range(self.size):
            idx = (h1 + i * h2) % self.size
            if self.table[idx] is None:
                return None
            if self.table[idx][0] == key:
                return self.table[idx][1]
        return None
# Средняя сложность O(1)
# Наихудшая слольность O(n)

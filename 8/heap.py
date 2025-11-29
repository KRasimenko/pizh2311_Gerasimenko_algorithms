class Heap:
    def __init__(self, is_min=True):
        self.data = []  # внутренний массив для хранения элементов кучи
        self.is_min = is_min  # True для min-кучи, False для max-кучи

    # Всплытие элемента вверх
    def _sift_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self._compare(self.data[index], self.data[parent]):
            # Меняем местами текущий элемент с родителем
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent
            parent = (index - 1) // 2
        # Сложность: O(log n)

    # Погружение элемента вниз
    def _sift_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            target = index
            if left < size and self._compare(self.data[left],
                                             self.data[target]):
                target = left
            if right < size and self._compare(self.data[right],
                                              self.data[target]):
                target = right
            if target == index:
                break
            self.data[index], self.data[target] = self.data[target], self.data[index]
            index = target
        # Сложность: O(log n)

    # Метод сравнения в зависимости от типа кучи

    def _compare(self, child, parent):
        if self.is_min:
            return child < parent  # для min-кучи
        else:
            return child > parent  # для max-кучи
        # Сложность: O(1)

    # Вставка нового элемента
    def insert(self, value):
        self.data.append(value)
        self._sift_up(len(self.data) - 1)
        # Сложность: O(log n)

    # Извлечение корня (минимум для min-кучи, максимум для max-кучи)

    def extract(self):
        if not self.data:
            return None
        root = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        return root
        # Сложность: O(log n)

    # Просмотр корня без извлечения
    def peek(self):
        if self.data:
            return self.data[0]
        return None
        # Сложность: O(1)

    # Построение кучи из массива
    def build_heap(self, array):
        self.data = array[:]
        # Погружаем элементы начиная с середины
        for i in range(len(self.data)//2 - 1, -1, -1):
            self._sift_down(i)
        # Сложность: O(n)

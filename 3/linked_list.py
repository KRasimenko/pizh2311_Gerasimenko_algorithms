class Node:
    """Класс узла связного списка"""
    def __init__(self, data):
        self.data = data      # данные в узле
        self.next = None      # ссылка на следующий узел


class LinkedList:
    """Класс связного списка"""
    def __init__(self):
        self.head = None      # голова списка (первый элемент)
        self.tail = None      # хвост списка (для O(1) вставки в конец)

    # Вставка в начало (O(1))
    def insert_at_start(self, data):
        new_node = Node(data)     # создаём новый узел
        new_node.next = self.head
        self.head = new_node      # теперь он — голова списка
        if self.tail is None:     # если список был пуст
            self.tail = new_node  # хвост тоже указывает на него
        # Сложность: O(1)

    # Вставка в конец (O(1) при хвосте, иначе O(n))
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:     # если список пуст
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            # "старый хвост" указывает на новый узел
            self.tail = new_node      # теперь новый узел становится хвостом
        # Сложность: O(1) при наличии tail, иначе O(n)

    # Удаление из начала (O(1))
    def delete_from_start(self):
        if self.head is None:
            print("Список пуст, нечего удалять")
            return
        removed_data = self.head.data   # данные удаляемого узла
        self.head = self.head.next      # смещаем голову на следующий узел
        if self.head is None:           # если список стал пустым
            self.tail = None
        return removed_data
        # Сложность: O(1)

    def traversal(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")   # конец списка
        # Сложность: O(n)

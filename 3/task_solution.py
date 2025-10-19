from collections import deque


def is_balanced_brackets(expression):
    """Проверяет, сбалансированы ли скобки в выражении"""
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in '({[':
            stack.append(char)  # открывающая скобка кладётся в стек
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()  # удаляем последнюю открывающую скобку

    return not stack  # True, если стек пустой


class PrintQueue:
    def __init__(self):
        self.queue = deque()

    def add_job(self, job):
        """Добавляем задачу в очередь"""
        self.queue.append(job)

    def process_job(self):
        """Обрабатываем задачу из начала очереди"""
        if self.queue:
            job = self.queue.popleft()
            print(f"Обрабатывается задача: {job}")
        else:
            print("Очередь пуста")

    def show_queue(self):
        """Показать все задачи в очереди"""
        print("Текущая очередь:", list(self.queue))


def is_palindrome(sequence):
    """Проверяет, является ли последовательность палиндромом"""
    dq = deque(sequence)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():  # сравниваем первый и последний элементы
            return False
    return True


if __name__ == "__main__":
    # 1. Скобки
    expr = "{[()()]}"
    print(f"{expr} сбалансировано? -> {is_balanced_brackets(expr)}")

    # 2. Очередь печати
    pq = PrintQueue()
    pq.add_job("Документ 1")
    pq.add_job("Документ 2")
    pq.show_queue()
    pq.process_job()
    pq.show_queue()

    # 3. Палиндром
    seq = "мир или рим"
    print(f"{seq} это палиндром? -> {is_palindrome(seq)}")
    seq = "привет"
    print(f"{seq} это палиндром? -> {is_palindrome(seq)}")

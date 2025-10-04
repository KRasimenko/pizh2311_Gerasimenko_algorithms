from collections import deque
from typing import Deque


def is_balanced_brackets(s: str) -> bool:
    """
    Проверка сбалансированности скобок, использует стек на list.
    Пример: "{[()]}" -> True
    Сложность: O(n) по времени, O(n) по памяти.
    """
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack


def print_queue_simulation(tasks: list, process_time: float = 0.0) -> None:
    """
    Симуляция очереди задач печати с deque.
    Enqueue: append (O(1)), Dequeue: popleft (O(1))
    """
    dq: Deque[str] = deque(tasks)
    while dq:
        task = dq.popleft()  # O(1)
        print("Processing:", task)
        if process_time:
            import time
            time.sleep(process_time)


def is_palindrome_sequence(seq) -> bool:
    """
    Проверка палиндрома с использованием deque.
    Сложность: O(n)
    """
    dq = deque(seq)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


if __name__ == "__main__":
    print("Баланс скобок:")
    tests = ["{[()]}", "{[(])}", "(()", ""]
    for t in tests:
        print(t, "->", is_balanced_brackets(t))

    print("\nСимуляция очереди печати:")
    tasks = ["doc1.pdf", "photo.jpg", "report.docx"]
    print_queue_simulation(tasks, process_time=0)  # process_time можно поставить >0

    print("\nПалиндромы:")
    seqs = ["radar", "hello", [1, 2, 3, 2, 1], [1, 2, 3]]
    for s in seqs:
        print(s, "->", is_palindrome_sequence(s))

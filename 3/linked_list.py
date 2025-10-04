from typing import Any, Iterator, Optional


class Node:
    """Узел связного списка."""
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional["Node"] = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """Простой односвязный список с хвостом (tail)."""

    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size = 0  

    def insert_at_start(self, data: Any) -> None:
        """Вставка в начало — O(1)."""
        # O(1)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:  # если был пустой список
            self.tail = new_node
        self._size += 1

    def insert_at_end(self, data: Any) -> None:
        """Вставка в конец — O(1) благодаря хвосту (tail)."""
        # O(1)
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def delete_from_start(self) -> Optional[Any]:
        """Удаление из начала — O(1). Возвращает удалённые данные или None."""
        # O(1)
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next
        if self.head is None:  # если список стал пуст
            self.tail = None
        self._size -= 1
        return removed.data

    def traversal(self) -> None:
        """Печать всех элементов в порядке следования — O(n)."""
        # O(n)
        cur = self.head
        out = []
        while cur:
            out.append(str(cur.data))
            cur = cur.next
        print(" -> ".join(out) + " -> None")

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next


if __name__ == "__main__":
    
    ll = LinkedList()
    ll.insert_at_start(3)
    ll.insert_at_start(2)
    ll.insert_at_start(1)  # 1 -> 2 -> 3
    print("После insert_at_start:")
    ll.traversal()

    ll.insert_at_end(4)
    ll.insert_at_end(5)  # 1 -> 2 -> 3 -> 4 -> 5
    print("После insert_at_end:")
    ll.traversal()

    removed = ll.delete_from_start()  # удаляет 1
    print("Удалено:", removed)
    ll.traversal()
    print("Длина:", len(ll))

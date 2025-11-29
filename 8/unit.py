import unittest

from heap import Heap
from heapsort import heapsort_inplace
from priority_queue import PriorityQueue


class TestHeapAndPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.array = [5, 3, 8, 1, 2, 7]

    # Тестирование кучи
    def test_heap_insert_and_extract_min(self):
        heap = Heap(is_min=True)
        for val in self.array:
            heap.insert(val)
        # Проверка свойства min-кучи
        for i in range(len(heap.data)):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(heap.data):
                self.assertLessEqual(heap.data[i], heap.data[left])
            if right < len(heap.data):
                self.assertLessEqual(heap.data[i], heap.data[right])
        # Проверка извлечения элементов по возрастанию
        sorted_array = sorted(self.array)
        extracted = [heap.extract() for _ in range(len(self.array))]
        self.assertEqual(extracted, sorted_array)

    # Тестирование Heapsort in-place
    def test_heapsort_inplace(self):
        arr = self.array[:]
        sorted_arr = sorted(arr)
        heapsort_inplace(arr)
        self.assertEqual(arr, sorted_arr)

    # Тестирование PriorityQueue
    def test_priority_queue(self):
        pq = PriorityQueue()
        pq.enqueue("A", 5)
        pq.enqueue("B", 2)
        pq.enqueue("C", 4)
        # Проверка peek
        self.assertEqual(pq.peek(), "B")
        # Проверка извлечения по приоритету
        self.assertEqual(pq.dequeue(), "B")
        self.assertEqual(pq.dequeue(), "C")
        self.assertEqual(pq.dequeue(), "A")
        self.assertIsNone(pq.dequeue())  # Очередь пустая

    # Проверка свойства кучи после операций
    def test_heap_property_after_operations(self):
        heap = Heap(is_min=True)
        heap.build_heap(self.array)

        # Вставка
        heap.insert(0)
        for i in range(len(heap.data)):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(heap.data):
                self.assertLessEqual(heap.data[i], heap.data[left])
            if right < len(heap.data):
                self.assertLessEqual(heap.data[i], heap.data[right])
        # Извлечение
        heap.extract()
        for i in range(len(heap.data)):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(heap.data):
                self.assertLessEqual(heap.data[i], heap.data[left])
            if right < len(heap.data):
                self.assertLessEqual(heap.data[i], heap.data[right])


if __name__ == "__main__":
    unittest.main()

import unittest

from hash_table_chaining import (HashTableChaining, HashTableDouble,
                                    HashTableLinear)


class TestHashTables(unittest.TestCase):

    # Тесты для метода цепочек
    def test_chaining_insert_and_find(self):
        """Проверка добавления и поиска в HashTableChaining"""
        ht = HashTableChaining()
        ht.insert("apple", 10)
        ht.insert("banana", 20)
        self.assertEqual(ht.find("apple"), 10)
        self.assertEqual(ht.find("banana"), 20)
        self.assertIsNone(ht.find("cherry"))  # нет такого ключа

    def test_chaining_collision(self):
        """Проверка обработки коллизий в HashTableChaining"""
        ht = HashTableChaining(size=2)  # малый размер повышает шанс коллизий
        ht.insert("a", 1)
        ht.insert("b", 2)
        # Оба ключа должны быть доступны
        self.assertEqual(ht.find("a"), 1)
        self.assertEqual(ht.find("b"), 2)

    def test_chaining_resize(self):
        """Проверка увеличения размера таблицы при переполнении"""
        ht = HashTableChaining(size=2)
        for i in range(5):  # вызовет увеличение размера
            ht.insert(f"k{i}", i)
        self.assertGreaterEqual(ht.size, 4)  # таблица увеличилась
        self.assertEqual(ht.find("k0"), 0)

    # Тесты для линейного пробирования
    def test_linear_insert_and_find(self):

        """Проверка добавления и поиска в HashTableLinear"""
        ht = HashTableLinear()
        ht.insert("apple", 10)
        ht.insert("banana", 20)
        self.assertEqual(ht.find("apple"), 10)
        self.assertEqual(ht.find("banana"), 20)
        self.assertIsNone(ht.find("cherry"))

    def test_linear_collision(self):
        """Проверка обработки коллизий в HashTableLinear"""
        ht = HashTableLinear(size=3)
        # Подбираем слова с одинаковым хешом вручную
        keys = ["a", "b", "c"]
        for i, k in enumerate(keys):
            ht.insert(k, i)
        # Проверим, что все вставились и доступны
        for i, k in enumerate(keys):
            self.assertEqual(ht.find(k), i)

    def test_linear_overflow(self):
        """Проверка переполнения таблицы при линейном пробировании"""
        ht = HashTableLinear(size=2)
        ht.insert("a", 1)
        ht.insert("b", 2)
        with self.assertRaises(Exception):  # таблица переполнена
            ht.insert("c", 3)

    # Тесты для двойного хеширования
    def test_double_insert_and_find(self):

        """Проверка добавления и поиска в HashTableDouble"""
        ht = HashTableDouble()
        ht.insert("apple", 10)
        ht.insert("banana", 20)
        self.assertEqual(ht.find("apple"), 10)
        self.assertEqual(ht.find("banana"), 20)

    def test_double_collision(self):
        """Проверка коллизий в HashTableDouble"""
        ht = HashTableDouble(size=3)
        keys = ["a", "b", "c"]
        for i, k in enumerate(keys):
            ht.insert(k, i)
        for i, k in enumerate(keys):
            self.assertEqual(ht.find(k), i)

    def test_double_overflow(self):
        """Проверка переполнения таблицы при двойном хешировании"""
        ht = HashTableDouble(size=2)
        ht.insert("a", 1)
        ht.insert("b", 2)
        with self.assertRaises(Exception):  # таблица переполнена
            ht.insert("c", 3)


if __name__ == "__main__":
    pc_info = """
    Конфигурация ПК:
    - Процессор: 11th Gen Intel(R) Core(TM) i5-1155G7 @ 2.50 GHz
    - Оперативная память: 16,0 ГБ (доступно: 15,8 ГБ)
    - Тип системы: 64-разрядная операционная система, процессор x64
    - ОС: Windows 11 Pro
    - Версия: 24H2
    - Сборка ОС: 26100.4946
    - Python: 3.13.3
    """
    unittest.main()

import unittest
import random
import string
import io
import sys

from kmp_search import kmp
from z_function import z_func
from string_matching import boyer_moore


def naive_search(text, pattern):
    """Эталонный (наивный) поиск"""
    res = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            res.append(i)
    return res


def run_kmp(pattern, text):
    """Запуск KMP с перехватом print"""
    buffer = io.StringIO()
    sys.stdout = buffer
    kmp(pattern, text)
    sys.stdout = sys.__stdout__

    output = buffer.getvalue().strip()
    if not output:
        return []
    return list(map(int, output.split()))


def run_z(pattern, text):
    """Запуск Z-алгоритма"""
    s = pattern + '#' + text
    z = z_func(s)
    p_len = len(pattern)

    res = []
    for i in range(p_len + 1, len(s)):
        if z[i] == p_len:
            res.append(i - p_len - 1)
    return res


class TestStringMatching(unittest.TestCase):

    def check_all(self, text, pattern):
        expected = naive_search(text, pattern)

        kmp_res = run_kmp(pattern, text)
        z_res = run_z(pattern, text)
        bm_res = boyer_moore(text, pattern)

        self.assertEqual(kmp_res, expected)
        self.assertEqual(z_res, expected)
        self.assertEqual(bm_res, expected)

    def test_random_strings(self):
        for _ in range(10):
            text = ''.join(random.choice(string.ascii_lowercase) for _ in range(50))
            pattern = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            self.check_all(text, pattern)

    def test_periodic_strings(self):
        text = "abc" * 20
        pattern = "abc"
        self.check_all(text, pattern)

        pattern = "bca"
        self.check_all(text, pattern)

    def test_repeated_characters(self):
        text = "aaaaaaabaaaaaa"
        pattern = "aaa"
        self.check_all(text, pattern)

    def test_pattern_not_found(self):
        text = "abcdefg"
        pattern = "xyz"
        self.check_all(text, pattern)

    def test_pattern_equals_text(self):
        text = "algorithm"
        pattern = "algorithm"
        self.check_all(text, pattern)

    def test_pattern_longer_than_text(self):
        text = "short"
        pattern = "verylongpattern"
        self.check_all(text, pattern)


if __name__ == '__main__':
    unittest.main()

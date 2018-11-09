from unittest import TestCase
from decorators import test_cases, add_tests
from functions_to_test import f1, f2, f3
import unittest

test_input = [
    [
        f1,
        [1],
        2
    ],
    [
        f2,
        [2],
        3
    ],
    [
        f3,
        [1, 2],
        False
    ]
]


class TestSuit(TestCase):
    def test_f1(self):
        a = 1
        self.assertEqual(f1(a), 2)


TestSuit = add_tests(test_cases(test_input))(TestSuit)

unittest.main()

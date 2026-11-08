import unittest

from generator import parity_generator


class TestGenerator(unittest.TestCase):

    def test_parity_generator(self):
        gen = parity_generator()

        self.assertEqual(next(gen), "Парне")
        self.assertEqual(next(gen), "Непарне")
        self.assertEqual(next(gen), "Парне")


if __name__ == "__main__":
    unittest.main()
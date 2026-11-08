
import unittest
from io import StringIO
from contextlib import redirect_stdout

from strings import print_string, check_case, uppercase_letters


class TestStrings(unittest.TestCase):

    def test_print_string(self):
        output = StringIO()

        with redirect_stdout(output):
            print_string("Hello")

        self.assertEqual(output.getvalue().strip(), "Hello")

    def test_check_case(self):
        output = StringIO()

        with redirect_stdout(output):
            check_case("HELLO")

        self.assertEqual(
            output.getvalue().strip(),
            "All letters are uppercase"
        )

    def test_uppercase_letters(self):
        self.assertEqual(
            uppercase_letters("smogtether"),
            list("SMOGTETHER")
        )

    def test_invalid_type(self):
        output = StringIO()

        with redirect_stdout(output):
            print_string(123)

        self.assertIn("Error", output.getvalue())


if __name__ == "__main__":
    unittest.main()

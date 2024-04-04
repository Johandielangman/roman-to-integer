import unittest
from main import Solution

# Create a list of tests to run
# Each test is a tuple with the first element being a dictionary of input arguments
# and the second element being the expected output
tests = [
    [{"s": "I"}, 1],
    [{"s": "II"}, 2],
    [{"s": "III"}, 3],
    [{"s": "IV"}, 4],
    [{"s": "V"}, 5],
    [{"s": "VI"}, 6],
    [{"s": "VII"}, 7],
    [{"s": "VIII"}, 8],
    [{"s": "IX"}, 9],
    [{"s": "X"}, 10],
    [{"s": "LVIII"}, 58],
    [{"s": "MCMXCIV"}, 1994],
]


class TestSolution(unittest.TestCase):
    def test_romanToInt(self):
        for test in tests:
            input, expected = test
            with self.subTest(input=input, expected=expected):
                s = Solution()
                self.assertEqual(s.romanToInt(**input), expected)


if __name__ == "__main__":
    unittest.main()

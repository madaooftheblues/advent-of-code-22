import unittest
from day_6 import first_marker


class TestAoC(unittest.TestCase):
    def test_first_marker(self):
        self.assertEqual(first_marker(4, "bvwbjplbgvbhsrlpgdmjqwftvncz"), 5)
        self.assertEqual(first_marker(4, "nppdvjthqldpwncqszvftbrmjlhg"), 6)
        self.assertEqual(first_marker(4, "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 10)
        self.assertEqual(first_marker(4, "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 11)
        self.assertEqual(first_marker(4, "mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 7)
        self.assertEqual(first_marker(4, ""), -1)
        self.assertEqual(first_marker(1, "a"), 1)
        self.assertEqual(first_marker(4, "a"), -1)
        self.assertEqual(first_marker(4, "aaa"), -1)
        self.assertEqual(first_marker(14, "bvwbjplbgvbhsrlpgdmjqwftvncz"), 23)
        self.assertEqual(first_marker(14, "nppdvjthqldpwncqszvftbrmjlhg"), 23)
        self.assertEqual(first_marker(14, "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 29)
        self.assertEqual(first_marker(14, "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 26)
        self.assertEqual(first_marker(14, "mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 19)


if __name__ == "__main__":
    unittest.main()

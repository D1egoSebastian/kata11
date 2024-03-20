import unittest
from main import sort_it
from main import compare_chars

class test_sort_it(unittest.TestCase):
      def test_case1(self):
          string = "A"
          expected = "a"
          self.assertEqual(sort_it(string), expected)

      def test_case2(self):
          string = "A!@#"
          expected = "a"
          self.assertEqual(sort_it(string), expected)

      def test_case3(self):
          string = "When not studying nuclear physics, Bambi likes to play beach volleyball."
          expected = "aaaaabbbbcccdeeeeeghhhiiiiklllllllmnnnnooopprsssstttuuvwyyyy"
          self.assertEqual(sort_it(string), expected)


if __name__ == '__main__':
    unittest.main()


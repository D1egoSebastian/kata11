import unittest
from main import sort_it

class test_sort_it(unittest.TestCase):

    def test_sort1(self):
        string = "A"
        expected = 'a'
        self.assertEqual(sort_it(string), expected)

    def test_sort2(self):
        string = "A!@#"
        expected = "a"
        self.assertEqual(sort_it(string), expected)

    def test_sort3(self):
        string = "When not studying nuclear physics, Bambi likes to play beach volleyball."
        expected = "aaaaabbbbcccdeeeeeghhhiiiiklllllllmnnnnooopprsssstttuuvwyyyy"
        self.assertEqual(sort_it(string), expected)

if __name__ == '__main__':
    unittest.main()


import unittest
import add

class SampleTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add.add(1, 2), 3)
#         self.assertEqual(add.add(1, 2), 5)

if __name__ == "__main__":
    unittest.main()

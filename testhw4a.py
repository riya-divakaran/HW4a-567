import unittest
import Hw04a

class Test_567hw4a(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Hw04a.getComms('riya-divakaran'), 587)
    def test_2(self):
        self.assertEqual(Hw04a.getComms('Riya-Divakaran'),"Username is not valid")
    def test_3(self):
        self.assertEqual(Hw04a.getComms(1289),"Username is not valid")
if __name__ == '__main__':
    unittest.main()
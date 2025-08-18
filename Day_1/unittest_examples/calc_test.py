import unittest
import Day_1.unittest_examples.calc as calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)
        with self.assertRaises(TypeError) as te:
            calc.add(2, "3")
        exception = te.exception
        self.assertIsInstance(exception, TypeError)
        self.assertRegex(str(exception), "unsupported operand type")


    def test_sub(self):
        self.assertEqual(calc.sub(6, 4), 2)
        self.assertNotEqual(calc.sub(9, 2), 2)

    def test_mul(self):
        self.assertEqual(calc.mul(2, 3), 6)
        self.assertTrue(calc.mul(9, 2)==18)

    
    def test_div(self):
        self.assertEqual(calc.div(6, 3), 2)
        self.assertIsInstance(calc.div(8, 4), float)


if __name__ == "__main__":
    unittest.main(verbosity=2)
import sys
import unittest
import Day_2.more_calc as calc

VALUE = 2
sys.stdout = open("result.txt", "w", encoding="utf-8")

class TestBasicCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("=" * 25)
        print("Prepare data for testing")
        print("=" * 25)      
    
    @classmethod
    def tearDownClass(cls) -> None:
        print("=" * 30)
        print("Close all connections and clear temporary values")
        print("=" * 30)

    @unittest.skipIf(VALUE < 3, "Temporary skip test_add")
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)
        with self.assertRaises(TypeError) as te:
            calc.add(2, "3")

    def test_sub(self):
        self.assertEqual(calc.sub(6, 4), 2)
        self.assertNotEqual(calc.sub(9, 2), 2)

    def test_mul(self):
        self.assertEqual(calc.mul(2, 3), 6)
        self.assertTrue(calc.mul(9, 2)==18)
    
    def test_div(self):
        self.assertEqual(calc.div(6, 3), 2)
        self.assertIsInstance(calc.div(8, 4), float)


@unittest.skip("Waiting for realization")
class TestMoreCalc(unittest.TestCase):
    """ test MoreCalc class"""
    def test_sqrt(self):
        """ check that sqrt function works right"""
        self.assertEqual(calc.sqrt(25), 5.0)
        self.assertIsInstance(calc.sqrt(9), float)



def main(out=sys.stdout, verbosity=2):
    """Runner example"""

    loader = unittest.TestLoader()

    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == "__main__":
    # main()
    unittest.main()
    

import sys
import unittest
import more_calc_test as mct


def main(out=sys.stdout, verbosity=2):
    loader = unittest.TestLoader()

    suite = loader.loadTestsFromModule(mct)
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == "__main__":
    with open("result2.txt", "w", encoding="utf-8") as file:
        main(file)
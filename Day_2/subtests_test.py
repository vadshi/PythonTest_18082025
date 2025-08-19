import unittest

class TestContainer(unittest.TestCase):
    longMessage = True
    tests_dict = {
        "foo": [1, 1],
        "bar": [1, 2],
        "baz": [5, 5]
    }

    def test_equality(self):
        for name, (a, b) in self.tests_dict.items():
            with self.subTest(name=name):
                self.assertEqual(a, b, name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
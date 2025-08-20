import unittest
import Day_2.Solutions.encode_decode as ed


class TestEncodeDecode(unittest.TestCase):
    def test_decode(self):
        """ Test decode """
        self.assertEqual(ed.decode('070411111426152419071413'), 'hello python')
        self.assertRaises(TypeError, ed.decode, 110411111426152419071413)
        self.assertRaises(ValueError, ed.decode, 'hello python')
        
        
    def test_encode(self):
        """ Test encode """
        self.assertEqual(ed.encode('hello python'), '070411111426152419071413')
        self.assertRaises(TypeError, ed.encode, 110411111426152419071413)
        self.assertRaises(ValueError, ed.encode, '110411111426152419071413')
            


if __name__ == "__main__":
    unittest.main(verbosity=2)
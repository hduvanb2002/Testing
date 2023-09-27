import unittest
from nose2.tools import params
from removeV import removeVowels

class TestStringMethods(unittest.TestCase):
    @params(("Caballo","Cbll"),("Yegua","Yg"),("Camello","Cmll"),("Loro","Lr"))
    def test_removeVowels(self, input_str, expected):
        # self.assertEqual(removeVowels(input_str), expected)
        assert removeVowels(input_str) == expected

if __name__ == '__main__':
    import nose2
    nose2.main()

import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is not False")

        b = False

        self.assertTrue(b, "b is not True")


    def test_assertEqual(self):

        a = "Test"

        b = "Test"

        self.assertNotEqual(a,b, msg= "'a' is not equal to 'b'" )


if __name__ == '__main__':
    unittest.main(verbosity=2)
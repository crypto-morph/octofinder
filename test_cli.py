from ctypes import util
import utils
import unittest

class TestAutoOctoFinder(unittest.TestCase):

    def test_word_check(self):

        with self.assertRaises(TypeError):
            utils.check(1234)
        
        # Standard cases.
        with self.subTest(0):
            self.assertFalse(utils.check('ABCDEFGH'))
            self.assertFalse(utils.check('LLLLLLLL'))
            self.assertFalse(utils.check('BILLIONS'))

        # Fail cases.
        with self.subTest(1):
            # Len != 8.
            self.assertTrue(utils.check('ABCDEFH')) 
            self.assertTrue(utils.check('ABCDEFHZZZZZZZZZZZ')) 
            self.assertTrue(utils.check('AZ')) 

            # Non-Alpha Values.
            self.assertTrue(utils.check('ABCDEFH2'))
            self.assertTrue(utils.check('B_DEFH!'))
            self.assertTrue(utils.check('B@$%^H!'))

            # Empty.
            self.assertTrue(utils.check(''))

    def test_find_difference(self):

        with self.subTest('Type Assert Checks'):
            with self.assertRaises(TypeError):
                utils.findDifference("A","b")
            with self.assertRaises(TypeError):
                utils.findDifference("1","2")
                
        with self.subTest('Standard Case'):
            self.assertEqual(utils.findDifference(ord('A'),ord('B')), 1)
            self.assertEqual(utils.findDifference(ord('A'),ord('Z')), 25)

        with self.subTest('Fail Case'):
            self.assertNotEqual(utils.findDifference(ord('Z'),ord('A')), 24)
            self.assertNotEqual(utils.findDifference(ord('G'),ord('Z')), 5)
                
        
if __name__ == '__main__':
    unittest.main()






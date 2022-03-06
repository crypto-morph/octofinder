import utils
import unittest
import yaml

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
    
    def test_calculate_words(self):
        
        words = set() 
        test_dir = './test_data/'

        with open("words.txt") as f:
            words = set(f.read().splitlines())
            f.close()

        with self.subTest('Standard Cases'):
            stream = open(test_dir + 'test_billions.yml','r')
            expected_result = yaml.safe_load(stream)
            stream.close()
            actual_result = utils.calculateWords('BILLIONS', words, utils.default_turns)
            self.assertEqual(
                actual_result,
                expected_result)

            stream = open(test_dir + 'test_fakegrin_25.yml','r')
            expected_result = yaml.safe_load(stream)
            stream.close()
            actual_result = utils.calculateWords('FAKEGRIN', words, 25)
            self.assertEqual(
                actual_result,
                expected_result)

if __name__ == '__main__':
    unittest.main()

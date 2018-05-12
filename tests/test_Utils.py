import unittest

from Utils import Utils



class Tester(unittest.TestCase):
    def test_bow_to_vec(self):
    	vocab = ["a", "simple", "vocab"]
    	bow = ["simple", "a"]
    	vec = Utils.bow_to_vec(vocab, bow)
    	self.assertEqual(vec, [1,1,0])

    	# handles OOV word
    	bow = ["simple", "a", "OOV"]
    	vec = Utils.bow_to_vec(vocab, bow)
    	self.assertEqual(vec, [1,1,0])
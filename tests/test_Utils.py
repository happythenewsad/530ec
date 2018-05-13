import unittest

from Utils import Utils
from PorterStemmer import PorterStemmer

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


    def test_stem(self):
    	words = "dogs walking cat".split()
    	porter = PorterStemmer()
    	result = Utils.stem(porter,words)
    	#print(result)
    	self.assertEqual(result, ["dog", "walk", "cat"])
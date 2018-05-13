pearson is in evaluate.py already

-1 if no correlated
1 if perfectly correlated



 a simple unsupervised baseline can be the cosine similarity between the bag-of-words representation sentence. You need to implement this simple baseline as a sanity check. This should reach a Pearson correlation of about 0.35 on the test set.

 start here: look at how many unique words are in train.


 seems like the STS wiki is a good resource

 find eval script in google groups?

python3 evaluate.py --goldfile data/en-test.txt --predfile simple_baseline_test.txt 
Namespace(goldfile='data/en-test.txt', predfile='simple_baseline_test.txt')
4.200668258079036 average for 10 with gs 5.0
0.5801012526148436 average for 11 with gs 0.0
Performance: 0.7112355581576367


3.2.6: vectorize sentences using inter-sentence vocabulary such that index 1 of sentence A is favoried if index 1 of sentance B conatins a synonym

# how many unique words are there in train?
#19850


TODO:
lemmatization - stemming etc
BOW but with word2vec synonyms?
POS - favor pairs that have same POS sequence
	edit distance between POS sequences?
	intersection of POS tags as a feature?

alignments
Hungarian algorithm (Kuhn, 1955) implemented in the SEMILAR Toolkit (Rus et al., 2013).


sent2vec

Good signal in BOW, but am going to try PCA, random forest, TFIDF vocab - look for least common?


random forest - only class prediction?

Q how do their classifiers map to 0-5?
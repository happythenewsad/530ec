pearson is in evaluate.py already

-1 if no correlated
1 if perfectly correlated



 a simple unsupervised baseline can be the cosine similarity between the bag-of-words representation sentence. You need to implement this simple baseline as a sanity check. This should reach a Pearson correlation of about 0.35 on the test set.

 start here: look at how many unique words are in train.


 seems like the STS wiki is a good resource

 find eval script in google groups?

(no porter)
python3 evaluate.py --goldfile data/en-test.txt --predfile simple_baseline_test.txt 
Namespace(goldfile='data/en-test.txt', predfile='simple_baseline_test.txt')
4.200668258079036 average for 10 with gs 5.0
0.5801012526148436 average for 11 with gs 0.0
Performance: 0.7112355581576367

(with porter)
python3 evaluate.py --goldfile data/en-test.txt --predfile simple_baseline_test.txt 
Namespace(goldfile='data/en-test.txt', predfile='simple_baseline_test.txt')
4.258631077743398 average for 10 with gs 5.0
0.5844721920144405 average for 11 with gs 0.0
Performance: 0.7322417877328065



KRM with porter, val:
 python3 evaluate.py --goldfile data/en-val.txt --predfile val_y_pred.txt
Namespace(goldfile='data/en-val.txt', predfile='val_y_pred.txt')
3.9014097230056395 average for 128 with gs 5.0
0.5554145073289327 average for 119 with gs 0.0
Performance: 0.5793278273995568

KRM with porter, POS, val:
3.785513251997569 average for 128 with gs 5.0
0.6648770896795969 average for 79 with gs 0.0
Performance: 0.5935844434325268

KRM with porter, POS, test:
Performance: 0.7289798024103769



3.2.6: vectorize sentences using inter-sentence vocabulary such that index 1 of sentence A is favoried if index 1 of sentance B conatins a synonym

# how many unique words are there in train?
#19850

'ADJ',
 'ADP',
 'ADV',
 'CCONJ',
 'DET',
 'INTJ',
 'NOUN',
 'NUM',
 'PART',
 'PRON',
 'PROPN',
 'PUNCT',
 'SPACE',
 'SYM',
 'VERB',
 'X'

entities:
0,
 378,
 379,
 381,
 382,
 383,
 384,
 385,
 386,
 388,
 389,
 390,
 391,
 392,
 393,
 394,
 448,


TODO:

BOW but with word2vec synonyms? no.
POS - favor pairs that have same POS sequence
	edit distance between POS sequences?
	intersection of POS tags as a feature?
NER

features:
	absolute difference in POS counts
	absolute difference in entity counts?


alignments
Hungarian algorithm (Kuhn, 1955) implemented in the SEMILAR Toolkit (Rus et al., 2013).


sent2vec

Good signal in BOW, but am going to try PCA, random forest, TFIDF vocab - look for least common?


random forest - only class prediction?

Q how do their classifiers map to 0-5?
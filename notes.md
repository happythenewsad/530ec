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

porter, POS, ner, val:
Performance: 0.5940330229859941

porter, POS, ner, test:
Performance: 0.7290702218576988

porter, POS, ner,, RBF val:
Performance: 0.5991922333329962

porter, POS, ner,, RBF test:
Performance: 0.7406295258551159


porter, POS, ner,, RBF .5 alpha val:
Performance: 0.5998956663978675

porter, POS, ner,, RBF .5 alpha test:
Performance: 0.740929894376735


porter, POS, ner,, RBF .5 alpha .8 gamma val:
Performance: 0.6072420908867939

porter, POS, ner,, RBF .5 alpha .8 gamma test:
Performance: 0.7382601961971023

porter, POS, ner,, RBF .5 alpha .4 gamma val:
Performance: 0.6072420908867939






# how many unique words are there in train?
#19850

RF, POS, NER, est=10, val:
Performance: 0.5713921178463931

RF, POS, NER, est=10, test:
Performance: 0.5923193692438096

RF, POS, NER, est=20, val:
Performance: 0.5750611048755191

RF, POS, NER, est=20, test:
Performance: 0.6009647642732455

RF, POS, NER, est=40, val:
Performance: 0.5808596287306547

RF, POS, NER, est=40, test:
Performance: 0.6084645212408156

RF, POS, NER, est=80, val:
Performance: 0.5848848747796371

RF, POS, NER, est=80, test:
Performance: 0.6108458768960248

RF, POS, NER, est=160, val:
Performance: 0.5857055518307862

RF, POS, NER, est=160, test:
Performance: 0.6109141599122807



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


3.2.6: vectorize sentences using inter-sentence vocabulary such that index 1 of sentence A is favoried if index 1 of sentance B conatins a synonym

analysis
========
most important RF feature was last one: 7.06082346e-01
 aka cosine


indicates further improvements using synonyms
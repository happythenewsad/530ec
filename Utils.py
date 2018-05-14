from scipy import spatial
from PorterStemmer import PorterStemmer
from sklearn.feature_extraction import DictVectorizer
import spacy

class Utils:
	# order of vocab matters. it has been deduped
	@staticmethod
	def bow_to_vec(vocab, bow):
		vec = list((0,) * len(vocab))
		for word in bow:
			vocab_index = None
			try:
				vocab_index = vocab.index(word)
			except:
				None
			if vocab_index is not None:
				vec[vocab_index] += 1
		return vec

	# returns unique sorted vocab
	@staticmethod
	def file_to_vocab(file, stem=True):
		porter = PorterStemmer()
		with open("data/en-train.txt",'r') as f1:
			train = f1.readlines()
			words = []

			for ln in train:
				segments = ln.split('\t')
				first_seg = segments[0].split()
				second_seg = segments[1].split()

				if stem:
					first_seg = Utils.stem(porter, first_seg)
					second_seg = Utils.stem(porter, second_seg)

				words.extend(first_seg)
				words.extend(second_seg)

		unique_words = list(set(words))
		unique_words.sort()
		return unique_words


	@staticmethod
	def normalized_abs_diff(featName, featDict):
		if (('first_'+featName) in featDict) and (('second_'+featName) in featDict):
			doc1val = featDict['first_'+featName]
			doc2val = featDict['second_'+featName]
			return abs(doc1val - doc2val)/(doc1val + doc2val)
		return float(0)

	@staticmethod
	def gen_pos_ner_features(infile):
		rows = []
		pos_types = ['ADJ','ADV','NOUN','NUM','PROPN','VERB']
		ent_types = ['PERSON', 'NORP','ORG','GPE', 'LOC', 'PRODUCT', 'EVENT', 'WORK_OF_ART',
			'DATE', 'TIME', 'LANGUAGE', 'MONEY', 'QUANTITY', 'ORDINAL', 'CARDINAL']

		nlp = spacy.load('en_core_web_sm')

		with open(infile,'r') as f1:
			lines = f1.readlines()
			#lines = lines[:10]
			for idx,line in enumerate(lines):
				if idx % 1000 == 0:
					print(idx)
				posdict = {}
				row_features = {}
				segments = line.split('\t')
				first_seg = segments[0]
				second_seg = segments[1]

				doc1 = nlp(first_seg)
				doc2 = nlp(second_seg)

				for token in doc1:
				    if token.pos_ in pos_types:
				        if 'first_'+token.pos_ in posdict:
				            posdict['first_'+token.pos_] += 1
				        else:
				            posdict['first_'+token.pos_] = 1
				            
				for token in doc2:
				    if token.pos_ in pos_types:
				        if 'second_'+token.pos_ in posdict:
				            posdict['second_'+token.pos_] += 1
				        else:
				            posdict['second_'+token.pos_] = 1


				for ent in doc1.ents:
					if ent.label_ in ent_types:
						if 'first_'+ent.label_ in posdict:
							posdict['first_'+ent.label_] += 1
						else:
							posdict['first_'+ent.label_] = 1

				for ent in doc2.ents:
					if ent.label_ in ent_types:
						if 'second_'+ent.label_ in posdict:
							posdict['second_'+ent.label_] += 1
						else:
							posdict['second_'+ent.label_] = 1

				for ent in ent_types:
					row_features['abs_diff_'+ent] = Utils.normalized_abs_diff(ent, posdict)

				for typ in pos_types:
					row_features['abs_diff_'+typ] = Utils.normalized_abs_diff(typ, posdict)

				#print(posdict, '------\n')
				rows.append(row_features)
    
		return rows  

	@staticmethod
	def gen_cosine_sim_feature(lines, vocab, stem=True):
		porter = PorterStemmer()
		results = []
		for idx, line in enumerate(lines):
		    segments = line.split('\t')
		    first_seg = segments[0].split()
		    second_seg = segments[1].split()

		    if stem:
		    	first_seg = Utils.stem(porter, first_seg)
		    	second_seg = Utils.stem(porter, second_seg)
		    
		    first_seg_vec = Utils.bow_to_vec(vocab, set(first_seg))
		    second_seg_vec = Utils.bow_to_vec(vocab, set(second_seg))
		    result = (1 - spatial.distance.cosine(first_seg_vec, second_seg_vec)) * 5
		    results.append(result)
		    
		    if idx % 1000 == 0:
		        print(idx, result)

		return results

	@staticmethod
	def extract_labels(inp):
		labels = []
		with open(inp,'r') as f1:
		    lines = f1.readlines()
		for idx, line in enumerate(lines):
		    segments = line.split('\t')
		    score = segments[-1].strip()
		    labels.append(float(score))
		return labels

	@staticmethod
	def gen_baseline_labels(inp, outp, vocab):
		with open(inp,'r') as f1:
		    lines = f1.readlines()
		    
		results = Utils.gen_cosine_sim_feature(lines, vocab)

		with open(outp, 'w') as f:      
		    for score in results:
		        f.write("{}\n".format(score)) 

    
    # convenience wrapper for Porter stemmer
	def stem(stemmer, words):
		return [stemmer.stem(word, 0,len(word)-1) for word in words]



# if __name__ == '__main__':
#     p = PorterStemmer()
#     if len(sys.argv) > 1:
#         for f in sys.argv[1:]:
#             infile = open(f, 'r')
#             while 1:
#                 output = ''
#                 word = ''
#                 line = infile.readline()
#                 if line == '':
#                     break
#                 for c in line:
#                     if c.isalpha():
#                         word += c.lower()
#                     else:
#                         if word:
#                             output += p.stem(word, 0,len(word)-1)
#                             word = ''
#                         output += c.lower()
#                 print output,
#             infile.close()


	# def readLabels(datafile):

	#     labels = []
	#     with open(datafile, 'r') as f:
	#         inputlines = f.read().strip().split('\n')

	#     for line in inputlines:
	#         hypo, hyper, label = line.split('\t')
	#         if label == 'True':
	#             labels.append(1)
	#         else:
	#             labels.append(0)

	#     return labels
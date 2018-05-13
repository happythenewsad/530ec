from scipy import spatial

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
	def file_to_vocab(file):
		with open("data/en-train.txt",'r') as f1:
		    train = f1.readlines()
		    words = []
		    
		    for ln in train:
		        segments = ln.split('\t')
		        first_seg = segments[0].split()
		        second_seg = segments[1].split()
		        words.extend(first_seg)
		        words.extend(second_seg)

		unique_words = list(set(words))
		unique_words.sort()
		return unique_words

	@staticmethod
	def gen_cosine_sim_feature(lines, vocab):
		results = []
		for idx, line in enumerate(lines):
		    segments = line.split('\t')
		    first_seg = segments[0].split()
		    second_seg = segments[1].split()
		    
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

    
    # CITATION: This function derived from external Porter source
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
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
	def gen_baseline_labels(inp, outp, vocab):
		with open(inp,'r') as f1:
		    val = f1.readlines()
		    
		results = []
		for idx, line in enumerate(val):
		    segments = line.split('\t')
		    first_seg = segments[0].split()
		    second_seg = segments[1].split()
		    
		    first_seg_vec = Utils.bow_to_vec(vocab, set(first_seg))
		    second_seg_vec = Utils.bow_to_vec(vocab, set(second_seg))
		    result = (1 - spatial.distance.cosine(first_seg_vec, second_seg_vec)) * 5
		    results.append(result)
		    
		    if idx % 100 == 0:
		        print(idx, result)        

		with open(outp, 'w') as f:      
		    for score in results:
		        f.write("{}\n".format(score)) 



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
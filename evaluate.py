import pprint
import argparse
import math
import numpy as np

from Utils import Utils
from scipy.stats import pearsonr

pp = pprint.PrettyPrinter()
parser = argparse.ArgumentParser()

parser.add_argument('--goldfile', type=str, required=True)
parser.add_argument('--predfile', type=str, required=True)


def main(args):
    with open(args.goldfile,'r') as f1:
        with open(args.predfile,'r') as f2:
            gold = f1.readlines()
            pred = f2.readlines()
            # http://alt.qcri.org/semeval2017/task1/
            # evaluation -- Pearson correlation
            gold = [float(g.split()[-1]) for g in gold]
            pred = [float(p.split()[-1]) for p in pred]
            debug5 = [pred[idx] for idx,g in enumerate(gold) if 5 == int(g)]
            debug0 = [pred[idx] for idx,p in enumerate(pred) if 0 == int(p)]
            print(np.mean(debug5), "average for", len(debug5),"with gs 5.0")
            print(np.mean(debug0), "average for", len(debug0),"with gs 0.0")

            # gold_and_pred = zip(gold,pred)
            # differences = [abs(x-y) for (x,y) in gold_and_pred]
            # max_idx = -1
            # mx = 0
            # for idx,elem in enumerate(differences):
            #     if elem > mx:
            #         max_idx = idx
            #         mx = elem
            # print(mx)
            # print(max_idx)

    # https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.pearsonr.html
    ret = pearsonr(gold,pred)[0]
        
    print("Performance:",ret)


if __name__ == '__main__':
    args = parser.parse_args()
    pp.pprint(args)
    main(args)

import sys
import pandas as pd
import matplotlib.pyplot as plt
#import my_progressbar
from my_progressbar import Progressbar
#import collections
from collections import Counter
genes = []
pli = []
with open('pli_scores.txt', 'r') as f_pl:
    head = f_pl.readline()
    for st in f_pl:
        stm = st[:-1].split('\t')
        genes.append(stm[1].upper())
        pli.append(stm[-1])
print(genes[0:4])
print(pli[0:4])

genes_pred = []
counter_no = {}
mybar = Progressbar(10, 81688/2)


counter = 0
#genes_sep = list(Counter(genes).keys())
#print(Counter(genes))
#df_pl = pd.DataFrame(index=genes)
df_pl = pd.DataFrame()

df_pl['gen'] = genes.copy()
df_pl['pli'] = pli.copy()
df_pl['mut'] = 0
#df_pl.drop(df_pl[df_pl['gen'] == 'C2ORF15'].index,axis=0,inplace=True)
df_pl.drop([2379],axis=0,inplace=True)
print(float(df_pl[df_pl['gen'] == 'C2ORF15']['pli']))
#df_pl.reset_index(inplace=True)
border = 0.8
dict_bord = {}
dict_bord[str(border)] = 0
#sys.exit()
with open('pred_filtr.vcf', 'r') as f_pred:
    head = f_pred.readline()
    for st in f_pred:
        mybar.next()
        stm = st[:-1].split('\t')
        gen = stm[-1].split('|')[1]
        gen = gen.upper()
        if not(gen in genes):
            counter += 1
            if gen in counter_no.keys():
                counter_no[gen] += 1
            else:
                counter_no[gen] = 1
        else:
            if float(df_pl[df_pl['gen'] == gen]['pli']) >= border:
                dict_bord[str(border)] += 1

        st = f_pred.readline()
print()
#for el in counter_no.items():
    #print(f'{el[0]} {el[1]}')
print(counter)
plt.bar(dict_bord.keys(),dict_bord.values())
print(counter)
print(dict_bord)
plt.show()

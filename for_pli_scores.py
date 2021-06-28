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
        pli.append(float(stm[-1]))
print(genes[0:4])
print(pli[0:4])
print('Количество генов в списке pli и pli:')
print(len(genes))
print(len(pli))
genes_ad = []
with open('gens_ad','r') as f_ad:
    for st in f_ad:
        genad = st[:-1]
        genes_ad.append(genad)
#print(genes_ad)

genes_ad_pli = []
pli_ad = []
#mybar0 = Progressbar(10,18226)

count = 0
#print(Counter(genes))
#print(Counter(genes_ad))
for i in range(len(genes)):

    if genes[i] in genes_ad:
        count += 1
        genes_ad_pli.append(genes[i])
        pli_ad.append(pli[i])
print(f'Всего генов AD: {len(genes_ad)}')
print(f'Количество генов AD, которые имеют pli: {count}')
#print(len(genes_ad_pli))
#print(len(pli_ad))
genes_pred = []






#genes_sep = list(Counter(genes).keys())
#print(Counter(genes))
#df_pl = pd.DataFrame(index=genes)
# df_pl = pd.DataFrame()
#
# #df_pl['gen'] = genes.copy()
# df_pl['gen'] = genes_ad_pli.copy()
# df_pl['pli'] = pli_ad.copy()
# df_pl['mut'] = 0
#df_pl.drop(df_pl[df_pl['gen'] == 'C2ORF15'].index,axis=0,inplace=True)

#df_pl.drop([2379],axis=0,inplace=True)
#print(float(df_pl[df_pl['gen'] == 'C2ORF15']['pli']))
mas_bord = []
el = 0

while el <= 0.9:
    mas_bord.append(el)
    el += 0.1
print(mas_bord)
dict_bord = {}

for border in mas_bord:
    n_mut = 0
    not_ad_gens = {}
    count_ad = 0
    mut_without_ad = 0
    all_gens = {}
    count_gens_ad = {}
    count_gens_ad_pli = {}
    count_ad_pli = 0
    mybar = Progressbar(10, 81688 / 2, name='border '+str(round(border,2))+' ')
    dict_bord[str(border)] = 0
    with open('pred_filtr.vcf', 'r') as f_pred:
        head = f_pred.readline()
        for st in f_pred:
            mybar.next()
            stm = st[:-1].split('\t')
            gen = stm[-1].split('|')[1]
            gen = gen.upper()
            if not(gen in all_gens.keys()):
                all_gens[gen] = 1
            else:
                all_gens[gen] += 1
            if not(gen in genes_ad): # !!!!!!!!!!!!!!!!!!!!!!!!!!!
                mut_without_ad += 1
                if gen in not_ad_gens.keys():
                    not_ad_gens[gen] += 1
                else:
                    not_ad_gens[gen] = 1
            else:
                if (gen in genes_ad_pli):
                    count_ad_pli += 1
                    if not (gen in count_gens_ad.keys()):
                        count_gens_ad_pli[gen] = 1
                    else:
                        count_gens_ad_pli[gen] += 1
                    if border < pli_ad[genes_ad_pli.index(gen)] <= border + 0.1:
                        dict_bord[str(border)] += 1
                else:
                    count_ad += 1
                    if not (gen in count_gens_ad.keys()):
                        count_gens_ad[gen] = 1
                    else:
                        count_gens_ad[gen] += 1

            st = f_pred.readline()
            n_mut += 1

count_ad += 1
print()

print(f'Мутации, которые НЕ в ad генах: {mut_without_ad}')
print(f'Кол-во ГЕНОВ с предсказаниями, НЕ попавших в ad: {len(not_ad_gens.keys())}')
print(f'count ad, мутации, которые в ad генах БЕЗ pli: {count_ad}')
print(f'Кол-во генов с предсказаниями, попавших в ad БЕЗ pli : {len(count_gens_ad.keys())}')
print(f'count ad, мутации, которые в ad генах С pli: {count_ad_pli}')
print(f'Кол-во генов с предсказаниями, попавших в ad С pli : {len(count_gens_ad_pli.keys())}')
print(f'Всего генов с предсказаниями: {len(all_gens.keys())}')
print(f'Всего мутаций: {n_mut}')
#for el in not_ad_gens.items():
    #print(f'{el[0]} {el[1]}')
x_pli = []
y_pli = []
for key in dict_bord.keys():
    x_pli.append(str(round(float(key),2)))
    y_pli.append(dict_bord[key])
print(x_pli)
print(y_pli)
plt.bar(x_pli,y_pli)
#print(counter)
#print(dict_bord)
plt.xlabel('PLI score')
plt.ylabel('number of mutations')
plt.title('Location of mutation with different predictions \n in AD genes with different PLI scores')
plt.show()

#count ad: 4072 в ad-генах с pli-скором
#counter: 36773 не в ad-генах с pli-скором.

# {'0.9': 8908}
# {'0.8': 9879}
# {'0.5': 12157}
# {'0.3': 13717}

# 1533 - Мутации из списка pli, которые являются ad.
# 1610 - генов ad.


# Мутации, которые НЕ в ad генах: 36682 (36680)
# Кол-во ГЕНОВ с предсказаниями, НЕ попавших в ad: 9655
# count ad, мутации, которые в ad генах БЕЗ pli: 92
# Кол-во генов с предсказаниями, попавших в ad БЕЗ pli : 24
# count ad, мутации, которые в ad генах С pli: 4071 (4072!!)
# Кол-во генов с предсказаниями, попавших в ad С pli : 979
# Всего генов с предсказаниями: 10658
# Всего мутаций: 40844
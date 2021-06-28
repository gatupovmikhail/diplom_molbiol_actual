import matplotlib.pyplot as plt
import pandas as pd


with open('gens_ad', 'r') as f:
    gens_ad = f.read().split('\n')[:-1]
with open('gens_ar', 'r') as f:
    gens_ar = f.read().split('\n')[:-1]
with open('pred_filtr.vcf', 'r') as predict:
    zag = predict.readline()
    n_st = 0
    ad_count = 0
    ar_count = 0
    both_count = 0
    ost_count = 0
    list_ad = {}
    list_ar = {}
    list_adar = {}
    list_ost = {}
    for st in predict:
        n_st += 1
        if n_st % 2 == 1:
            gen = st[:-1].split('\t')[6].split('|')[1]
            fl = 0
            if gen in gens_ad:
                ad_count += 1
                fl += 1
                if gen in list_ad.keys():
                    list_ad[gen] += 1
                else:
                    list_ad[gen] = 1
            if gen in gens_ar:
                ar_count += 1
                fl += 1
                if gen in list_ar.keys():
                    list_ar[gen] += 1
                else:
                    list_ar[gen] = 1
            if fl == 2:
                both_count+=1
                if gen in list_adar.keys():
                    list_adar[gen] += 1
                else:
                    list_adar[gen] = 1

            if fl == 0:
                ost_count += 1
                if gen in list_ost.keys():
                    list_ost[gen] += 1
                else:
                    list_ost[gen] = 1

        else:
            continue

all_p = n_st//2
print(f'ad_mutations: {ad_count}, {ad_count/all_p} %')
print(f'ar_mutations: {ar_count}, {ar_count/all_p} %')
print(f'ad_and_ar_mutations: {both_count}, {both_count/all_p} %')
print(f'not_ad_ar_mutations: {ost_count}, {ost_count/all_p} %')
print(f'all_mutations: {all_p}')
print(f'summa: {ad_count + ar_count + ost_count}')
print(f'ad_gens: {len(list_ad)}')  # 1004 len
print(f'ar_gens: {len(list_ar)}')
print(f'ad_ar_gens: {len(list_adar)}') # 1571 len
print(f'not_ad_ar_gens: {len(list_ost)}')  # 8379 len
print()
print('Litter')
print(len(gens_ar))  # 2502
print(len(gens_ad))  # 1610
mas = pd.DataFrame(index=['AD','AR'])
mas['absolute'] = [1004, 1571]
mas['percentage'] = [1004/1610, 1571/2502]
mas['Number of gens in group'] = [1610, 2502]
print(mas.head())

# x = []
# y = []
# counter_dict = {}
# for k in list_ad.keys():
#     x.append(k)
#     y.append(list_ad[k])
#     if list_ad[k] in counter_dict.keys():
#         counter_dict[list_ad[k]] += 1
#     else:
#         counter_dict[list_ad[k]] = 1
#print(counter_dict)
# plt.bar(x, y, width=0.8)
# plt.xlabel('Gen')
# plt.ylabel('Number of mutations')
# plt.title('Number of predictions in different AD gens')
# plt.grid(True)
# plt.show()

# ВЫВОД
# ad_mutations: 4164, 0.10194887866026833 %
# ar_mutations: 6956, 0.17030653217118794 %
# ad_and_ar_mutations: 1334, 0.032660855939672905 %
# not_ad_ar_mutations: 31058, 0.7604054451082166 %
# all_mutations: 40844
# summa: 42178
# ad_gens: 1004
# ar_gens: 1571
# ad_ar_gens: 296
# not_ad_ar_gens: 8379
#
# Litter
# 2502
# 1610
#     absolute  percentage  Number of gens in group
# AD      1004    0.623602                     1610
# AR      1571    0.627898                     2502

# 1) Я пересчитал статистику по попаданию мутаций в AD и AR гены. Та статистика, что вы скидывали, была сделана на основе файла
# с лишними мутациями. Я сделал статистику на основе итогового файла зred_filtr.vcf, и там немного изменились значения. Значения в процентах
# практически не изменились.
# Всего мутаций с различающимися предсказаниями: 40844
# мутации в AD генах: 4164, 10.2 %
# мутации в AR генах: 6956, 17.0 %
# Мутации в генах, которые одновременно в AD и AR списке: 1334, 3.3 %
#Остальные мутации: 31058, 76.0 %
#(Проверка: 4164+6956−1334+31058 = 40844)
# (НЕ в AD генах: 31058+6956-1334 = 36680)
# 2) Сумма всех мутаций из гистограммы распределений по ad генам с различными pli скорами составляет 4072.
# Есть AD гены, для которых я не нашел pli-скоры, таких генов 25. К таким генам относятся еще 92 мутации:
# Таким образом, к AD генам относится 4072+92=4164 мутации, что полностью совпадает с приведенной в 1) статистикой.
# То есть распределение по pli-скорам верное.


# Мутации, которые НЕ в ad генах: 36682 (36682)
# Кол-во ГЕНОВ с предсказаниями, НЕ попавших в ad: 9655
# count ad, мутации, которые в ad генах БЕЗ pli: 92
# Кол-во генов с предсказаниями, попавших в ad БЕЗ pli : 24
# count ad, мутации, которые в ad генах С pli: 4071 (4072)
# Кол-во генов с предсказаниями, попавших в ad С pli : 979
# Всего генов с предсказаниями: 10658
# Всего мутаций: 40844
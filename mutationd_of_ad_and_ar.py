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
    ost_count = 0
    list_ad = {}
    list_ar = {}
    list_ost = {}
    for st in predict:
        n_st += 1
        if n_st % 2 == 1:
            gen = st[:-1].split('\t')[6].split('|')[1]
            fl = 0
            if gen in gens_ad:
                ad_count += 1
                fl = 1
                if gen in list_ad.keys():
                    list_ad[gen] += 1
                else:
                    list_ad[gen] = 1
            if gen in gens_ar:
                ar_count += 1
                fl = 1
                if gen in list_ar.keys():
                    list_ar[gen] += 1
                else:
                    list_ar[gen] = 1

            if fl == 0:
                ost_count += 1
                if gen in list_ost.keys():
                    list_ost[gen] += 1
                else:
                    list_ost[gen] = 1

        else:
            continue

all_p = n_st//2
print(ad_count)
print(ar_count)
print(ost_count)
print(all_p)
print(ad_count/all_p)
print(ar_count/all_p)
print(ost_count/all_p)
print(len(list_ad))  # 1004 len
print(len(list_ar))  # 1571 len
print(len(list_ost))  # 8379 len

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



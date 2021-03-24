## Построение гистограммы. Для предсказания каждого полиморфизма выбирается максимальная вероятность образования/нарушения СС.Строится гистограмма
## распределения предсказаний по максимальным вероятностям.
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
# для создание статистики. Сохраняется в freq_mut_alt_genom.txt
# file_mut = open('mutations_alt_genom_filtr.vcf','r')
# zag = file_mut.readline()
# freq = {}
# for i in range(100):
#     if ((i+1)%10 == 0):
#         freq[str((i+1)/100)+'0']=0
#         continue
#     freq[str((i+1)/100)]=0
# #print(freq.keys())
# for st in file_mut:
#     stm = st[0:-1].split('\t')
#     fl = 0
#     try:
#         info = stm[4]
#     except IndexError:
#         continue
#     try:
#         spliceai = info.split(';')[1]
#     except IndexError:
#         continue
#     probab = spliceai.split('|')
#     try:
#         re = probab[5]
#     except IndexError:
#         continue
#     mmax = '-1'
#     for j in range(2,6):
#         if float(probab[j]) > float(mmax):
#             mmax = probab[j]
#     freq[mmax]+=1
# pr = []
# fr = []
# for k in freq.keys():
#     pr.append(k)
#     fr.append(freq[k])
# #print(pr)
# #print(fr)
# file_mut.close()
# S = sum(fr)
# frp=[]
# for el in fr:
#     frp.append(el/S)
# # for el in frp:
# #     print('{:.2}'.format(round(el,2)),end=' ')
# fif = open('freq_mut_alt_genom.txt','w')
# fif.write('#MAX_PROBABILITY\tAMOUNT\tFREQUENCY\n')
# for p,fp in zip(pr,fr):
#     fif.write('{}\t{}\t{:.2}\n'.format(p,fp,round(fp/S,2)))
#
# fif.close()
fif = open('freq_mut_alt_genom.txt','r')
zag = fif.readline()
pr = []
amount = []
fr = []

for st in fif:
    stm = st[:-1].split('\t')
    pr.append(float(stm[0])*100)
    amount.append(int(stm[1]))
    fr.append(float(stm[2])*100)

fif.close()
print(pr)
print(fr)

print(amount)
fig, ax = plt.subplots(figsize=(15,15))
#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
plt.bar(pr,fr,width = 0.8)
plt.grid(True)

plt.xlabel('Maximum probability from 4 \n probabilities of appearing/disappearing of \n donor/acceptor sites, %')
plt.ylabel('Percentage from whole amount of predictions, %')
plt.title('Probabilities of appearing/disappearing splicing sites')
plt.show()





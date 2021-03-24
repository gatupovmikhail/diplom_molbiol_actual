## Построение гистограммы. Для предсказания каждого полиморфизма выбирается максимальная вероятность образования/нарушения СС.Строится гистограмма
## распределения предсказаний по максимальным вероятностям.
import matplotlib.pyplot as plt
file_mut = open('mutations_alt_genom_filtr.vcf','r')
zag = file_mut.readline()
freq = {}
for i in range(100):
    if ((i+1)%10 == 0):
        freq[str((i+1)/100)+'0']=0
        continue
    freq[str((i+1)/100)]=0
#print(freq.keys())
for st in file_mut:
    stm = st[0:-1].split('\t')
    fl = 0
    try:
        info = stm[4]
    except IndexError:
        continue
    try:
        spliceai = info.split(';')[1]
    except IndexError:
        continue
    probab = spliceai.split('|')
    try:
        re = probab[5]
    except IndexError:
        continue
    mmax = '-1'
    for j in range(2,6):
        if float(probab[j]) > float(mmax):
            mmax = probab[j]
    freq[mmax]+=1
pr = []
fr = []
for k in freq.keys():
    pr.append(k)
    fr.append(freq[k])
#print(pr)
#print(fr)
file_mut.close()
S = sum(fr)
frp=[]
for el in fr:
    frp.append(el/S)
# for el in frp:
#     print('{:.2}'.format(round(el,2)),end=' ')
fif = open('freq_mut_alt_genom.txt','w')
fif.write('#MAX_PROBABILITY\tAMOUNT\tFREQUENCY\n')
for p,fp in zip(pr,fr):
    fif.write('{}\t{}\t{:.2}\n'.format(p,fp,round(fp/S,2)))

fif.close()
plt.bar(pr,fr)
plt.grid(True)
plt.show()





import matplotlib.pyplot as plt
polim = open('polim_in_gens_form_razn.txt','r')
file_out = open('polimor10.vcf','w')
file_out.write(('#GEN\tCHROM\tSTRAND\tSTART\tEND\tPOS\tREF/ALT\n'))
zag = polim.readline()

# ref_mas = []  [3713077, 234, 61, 23, 14, 6, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0]
# for i in range(11):
#     ref_mas.append(i*10**6)
# for i in range(12,25,2):
#     ref_mas.append(i*10**6)
# ref_mas = [] [3707916, 2266, 904, 505, 338, 220, 183, 134, 98, 79, 71, 60, 60, 50, 44, 44, 35, 23, 19, 28, 0]
# for i in range(0,105,5):
#     ref_mas.append(i*10**4)
# S = 2000 [3678006, 19898, 1907, 993, 776, 718, 606, 533, 479, 416, 371, 349, 313, 304, 298, 256, 241, 190, 221, 189, 0]
# ref_mas = []
# for i in range(0,42000,S):
#     ref_mas.append(i)
# ref_mas = []
# S = 50
# for i in range(0,1550,S):
#     ref_mas.append(i)
ref_mas = []
S = 10
for i in range(0,210,S):
    ref_mas.append(i)
countm = [0]*len(ref_mas)
#ref_mas = []
# S = 1
# for i in range(0,22,S):
#     ref_mas.append(i)
# countm = [0]*len(ref_mas)

maxM = []
minM = []
chM = []
mmax = -1
mmin = 10*10**10

st0 = polim.readline()
ch0 = st0.split('\t')[1]
chM.append(ch0)
pos0 = int(st0.split('\t')[4])
for st in polim:
    ch = st.split('\t')[1]
    pos = int(st.split('\t')[4])
    delta = pos - pos0
    if (ch0 == ch):
        if delta <= 10:
            file_out.write(st)
        for i in range(len(ref_mas)-1):  ### -1!
            if ref_mas[i] <= delta < ref_mas[i+1]:
                countm[i]+=1
                fl = 1
                break
            else:
                pass
                #countm[20]+=1
    else:
        chM.append(ch)
        delta = 0
        # maxM.append(mmax)
        # minM.append(mmin)
        # mmax = -1
        # mmin = 10 * 10 ** 10
    pos0 = pos
    ch0 = ch
# maxM.append(mmax)
# minM.append(mmin)
# for i in range(len(chM)):
#     print('{}\t{}\t{}'.format(chM[i],minM[i],maxM[i]))
# print(max(maxM))
polim.close()
print(countm)
print(ref_mas)
print(len(countm))
fig, ax = plt.subplots()
# for i in range(len(ref_mas)):
#     ref_mas[i]+=S/2
d = S
plt.bar(ref_mas[:-1], countm[:-1], width=d * 0.8)
ax.set_title('Распределение расстояний между полиморфизмами')
ax.set_xlabel('r')
ax.set_ylabel('Frequency')
plt.grid(True)
plt.show()
file_out.close()
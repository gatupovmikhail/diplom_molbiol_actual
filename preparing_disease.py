#print(repr(' \n\r\thaha\n\r\t '.strip()))
def ohpos(st):
    st = st.strip()
    st=st.replace('Chr11:','')
    return st
def ohzam(st):
    st = st.strip()
    ind = st.find('>')
    ref = st[ind-1]
    alt = st[ind+1]
    return ref, alt
dis = open('diseases.txt','r')
anal = open('analis_from_splice50.vcf','r')
posdis=[]
refdis=[]
altdis=[]
for st in dis:
    stm = st.split('\t')
    #print(stm)
    posdis.append(ohpos(stm[1]))
    refd, altd = ohzam(stm[4])
    refdis.append(refd)
    altdis.append(altd)
zag= anal.readline()
possp=[]
refsp=[]
altsp = []
for st in anal:
    stm = st.split('\t')
    if stm[0] == 'alt':
        possp.append(stm[2])
        refsp.append(stm[3])
        altsp.append(stm[4])
sovp = []
for i in range(len(posdis)):
    for k in range(len(possp)):
        if posdis[i] == possp[k]: # and refdis[i] == refsp[k] and altdis[i] == altsp[k]:
            sovp.append(k)

print(sovp)

print(len(possp))
# print(refsp)
# print(altsp)

print(len(posdis))
# print(refdis)
# print(altdis)
anal.close()
dis.close()

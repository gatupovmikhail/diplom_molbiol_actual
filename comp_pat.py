dis = open('pathogenic.txt','r')
my = open('analis_from_splice.vcf','r')
posp = []
bukp = []
for st in dis:
    stm = st.split('\t')
    posp.append(int(stm[1].split(':')[1]))
    bukp.append(stm[4][-3:len(stm[4])])

print(bukp)
print(posp)
zag = my.readline()
for st in my:
    stm = st.split('\t')
    if stm[0] == 'alt':
        pos = int(stm[2])
        for i in range(len(posp)):
            if posp[i] == pos:
                print('{}\t{}\t{}/{}'.format(pos,bukp[i],stm[3],stm[4]))
my.close()
dis.close()
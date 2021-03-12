## убираем поли-snp в gnomad_polim только полим с af>0.01
polim = open('gnomad_polim.vcf','r')
file_out = open('gnomad_polim_snp.vcf','w')
zag = polim.readline()
file_out.write(zag)
st0 = polim.readline()
freq = []
stf = []
num = 2
for st in polim:
    num+=1
    if not ('$' in st) and not('$' in st0):
        file_out.write(st0)
    if ('$' in st) and not('$' in st0):
        freq.append( float(st0.split('\t')[4]) )
        stf.append(st0)
    if ('$' in st) and ('$' in st0):
        freq.append(float(st0.split('\t')[4]))
        stf.append(st0)
    if not('$' in st) and ('$' in st0):
        freq.append(float(st0.split('\t')[4]))
        stf.append(st0)
        #if len(freq) > 2:
            #print(num)
        m = -1
        k=-1
        for i in range(len(freq)):
            if freq[i] > m:
                m = freq[i]
                k = i

        file_out.write(stf[k].replace('$',''))
        freq = []
        stf = []

    st0 = st

## проверь, нет ли $ в последней строчке последней хромосомы !
file_out.write(st)
file_out.close()
polim.close()
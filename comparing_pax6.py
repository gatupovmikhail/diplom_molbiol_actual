# сравнивает список, полученный в результате прямого сравнения версий генов со списком полученным из polim_in_gens.txt
def chekbuk(buk):
    buk = buk.upper()
    if (buk == 'A') or (buk == 'T') or (buk == 'G') or (buk == 'C'):
        return True
    else:
        return False
file_ref = open('pax6_mut_ref.txt','r')
file_alt = open('pax6_mut_alt.txt','r')
file_ref_out = open('pax6_comp_ref.txt','w')
file_alt_out = open('pax6_comp_alt.txt','w')
#file_alt = open('pax6_alt.txt','r')
fl=0
for i in range(2):
    z=file_ref.readline()
    z=file_alt.readline()
num=2
pos = 31810457 - 1
pos_real = []
buk_real = []
pos_et = []
buk_et = []
for st1 in file_ref:
    num+=1
    st2 = file_alt.readline()
    for k in range(len(st1)):
        bukR = st1[k]
        bukA = st2[k]
        if chekbuk(bukR) and chekbuk(bukA):
            pos+=1
            if not(bukR.lower()==bukA.lower()):
                pos_real.append(pos)
                buk_real.append('{}/{}'.format(bukR.upper(),bukA.upper()))
etalon = open('polim_in_gens.txt','r')
for st in etalon:
    stl = st[0:-1].split('||')
    if stl[1] == 'PAX6':
        stm = stl[0].split('\t')
        try:
            pos = int(stm[1])*50 + int(stm[2].split(',')[0])
        except ValueError:
            print(st)
        buket = stm[2].split(',')[1]
        pos_et.append(pos)
        buk_et.append(buket)
fl1 = 0
# запись в файлы неверна!!!!
file_alt_out.write('#CHROM\tPOS\tREf/ALT\n')
file_ref_out.write('#CHROM\tPOS\tREf/ALT\n')
for k in range(len(pos_et)):
    file_alt_out.write('chr11\t{}\t{}\n'.format(pos_et[k],buk_et[k]))
    file_ref_out.write('chr11\t{}\t{}\n'.format(pos_et[k], buk_et[k]))
    if not(pos_et[k] == pos_real[k]):
        print(k)
        fl1 = 1
    if not(buk_et[k]==buk_real[k]):
        print(k)
        fl1 =1
print(fl1)
print(buk_et)
print(buk_real)
print(pos_et)
print(pos_real)
file_ref_out.close()
file_alt_out.close()
file_ref.close()
file_alt.close()
etalon.close()
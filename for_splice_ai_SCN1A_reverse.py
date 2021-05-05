# Мутагенез гена на - цепи
# посл для - цепи
from sys import exit
from my_library import writting_file, checkfile, zagprint, few_columns

def revers(buk):
    if buk.upper()=='A':
        return 'T'
    if buk.upper()=='T':
        return 'A'
    if buk.upper()=='G':
        return 'C'
    if buk.upper()=='C':
        return 'G'
    if buk.upper()=='N':
        return 'N'

def zapis(buk):
    tri=[]
    if buk.upper()=='N':
        tri.append('N')
    if not(buk.upper()=='A'):
        tri.append('A')
    if not(buk.upper()=='T'):
        tri.append('T')
    if not(buk.upper()=='G'):
        tri.append('G')
    if not(buk.upper()=='C'):
        tri.append('C')

    return tri

const_s='\t100\tPASS\tMQ=50\tAF:GT\t0.5:0/1\n'
file_out = open('SCN1A_reverse_mutations.vcf','w')
file_out.write('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tSAMPLE\n')
gen_rev = ''
#166930149 166845672
with open('SCN1A.fa','r') as file_gen:
    zag = file_gen.readline()
    gen = file_gen.read()
    gen = gen[::-1]
    for buk in gen:
        gen_rev += revers(buk)
print(gen_rev)
ch = 'chr2'
start = 166930149
for buk in gen_rev:
    bukvas = zapis(buk)
    for bukva in bukvas:
        file_out.write('{}\t{}\t.\t{}\t{}'.format(ch,start,buk.upper(),bukva)+const_s)
    start = start - 1
file_out.close()
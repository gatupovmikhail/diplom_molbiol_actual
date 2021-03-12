from sys import exit
def cheks(b):
    fl = 0
    if b=='A':
        fl = 1
    if b=='T':
        fl = 1
    if b=='G':
        fl = 1
    if b=='C':
        fl = 1
    return fl
file_ind = open('ind.txt','r')
ind = int(file_ind.read())
file_ind.close()
file_ind = open('ind.txt','w')
file_ind.write(str(ind+1))
file_ind.close()
num_ind = list(range(1,23))
num_ind.append('X')
#num_ind.append('Y')
N = num_ind[ind]
#N = 'Y'
name_file = 'gnomad.genomes.r2.0.2.sites.chr{}.vcf'.format(N)
#name_file = 'gnomad.exomes.r2.1.1.sites.Y.vcf'
gnom = open(name_file,'r')
file_out = open('gnomad_polim_chr{}.vcf'.format(N),'w')
file_log = open('gnomad_log.txt','a')
num = 0
st='#'
zag='#'
while('#' in st):
    zag = st
    st = gnom.readline()
    num+=1
if ind == 0:
    file_out.write('#CHROM\tPOS\tREF\tALT\tAF\tID\n')

stm = st.split('\t')
if len(stm) < 7:
    print('fail')
    gnom.close()
    file_out.close()
    file_log.close()
    exit()
id = stm[2]
ref = stm[3]
povt = 0
if len(ref) == 1:
    alt = stm[4].split(',')
    for i in range(len(alt)):
        if len(alt[i]) > 1:
            continue
        af = stm[7].split(';')[1].replace('AF=', '').split(',')
        if not (af[i] == '.'):
            aff = float(af[i])
        else:
            aff = 0

        if (cheks(ref) == 0) or (cheks(alt[i]) == 0):
            ch = stm[0]
            pos = stm[1]
            file_log.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format('chr'+ch, pos, ref, alt[i], aff, id))
            continue

        if aff >= -1:  ##### здесь важно
            if povt == 0:
                ch = stm[0]
                pos = stm[1]
                file_out.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format('chr'+ch, pos, ref, alt[i], aff, id))
            if povt > 0:
                ch = stm[0]
                pos = stm[1]
                file_out.write('${}\t{}\t{}\t{}\t{}\t{}\n'.format('chr'+ch, pos, ref, alt[i], aff, id))
            povt+=1


for st in gnom:
    num+=1
    stm = st.split('\t')
    if len(stm) < 7:
        file_log.write(st)
        continue

    povt = 0
    id = stm[2]
    ref = stm[3]
    if (',' in ref):
        print('warning')
        print(st)
        gnom.close()
        file_out.close()
        file_log.close()
        exit()


    if len(ref) > 1:
        continue
        
    alt = stm[4].split(',')
    for i in range(len(alt)):
        if len(alt[i]) > 1:
            continue
        af = stm[7].split(';')[1].replace('AF=', '').split(',') ######################################
        if not (af[i] == '.'):
            try:
                aff = float(af[i])
            except ValueError:
                print('Вот ты где')
                print(num)
                aff = 0
        else:
            aff = 0
    
        if (cheks(ref) == 0) or (cheks(alt[i]) == 0):
            ch = stm[0]
            pos = stm[1]
            file_log.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format('chr'+ch, pos, ref, alt[i], aff, id))
            continue
    
        if aff >= -1:  ### важно
            if povt == 0:
                ch = stm[0]
                pos = stm[1]
                file_out.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format('chr'+ch, pos, ref, alt[i], aff, id))
            if povt > 0:
                ch = stm[0]
                pos = stm[1]
                file_out.write('${}\t{}\t{}\t{}\t{}\t{}\n'.format('chr'+ch, pos, ref, alt[i], aff, id))
            povt+=1


print('Файл {} успешно обработан\n'.format(name_file))
gnom.close()
file_out.close()
file_log.close()

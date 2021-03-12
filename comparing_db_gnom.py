from sys import exit
dbsnp = open('num_pol_new.txt','r')
gnom = open('gnomad_polim_form.vcf','r')
file_otl = open('db_gnom_otl.vcf','w')
file_otl.write('#CHROM\tNUM_ST\tPOS_IN_ST\tNUM_GN\tNUM_DB\n')
sovp = 0
otl = 0
ch_d = 'a'
std0 = ''
num_gn = 0
num_db = 0
for st in gnom:
    num_gn+=1
    stm = st[0:-1].split('\t')
    ch_g = stm[0]
    nst_g = int(stm[1])
    npos_g = int(stm[2].split(',')[0])
    if not(ch_g == ch_d):
        file_ch = open('compar_ch.txt', 'w')
        file_ch.write(std0)
        ch_d = ch_g
        while(ch_g == ch_d):
            std = dbsnp.readline()
            num_db+=1
            stdm = std.split('\t')
            ch_d = stdm[0]
            nst_d = stdm[1]
            npos_d = stdm[2].split(',')[0]
            if ch_d == ch_g:
                file_ch.write('{}\t{}\t{}\n'.format(ch_d,nst_d,npos_d))
            else:
                std0 = '{}\t{}\t{}\n'.format(ch_d,nst_d,npos_d)
        ch_d = ch_g
        file_ch.close()
    file_ch = open('compar_ch.txt', 'r')
    flag = 0
    for st_h in file_ch:
        stm_h = st_h.split('\t')
        ch_h = stm_h[0]
        nst_h = int(stm_h[1])
        npos_h = int(stm_h[2])
        if not(ch_h == ch_g):
            print('ERROR!')
            print(repr(st))
            print(repr(st_h))
            exit()
        if (nst_h == nst_g) and (npos_g == npos_h):
            flag = 1
            break
        if (nst_h > nst_g):
            break
    file_ch.close()
    if flag == 0:
        file_otl.write(st[0:-1]+'\t'+str(num_gn)+'\t'+str(num_db)+'\n')

file_otl.close()
dbsnp.close()
gnom.close()
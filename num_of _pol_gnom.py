from sys import exit
# Часть 1 - перевод формата pos из формата позиции от начала хромосомы в формат номер строки + позиция в строке.
# Часть 2 - перевод всех полиморфизмов, следующих друг за другом в одной строке на одну строку документа.

from my_library import writting_file, checkfile, zagprint, few_columns

name_file='gnomad_polim_snp.vcf'
name_file_out='gnomad_polim_form.vcf'
file_out=open(name_file_out,'w')
with open(name_file) as mfile:
    zag=mfile.readline()
    for st in mfile:
        stm=st[0:-1].split('\t')
        num_st=int(stm[1])//50
        if int(stm[1])%50==0:
            ost_st =50
            num_st-=1
        else:
            ost_st=int(stm[1])%50
        ref = stm[2]
        alt=stm[3]
        af = stm[4]
        idd = stm[5]
        ch=stm[0]
        file_out.write('{}\t{}\t{}\t{}\t{},{}/{}\n'.format(ch,idd,af,num_st,ost_st,ref,alt))



file_out.close()
#                           previous version



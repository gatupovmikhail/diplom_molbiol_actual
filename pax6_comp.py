## Для сравнения референсной версии PAX6 и версии PAX6 от разработчиков SpliceAI
import os
from sys import exit # доработай входные файлы.
def comparing(st1,st2,file_out): # функция для сравнения вероятностей
    stm1 = st1[0:-1].split('\t')
    stm2 = st2[0:-1].split('\t')
    if not(stm1[1] == stm2[1]): # проверка соответствия значений в поле POS
        print('Пропуск какой-то позиции в одном из файлов, либо лишняя позиция')
        print('Позиция в файле ref: {} Позиция в файле alt: {}'.format(stm1[1],stm2[1]))
        exit()
    if stm1[3] =='E' or len(stm1) < 5:
        return 0
    alt_allel1 = stm1[4].split(',') # массив из аллелей
    alt_allel2 = stm2[4].split(',')
    info1= stm1[7] # значение поля INFO
    info2= stm2[7]
    flag_n = 0
    #### проверка, что все аллели совпадают
    # for k in range(3):
    #     for j in range(3):
    #         if alt_allel1[k] == alt_allel2[j]:
    #             flag_n+=1

    ## сравнение вероятностей только в случае сопвпадения аллелей
    for j in range(len(alt_allel1)):
        for k in range(len(alt_allel2)):
            try:
                re = alt_allel1[j]
            except IndexError:
                print(st1,end='')
                print(st2)
                return 1
            try:
                re = alt_allel2[k]
            except IndexError:
                print(st1,end='')
                print(st2)
                return 1
            try:
                re = info1.split(',')[j].split('|')[1]
            except IndexError:
                print(st1,end='')
                print(st2)
                return 1
            try:
                re = info2.split(';')[2].split(',')[k].split('|')[1]
            except IndexError:
                print(st1,end='')
                print(st2)
                return 1

            if alt_allel1[j] == alt_allel2[k] and info1.split(',')[j].split('|')[1]==info2.split(';')[2].split(',')[k].split('|')[1]:
                #snp1 = info1.split(';')[1].replace('SNP=','')  # инфо об SNP
                snp2 = info2.split(';')[1].replace('SNP=','')
                spl_ai1 = info1.replace('SpliceAI=','') # инфо от SpliceAI
                spl_ai2 = info2.split(';')[2].replace('SpliceAI=', '')
                probability1 = spl_ai1.split(',') # массив с предсказаниями отдельно для каждой аллели мутагенеза
                probability2 = spl_ai2.split(',')
                if not(probability1[j].split('|')[0] == alt_allel1[j]) or not(probability2[k].split('|')[0] == alt_allel2[k]): # проверка соответствия аллели в предсказании и аллели в поле POS
                    print('Error in prediction, in order of predicrions')
                    exit()
                else:
                    p_sites1 = []
                    for p in range(2,6):
                        p_sites1.append(float(probability1[j].split('|')[p])) # массив вероятностей ref
                    p_sites2 = []
                    for p in range(2, 6):
                        p_sites2.append(float(probability2[k].split('|')[p])) # массив вероятностей alt
                    for p in range(4): #j-k
                        if abs(p_sites2[p] - p_sites1[p]) >= probability_border:
                            file_out.write('ref\t{chrom}\t{pos}\t{ref}\t{alt}\t{snp}\t{pred}\n'.format(chrom=stm1[0],pos=stm1[1],ref=stm1[3],alt=alt_allel1[j], \
                                                                                                       snp=snp2,pred=probability1[j]))
                            file_out.write('alt\t{chrom}\t{pos}\t{ref}\t{alt}\t{snp}\t{pred}\n'.format(chrom=stm2[0], pos=stm2[1],ref=stm2[3], alt=alt_allel2[k], \
                                                                                        snp=snp2, pred=probability2[k]))
            if alt_allel1[j] == alt_allel2[k] and not(info1.split(',')[j].split('|')[1] == info2.split(';')[2].split(',')[k].split('|')[1]):
                file_er.write('ref'+st1)
                file_er.write('alt'+st2)
file_er = open('errors_of_splice.vcf','a')

# comparing(st1,st2,file_out)
file_ref = open('pax6_from_razrab_filtr.vcf','r')
file_alt = open('pax6_ref_alg.vcf','r')
name_out = 'an_pax6'
probability_border = 0.5
file_out = open(name_out+'_{:.2}.vcf'.format(probability_border),'w')
st1 = '#'
while '#' in st1:
    st1 = file_ref.readline()
st2 = '#'
while '#' in st2:
    st2 = file_alt.readline()

fl = comparing(st1, st2, file_out)
for st1 in file_ref:
    st2 = file_alt.readline()
    fl = comparing(st1, st2, file_out)
    if fl == 1:
        break
print('Записано в ' + name_out + '_{:.2}.vcf'.format(probability_border))
file_ref.close()
file_alt.close()
file_out.close()
file_er.close()
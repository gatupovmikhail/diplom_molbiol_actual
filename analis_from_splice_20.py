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
                    for p in range(4):
                        if abs(p_sites2[p] - p_sites1[p]) >= probability_border:
                            file_out.write('ref\t{chrom}\t{pos}\t{ref}\t{alt}\t{snp}\t{pred}\n'.format(chrom=stm1[0],pos=stm1[1],ref=stm1[3],alt=alt_allel1[j], \
                                                                                                       snp=snp2,pred=probability1[j]))
                            file_out.write('alt\t{chrom}\t{pos}\t{ref}\t{alt}\t{snp}\t{pred}\n'.format(chrom=stm2[0], pos=stm2[1],ref=stm2[3], alt=alt_allel2[k], \
                                                                                        snp=snp2, pred=probability2[k]))
            if alt_allel1[j] == alt_allel2[k] and not(info1.split(',')[j].split('|')[1] == info2.split(';')[2].split(',')[k].split('|')[1]):
                file_er.write('ref'+st1)
                file_er.write('alt'+st2)

files = os.listdir('/home/gatupov/PycharmProjects/first_project/archives')
#print(files)
file_files = open('splice_ref/info_files.txt','r')
ch_ref_mas = []
pos_ref_mas = []
for st in file_files:
    #print(st.split('\t')[2])
    ch_ref_mas.append(st.split('\t')[2].split('|')[0])
    pos_ref_mas.append(st.split('\t')[2].split('|')[1])
file_files.close()
file_er = open('errors_of_splice.vcf','w')
for file_ach in files:
    #file_ach = 'chr4_152639315_103800000.vcf'
    name_alt='archives/'+ file_ach
    ch_ach = file_ach.split('_')[0].replace('chr','')
    pos_ach = file_ach.split('_')[1]
    file_alt = open(name_alt,'r')

    name_ref='Nan'
    for i in range(len(ch_ref_mas)):
        if ch_ref_mas[i]==ch_ach and pos_ref_mas[i] == pos_ach:
            name_ref = '/media/gatupov/Elements1/splice/for_splice_{}.vcf'.format(i+1)
            print('{} {}\n'.format(name_ref,file_ach))
            break
    if name_ref == 'Nan':
        print(file_ach)
        print('not found')
        print(ch_ach,pos_ach)
        file_alt.close()
        exit()

    file_ref = open(name_ref,'r')
    probability_border = 0.5
    name_out = name_alt+'_comp'
    file_out = open('analis/'+file_ach.replace('.vcf','')+'_{:.2}.vcf'.format(probability_border),'w')
    file_out.write('#GENOM\tCHROM\tPOS\tREF\tALT\tSNP(CHROM|ID|POSITION|VARIATION|FREQUENCY)\tPROBABILITY(Format: ALLEL|GEN|DS_AG|DS_AL|DS_DG|DS_DL|DP_AG|DP_AL|DP_DG|DP_DL)\n')

    ###### Проверка, одинаковое ли количество строк с #  в начале файла.
    for numb in range(43):
        st1 = file_ref.readline()
    for numb in range(44):
        st2 = file_alt.readline()
    if not('#CHROM' in st1):
        print('Error. Не одинаковое количество заголовочных строк ref')
        print(file_ach,name_ref)
        exit()
    if not('#CHROM' in st2):
        print('Error. Не одинаковое количество заголовочных строк alt')
        print(file_ach, name_ref)
        exit()
    ###########################

    #comparing(st1,st2,file_out)
    for st1 in file_ref:
        st2 = file_alt.readline()
        fl = comparing(st1,st2,file_out)
        if fl==1:
            break
    print('Записано в '+name_out+'_{:.2}.vcf'.format(probability_border))
    file_ref.close()
    file_alt.close()
    file_out.close()

file_er.close()

# /media/gatupov/Elements1/splice/for_splice_2786.vcf chr14_32890489_278500000.vcf
#
# 14	32956402	.	A	C,G,T	.	.	SpliceAI=C|AKAP6|0.00|0.00|0.00|0.00|39|26|20|1,G|AKAP6|0.00|0.00|0.00|0.00|-7|26|-7|20,T|AKAP6|0.00|0.00|0.00|0.00|-7|26|-17|1
# chr14	32956402	.	A	T,G,C	100	PASS	MQ=50;SNP=chr14|rs10143778|32956352|T/C|0.658824,chr14|r
#
# /media/gatupov/Elements1/splice/for_splice_2496.vcf chr12_187019_249500000.vcf
#
# 12	415062	.	A	C,G,T	.	.	SpliceAI=C|KDM5A|0.00|0.00|0.00|0.00|-47|-25|29|-2,G|KDM5A|0.00|0.00|0.00|0.00|21|-47|-2|29,T|KDM5A|0.00|0.00|0.00|0.00|-2|-25|-2|-24
# chr12	415062	.	A	T,G,C	100	PASS	MQ=50;SNP=chr12|rs12303118|415056|T/C|0.0692188;SpliceAI=T|KDM5A|0.00|
#
# /media/gatupov/Elements1/splice/for_splice_2231.vcf chr10_75884749_223000000.vcf
#
# 10	76234447	.	T	A,C,G	.	.	SpliceAI=A|ADK|0.00|0.00|0.00|0.00|-27|21|-4|-2,C|ADK|0.00|0.00|0.00|0.00|-27|21|12|-2,G|ADK|0.00|0.00|0.00|0.00|12|21|-10|-8
# chr10	76234447	.	T	A,G,C	100	PASS	MQ=50;SNP=chr10|rs201219564|76234408|C/T|0.662637,chr10|rs4745747|76234437|G/T|0.621804;SpliceAI=A|ADK|0.00|0.00|0.00|0.00|-27|21|-4|-2,G|ADK
# Записано в archives/chr10_75884749_223000000.vcf_comp_0.5.vcf
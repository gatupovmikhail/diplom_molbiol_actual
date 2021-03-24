# Побочный проект: обработка предсказаний полиморфизмов. Удаляем все строки, для которых все вероятности равны нулю
#path = '/home/gatupov/Загрузки/ALL GnomAD variants/done_gnome_archives/'
import os  # ctrl + alt+ 7
import sys
from time import time
def func_sort_chr(name):
    try:
        nchr = int(name.split('_')[0].replace('chr',''))
        return nchr
    except ValueError:
        return 25
def func_sort_pos(name):
    nchr = int(name.split('_')[1])
    return(nchr)
#### от случайного срабатывания
sys.exit()

path = '/home/gatupov/PycharmProjects/first_project/Predictions on whole alternative genome/archives'
files = os.listdir(path)
files.sort(key=lambda x: (func_sort_chr(x),func_sort_pos(x)) )
for i in range(len(files)):
    files[i] = path + '/' + files[i]

#f = open(path+'for_splice_polim_1.vcf','r')
#file_out = open('all_gnom_variants_pred_filtr.vcf','w')
file_out = open('mutations_alt_genom_filtr.vcf','w')
file_error = open('mutations_alt_genom_errors.vcf','w')
num_in = 0
num_out = 0
# for i in range(44): # было 45
#     zag = f.readline()
#     file_out.write(zag)
# for st in f:
#     stm = st[0:-1].split('\t')
#     fl = 0
#     try:
#         info = stm[7]
#     except IndexError:
#         continue
#     try:
#         spliceai = info.split(';')[2] ## 3!
#     except IndexError:
#         continue
#     probab = spliceai.split('|')
#     try:
#         re = probab[5]
#     except IndexError:
#         continue
#
#     for j in range(2,6):
#         if not(float(probab[j]) == 0):
#             fl = 1
#
#     if fl == 1:
#         file_out.write(st)
#         num_in += 1
#     else:
#         num_out += 1
# f.close()

#for i in range(2,861):
ind_f = 0
t1 = time()
file_log = open('mutations_alt_genom_log.txt','w')
for name_f in files:
    #f = open(path+'for_splice_polim_{}.vcf'.format(i),'r')
    f = open(name_f,'r')
    ind_f += 1
    file_log.write(name_f + ' '+ str(ind_f) + '\n')
    if (ind_f%100==0):
        print(int(ind_f/100), end=' ')
    for i in range(44):
        zag = f.readline()
    if ind_f == 1:
        file_out.write('#CHROM\tPOS\tREF\tALT\tINFO\n')
    num_st = 44
    for st in f:
        num_st+=1
        if num_st%10000 == 0:
            file_log.write(str(num_st//10000)+' ')
        stm = st[0:-1].split('\t')
        if not(len(stm) ==  10):
            num_out += 3
            continue
        const1 = '\t'.join(stm[0:2]) + '\t' + stm[3]
        #const2 = '\t'.join(stm[5:7])
        #const3 = '\t'.join(stm[8:10])
        allel = stm[4]
        allel_m = allel.split(',')
        try:
            re = allel_m[2]
        except IndexError:
            num_out += 3
            continue
        try:
            info = stm[7]
        except IndexError:
            num_out += 3
            continue
        try:
            spliceai_3 = info.split(';')[2] #3!
        except IndexError:
            num_out += 3
            continue
        snp = info.split(';')[1]
        spliceai_mas = spliceai_3.replace('SpliceAI=','').split(',')
        try:
            spliceai_mas[2]
        except IndexError:
            num_out += 3
            continue
        if not(len(spliceai_mas) == 3):
            file_error.write(st)
            num_out += 3
            continue

        for n,spliceai in enumerate(spliceai_mas):
            fl = 0
            probab = spliceai.split('|')

            try:
                re = probab[5]
            except IndexError:
                num_out += 1
                continue

            for j in range(2, 6):
                if not (float(probab[j]) == 0):
                    fl = 1

            if fl == 1:
                file_out.write(const1+'\t'+allel_m[n]+'\t'+snp+';SpliceAI='+spliceai+'\n')
                num_in += 1
            else:
               num_out += 1
    file_log.write('\n')
    f.close()


file_out.close()
file_error.close()
t2 = time()
file_log.write('Прошли: ')
file_log.write(str(num_in))
file_log.write('\n')
file_log.write('Oтброшено: ')
file_log.write(str(num_out))
file_log.write('\n')
file_log.write('Доля отброшенных: ')
file_log.write(str(num_out/(num_in+num_out)))
file_log.write('\n')
file_log.write('Время выполнения (с): ')
file_log.write(str(t2-t1))
file_log.close()
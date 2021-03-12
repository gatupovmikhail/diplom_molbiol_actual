# Выделит только однонуклеотидные замены и посчитает из процент.
import collections
import sys
def zagprint(name_file):
    with open(name_file) as mfile:
        zag = mfile.readline()
        first_str=mfile.readline()
        first_str=first_str.split('\t')
        zag=zag.split('\t')
        for j in range(len(zag)):
            print('{} [{}] | {}'.format(zag[j],j,first_str[j]))

name_file='genom_variation_new'
zagprint(name_file)
name_file_out = 'genome_variation_single_event.txt'
name_file_shlak = 'genome_variation_others_event.txt'
file_out=open(name_file_out,'w')
file_shlak=open(name_file_shlak,'w')



with open(name_file) as mfile:
    counter_single=0
    counter_others=0
    counter_all = 0
    zag=mfile.readline()
    file_out.write(zag)
    file_shlak.write(zag)
    for strk in mfile:
        strkS=strk.split('\t')
        try:
            if (collections.Counter(strkS[9])['/'] == 1):
                file_out.write(strk)
                counter_single+=1
            else:
                file_shlak.write(strk)
                counter_others+=1
            counter_all+=1
        except IndexError:
            print(strkS)
            print(len(strkS))
            print('Строчка номер: {}'.format(counter_all))

file_out.close()
file_shlak.close()
print('counter_all: {} counter_single_others: {} + {} part_single: {}'.format(counter_all,counter_single,counter_others,counter_single/counter_all))
print('Данные записаны в ' + name_file_out)
print('Отсеянные данные записаны в ' + name_file_shlak)

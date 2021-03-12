# Побочный проект: обработка предсказаний полиморфизмов. Удаляем все строки, для которых все вероятности равны нулю
path = '/home/gatupov/Загрузки/ALL GnomAD variants/done_gnome_archives/'
f = open(path+'for_splice_polim_1.vcf','r')
file_out = open('all_gnom_variants_pred_filtr.vcf','w')
num_in = 0
num_out = 0
for i in range(45):
    zag = f.readline()
    file_out.write(zag)
for st in f:
    stm = st[0:-1].split('\t')
    fl = 0
    try:
        info = stm[7]
    except IndexError:
        continue
    try:
        spliceai = info.split(';')[3]
    except IndexError:
        continue
    probab = spliceai.split('|')
    try:
        re = probab[5]
    except IndexError:
        continue

    for j in range(2,6):
        if not(float(probab[j]) == 0):
            fl = 1

    if fl == 1:
        file_out.write(st)
        num_in += 1
    else:
        num_out += 1
f.close()

for i in range(2,861):
    f = open(path+'for_splice_polim_{}.vcf'.format(i),'r')
    print(i,end=' ')
    if (i%50==0):
        print()
    for i in range(45):
        zag = f.readline()
    for st in f:
        stm = st[0:-1].split('\t')
        fl = 0
        try:
            info = stm[7]
        except IndexError:
            continue
        try:
            spliceai = info.split(';')[3]
        except IndexError:
            continue

        probab = spliceai.split('|')

        try:
            re = probab[5]
        except IndexError:
            continue

        for j in range(2, 6):
            if not (float(probab[j]) == 0):
                fl = 1

        if fl == 1:
            file_out.write(st)
            num_in += 1
        else:
            num_out += 1
    f.close()


file_out.close()
print('Прошли')
print(num_in)
print('Oтброшено')
print(num_out)
print('Доля отброшенных')
print(num_out/(num_in+num_out))
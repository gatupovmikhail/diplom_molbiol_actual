# внимание, в коде куча мусора # для возвращения к старому формату убрать 20 отовсюду (3 позиции)
n_st = 0
num_zag = 0
with open('for_splice_ai_ref20.vcf','r') as predict:
    for st in predict:
        n_st += 1


predict = open('for_splice_ai_ref20.vcf','r')
polimorf = open('polim_in_gens.txt','r')
file_out = open('for_splice_ai_ref30.vcf','w')
zag = predict.readline()

gen = 'a'
st = 'o'
pr = 0.05

list_polimorf = []
list_allel = []
list_af = []
list_id = []
chrom = 'a'
for st in polimorf:
    if st[0:-1].split('||')[1] == 'PAX6':
        stm = st[0:-1].split('\t')
        if chrom == 'a': ## сомнительное решение
            chrom = stm[0]
        pos_1 = int(stm[3])*50 + int(stm[4].split(',')[0])
        list_allel.append(stm[4].split(',')[1].replace('||PAX6',''))
        list_polimorf.append(pos_1)
        list_id.append(stm[1])
        list_af.append(stm[2])
for st in predict:
    if '#' in st:
        file_out.write(st)
        continue
    stm = st[0:-1].split('\t')
    pos = int(stm[1])
    flag = 0
    pos_flag = 'NONE'
    for k in range(len(list_polimorf)):
        if abs(pos - list_polimorf[k]) <= 50:
            if flag == 0:
                pos_flag = 'SNP={ch}|{id}|{pol}|{vari}|{af}'.format(ch=chrom, id=list_id[k], pol=list_polimorf[k],
                                                                   vari=list_allel[k], af=list_af[k])
            if flag == 1:
                pos_flag += ',{ch}|{id}|{pol}|{vari}|{af}'.format(ch=chrom, id=list_id[k], pol=list_polimorf[k],
                                                                     vari=list_allel[k], af=list_af[k])
            flag = 1
    first = '\t'.join(stm[0:7])
    second = '\t'.join(stm[8:len(stm)])
    prom = stm[7]+';'+ pos_flag
    file_out.write(first + '\t' + prom + '\t' + second + '\n')
    num_zag += 1
    if (num_zag/n_st) > pr:
        #print(pr, end=' ')
        pr+=0.05





print(list_polimorf)
print('n_st '+str(n_st))
polimorf.close()
file_out.close()
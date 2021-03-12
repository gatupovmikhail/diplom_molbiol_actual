# внимание, в коде куча мусора # для возвращения к старому формату убрать 20 отовсюду (3 позиции)
n_st = 0
with open('alt20_analis_from_splice_0.5.vcf','r') as predict:
    zag = predict.readline()
    for st in predict:
        n_st += 1
    n_st = int(n_st / 2)

predict = open('alt20_analis_from_splice_0.5.vcf','r')
polimorf = open('polim_in_gens.txt','r')
#diap = open('modif_chr11.txt','r')
file_out = open('mod20_analis_from_splice_0.5.vcf','w')
zag = predict.readline()

posmas = [0]*n_st
pos_flag = ['NONE;NONE']*n_st
i = 0
for st in predict:
    stm = st.split('\t')
    pos = int(stm[2])
    posmas[i] = pos
    i+=1
    st1 = predict.readline()
predict.close()


gen = 'a'
st = 'o'

# while not(gen=='PAX6'):  #### пропускаем все гены до PAX6
#     st0 = st
#     st = diap.readline()
#     stm = st[0:-1].split('\t')
#     gen = stm[0]
#     start = int(stm[2])
#     end = int(stm[3])
#     pol = stm[4]
#     vari = stm[5]
# ##########################################
# for i in range(len(posmas)):            ################# первая строка PAX6
#     if (start <= posmas[i]) and (posmas[i] <= end):
#         pos_flag[i] = '{pol}\t{vari}'.format(pol=pol,vari=vari)
#     if posmas[i] > end:
#         continue
# ####################################### строка до PAX6
# stm = st0[0:-1].split('\t')
# start = int(stm[2])
# end = int(stm[3])
# pol = stm[4]
# vari = stm[5]
# for i in range(len(posmas)):
#     if (start <= posmas[i]) and (posmas[i] <= end):
#         pos_flag[i] = '{pol}\t{vari}'.format(pol=pol,vari=vari)
#     if posmas[i] > end:
#         continue
# ######################################
# while (gen == 'PAX6'):  ## gen PAX6
#     st = diap.readline()
#     stm = st[0:-1].split('\t')
#     gen = stm[0]
#     start = int(stm[2])
#     end = int(stm[3])
#     pol = stm[4]
#     vari = stm[5]
#     for i in range(len(posmas)):
#         if (start <= posmas[i]) and (posmas[i] <= end):
#             pos_flag[i] = '{pol}\t{vari}'.format(pol=pol, vari=vari)
#         if posmas[i] > end:
#             continue
# ###############################
# stm = st[0:-1].split('\t') ################### one row after PAX6
# gen = stm[0]
# start = int(stm[2])
# end = int(stm[3])
# pol = stm[4]
# vari = stm[5]
# for i in range(len(posmas)):
#     if (start <= posmas[i]) and (posmas[i] <= end):
#         pos_flag[i] = '{pol}\t{vari}'.format(pol=pol, vari=vari)
#     if posmas[i] > end:
#         continue
####################################

# for st in diap:   ############################конкретно этот блок устарел
#     stm = st[0:-1].split('\t')
#     gen = stm[0]
#     start = int(stm[2])
#     end = int(stm[3])
#     pol = stm[4]
#     vari = stm[5]
#     for i in range(len(posmas)):
#         if (start <= posmas[i]) and (posmas[i] <= end):
#             pos_flag[i] = '{pol}\t{vari}'.format(pol=pol, vari=vari)
#         # if posmas[i] > end:
#         #     continue #############################
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
for i in range(len(posmas)):
    flag = 0
    for k in range(len(list_polimorf)):
        if abs(posmas[i] - list_polimorf[k]) <= 50:
            if flag == 0:
                pos_flag[i] ='{ch};{id};{pol};{vari};{af}'.format(ch=chrom, id=list_id[k], pol=list_polimorf[k], vari=list_allel[k], af=list_af[k])
            if flag == 1:
                pos_flag[i] += '|{ch};{id};{pol};{vari};{af}'.format(ch=chrom, id=list_id[k], pol=list_polimorf[k], vari=list_allel[k], af=list_af[k])
            flag = 1



i=0
with open('alt20_analis_from_splice_0.5.vcf','r') as predict:
    zag = predict.readline()
    file_out.write('#GENOM\tCHROM\tPOS_MUTATION\tINFO(CHROM_VAR;ID_VAR;POS_VARIATION;VARIATION;AF_VAR)\tREF_MUT\tALT_MUT\tProbability(Format: ALLELE|SYMBOL|DS_AG|DS_AL|DS_DG|DS_DL|DP_AG|DP_AL|DP_DG|DP_DL)\n')
    for st in predict:
        stm = st[0:-1].split('\t')
        first = '\t'.join(stm[0:3])
        second = '\t'.join(stm[3:len(stm)])
        try:
            file_out.write('{}\t{}\t{}\n'.format(first,pos_flag[i],second))
        except IndexError:
            print(i)
            print(first)
            print(pos_flag)
            print(pos_flag[i])
            print(second)
        st = predict.readline()
        stm = st[0:-1].split('\t')
        first = '\t'.join(stm[0:3])
        second = '\t'.join(stm[3:len(stm)])
        file_out.write('{}\t{}\t{}\n'.format(first, pos_flag[i],second))
        i+=1
print(posmas)
print(list_polimorf)
print('n_st '+str(n_st))
polimorf.close()
file_out.close()
#diap.close()
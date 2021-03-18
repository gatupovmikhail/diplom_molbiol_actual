# вытаскивает только предсказания с донорными сайтами в альтернативном сплайсинге
# и подсчитывает их статистику
def in_ss_pos(mut_gen,mut_ss,pol_gen): # система координат -2-1+1+2 не используется! вместо нее -2-1,0,+1+2. То есть 0 - это +1 и т. д.
    delta = pol_gen - mut_gen
    if mut_ss > 0:
        mut_ss = mut_ss - 1
    if mut_ss == 0:
        return 10**4
    return mut_ss + delta
def chek(st_ref,st_alt,pos,pos_snp,probab_ref,probab_alt,positions_alt,er):
    fls = [-10]
    for i in [2,3]:
        if probab_alt[i] - probab_ref[i] >=0.5:
            if fls[0] ==-10:
                fls = [i]
                continue
            else:
                fls = [2,3]
    if fls[0] == -10:
        print('aaaaaaaa')
    if len(fls) == 1:
        pol_ss = in_ss_pos(pos,positions_alt[fls[0]],pos_snp)
        if not(pol_ss == 0) and not(pol_ss == 1):
            er+=1
    if len(fls) == 2:
        fer = 0
        for f in fls:
            pol_ss = in_ss_pos(pos,positions_alt[f],pos_snp)
            if not(pol_ss == 0) and not(pol_ss == 1):
                fer+=1
        if fer > 0:
            er+=1


# основная часть
er = 0
pred = open('pred_filtr.vcf','r')
zag = pred.readline()
out_don = open('pred_filtr_ds.vcf','w')
out_dg = open('pred_filtr_ds_dg.vcf','w')
out_dl = open('pred_filtr_ds_dl.vcf','w')
out_dgdl = open('pred_filtr_ds_dgdl.vcf','w')
out_dg.write(zag)
out_dl.write(zag)
out_dgdl.write(zag)
out_don.write(zag)
stat = [0]*4
lab_stat = ['ds_dg','ds_dl','ds_dgdl','all_ds']
f_pos = 0
for st in pred:
    f_pos +=1
    st_ref = st
    stm = st[:-1].split('\t')
    predict_ref = stm[6].split('|')
    snp = stm[5].split('|')
    pos_snp = int(snp[2])
    probab_ref = []
    for i in range(2,6):
        probab_ref.append(float(predict_ref[i]))
    if f_pos == 1:
        print('checking positions')
        print(st_ref)
        print('probab_ref')
        print(probab_ref)
    positions_ref = []
    for i in range(6,10):
        positions_ref.append(int(predict_ref[i]))
    if f_pos == 1:
        print('positions_ref')
        print(positions_ref)

    st = pred.readline()
    st_alt = st
    stm = st[:-1].split('\t')
    predict_alt = stm[6].split('|')
    probab_alt= []

    for i in range(2, 6):
        probab_alt.append(float(predict_alt[i]))
    if f_pos == 1:
        print('checking positions')
        print(st_alt)
        print('probab_alt')
        print(probab_alt)
    positions_alt = []
    for i in range(6, 10):
        positions_alt.append(int(predict_alt[i]))
    if f_pos == 1:
        print('positions_alt')
        print(positions_alt)
    if f_pos ==1:
        print('predict_ref\tpredict_alt\tpos_snp\tsnp')
        print('{}\t{}\t{}\t{}'.format(predict_ref,predict_alt,pos_snp,snp))
        print('###################################################################################################\n')
    # проверка позиций прошла успешно
    #ALLEL|GEN|DS_AG|DS_AL|DS_DG|DS_DL|DP_AG|DP_AL|DP_DG|DP_DL)
    if (abs(probab_alt[2] - probab_ref[2]) >= 0.5) and not(abs(probab_alt[3] - probab_ref[3]) >= 0.5):
        out_dg.write(st_ref+st_alt)
        stat[0]+=1
    if not(abs(probab_alt[2] - probab_ref[2]) >= 0.5) and (abs(probab_alt[3] - probab_ref[3]) >= 0.5):
        out_dl.write(st_ref+st_alt)
        stat[1]+=1
    if (abs(probab_alt[2] - probab_ref[2]) >= 0.5) and (abs(probab_alt[3] - probab_ref[3]) >= 0.5):
        out_dgdl.write(st_ref+st_alt)
        stat[2]+=1
    if abs(probab_alt[2] - probab_ref[2]) >= 0.5 or abs(probab_alt[3] - probab_ref[3]) >= 0.5:# and not((probab_alt[2] - probab_ref[2] >= 0.5) and (probab_alt[3] - probab_ref[3] >= 0.5)):
        out_don.write(st_ref+st_alt)
        stat[3]+=1
print('Статистика')
print(lab_stat)
print(stat)
print('Сумма==all_ds?: {}'.format(sum(stat[:-1])))



out_don.close()

dinpol = open('polim_in_dinucl.vcf','r')
zag = dinpol.readline()
for st in dinpol:
    st_ref = st
    stm = st[:-1].split('\t')
    pos = int(stm[2])
    predict_ref = stm[6].split('|')
    snp = stm[5].split('|')
    pos_snp = int(snp[2])
    probab_ref = []
    for i in range(2, 6):
        probab_ref.append(float(predict_ref[i]))
    positions_ref = []
    for i in range(6, 10):
        positions_ref.append(int(predict_ref[i]))

    st = dinpol.readline()
    st_alt = st
    stm = st[:-1].split('\t')
    predict_alt = stm[6].split('|')
    probab_alt = []
    for i in range(2, 6):
        probab_alt.append(float(predict_alt[i]))
    positions_alt = []
    for i in range(6, 10):
        positions_alt.append(int(predict_alt[i]))
    chek(st_ref, st_alt, pos, pos_snp, probab_ref, probab_alt, positions_alt, er)
print('Mission completed')
print(er)


dinpol.close()
out_dg.close()
out_dl.close()
out_dgdl.close()
pred.close()
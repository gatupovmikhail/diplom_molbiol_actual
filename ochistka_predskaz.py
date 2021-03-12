# очищает от предсказаний, рядом с которыми есть полиморфизмы, между которыми расстояние менее 10 нуклеотидов
pred = open('results_filtr.vcf','r')
file_out = open('pred_filtr.vcf','w')
file_er = open('pred_remove.vcf','w')
polim = open('gnomad_polim_snp.vcf','r')
zag_pred = pred.readline()
file_out.write(zag_pred)
file_er.write(zag_pred)
nst = 0
pr = {} # ключи - хромосомы.
for st in pred:  # получение позиций мутаций и номеров строчек в pr
    nst+=1
    stm = st[:-1].split('\t')
    ch = stm[1]
    pos = int(stm[2])
    if not(ch in pr.keys()):
        pr[ch] = []
    pr[ch].append((pos,nst))
    st1 = pred.readline()
    nst+=1
#print(pr)

pred.close()


zag_polim = polim.readline() # отыскивание полиморфизмов, в которых разница меньше 10
blizkie_polim = {}
ch0 = 'chr1'
fl = 0
pos_pol0 = 0
for st in polim:
    stm = st[:-1].split('\t')
    ch = stm[0]
    if not(ch in blizkie_polim.keys()):
        blizkie_polim[ch] = []
    pos_pol = int(stm[1])
    if not(ch0 == ch):
        ch0, pos_pol0 = (ch, pos_pol)
        fl = 0
        continue
    if pos_pol - pos_pol0 < 10 and fl == 0:
        blizkie_polim[ch].append(pos_pol0)
        blizkie_polim[ch].append(pos_pol)
        fl = 1
        ch0, pos_pol0 = (ch, pos_pol)
        continue
    if pos_pol - pos_pol0 < 10 and fl == 1:
        blizkie_polim[ch].append(pos_pol)
        continue
    if pos_pol - pos_pol0 >=10:
        fl = 0
        ch0,pos_pol0 = (ch,pos_pol)

polim.close()
otfiltr = []
hren = {}
for key in pr.keys():
    for pos_pr,nst in pr[key]:
        fl = 0
        for pos_pol in blizkie_polim[key]:
            if abs(pos_pol - pos_pr) <= 5:
                fl = 1
                hren[nst] = pos_pol
                break
            if pos_pol - pos_pr > 5:
                break
        if fl == 0:
            otfiltr.append(nst)
    print(key,end =' ')
#print(otfiltr)
pred = open('results_filtr.vcf','r')
zag_pred = pred.readline()
nst = 0
for st in pred:
    nst+=1
    st_ref = st
    if nst in otfiltr:
        file_out.write(st_ref)
        nst+=1
        st_alt = pred.readline()
        file_out.write(st_alt)
        continue
    if nst in hren.keys():
        file_er.write(st_ref[:-1]+'\t{}\n'.format(hren[nst]))
        st_alt = pred.readline()
        file_er.write(st_alt[:-1] + '\t{}\n'.format(hren[nst]))
        nst+=1
        continue
    print('ERROR nst ={}'.format(nst))
    st_alt = pred.readline()
    nst+=1
file_er.close()
file_out.close() # 40844 предсказаний







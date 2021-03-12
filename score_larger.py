## Сразу две функции. Во-первых оставляет только полиморфизмы в генах Ad/AR. Потом еще оставляет только полимфорфизмы с максимальными скорами >0.1 и >0.2
import matplotlib.pyplot as plt
#gnom = open('all_gnom_variants_pred_filtr_ad_ar.vcf','r')
#gnom = open('all_gnom_variants_pred_filtr_ad.vcf','r')
gnom = open('all_gnom_variants_pred_filtr_ar.vcf','r')
#file_out = open('all_gnom_variants_pred_filtr_l_02.vcf','w')
file_out = open('all_gnom_variants_pred_filtr_ar_l_02.vcf','w')
#gen_file = open('gens_ad','r') # only ad
gen_file = open('gens_ar','r')
gen_m = []
nst=0
for stg in gen_file:
    gen_m.append(stg[0:-1])

for i in range(45):
    zag = gnom.readline()
    file_out.write(zag)
g0 = 'h'
for st in gnom:
    nst+=1
    if (nst%100000==0):
        print(nst)
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
    #gen = info.split(';')[2].replace('GEN=','')
    probab = spliceai.split('|')
    try:
        re = probab[5]
    except IndexError:
        continue
    # for g in gen_m:
    #     if gen==g0 or g==gen:
    #         file_out.write(st)
    #         g0=g
    #         break

    mmax = -1
    for j in range(2,6):
        if float(probab[j]) > mmax:
            mmax = float(probab[j])
    if mmax > 0.2:
        file_out.write(st)

gnom.close()
file_out.close()
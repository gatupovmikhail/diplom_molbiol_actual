# отфильтровывает предсказания рядом с которыми есть несколько близких snp
pred_f = open('results_filtr.vcf','w')
with open('results_un.vcf','r') as pred:
    with open('pred_with_2_polim.vcf','w') as pred2:
        with open('pred_odinak.vcf','w') as pred_same:
            zag = pred.readline()
            pred2.write(zag)
            pred_same.write(zag)
            pred_f.write(zag)
            for st in pred:
                stm = st[:-1].split('\t')
                pos = stm[2]
                snp = stm[5]
                if len(snp.split(','))>1:
                    pred2.write(st)
                    continue
                if snp.split('|')[2] == pos:
                    pred_same.write(st)
                    continue
                pred_f.write(st)
pred_f.close()

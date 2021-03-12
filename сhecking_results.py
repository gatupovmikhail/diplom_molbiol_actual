# Проверяет различные предсказания на повторяемость
with open('results_un.vcf','w') as file_out:
    with open('results.vcf','r') as res:
        st0re = 'n'
        st0al = 'n'
        n_pov = 0
        zag = res.readline()
        file_out.write(zag)
        for stre in res:
            stal = res.readline()
            if not(stre==st0re) and not(stal==st0al):
                file_out.write(stre+stal)
            if (stre==st0re) or (stal==st0al):
                print(stre+stal)
                n_pov+=1
            st0al = stal
            st0re = stre
print(n_pov)

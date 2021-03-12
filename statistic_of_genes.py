## подсчет полиморфизмов для каждого гена.
#file_gen = open('gens_spliceAI.txt','r')
file_gen = open('gens_spliceAI_sorted_concantenated.txt','r')

zag = file_gen.readline()
gens = {}
for st in file_gen:
    stm = st.split('\t')
    gen = stm[0]
    chr = stm[1]
    start = int(stm[3])
    end = int(stm[4])
    length = end - start + 1
    #gens.append((gen,chr,start,end,length,0))
    gens[gen] = [chr,start,end,length,0]
file_gen.close()
#print(len(gens.keys())) #17789
polims = open('gnomad_polim_all_filtr.vcf','r') #//per
#polims = open('polim_in_gens_form_5.txt','r')
zag = polims.readline()
nst = 0
for st in polims:
    nst+=1
    if (nst%10**7==0):
        print(nst/10**6,end=' ')
    stm = st[:-1].split('\t')
    gen = stm[6]  #//per
    #gen = stm[0]
    gens[gen][4]+=1
print(gens)
polims.close()
print('DONE_PART')
file_out = open('gens_statistic_polim.vcf','w')
gens_kom = list(gens.items())
print(gens_kom)
print(nst) # 85906651 всего полиморфизмов
#gens_sort = sorted(gens_kom,key= lambda x: x[1][3],reverse=True)
#print('DONE SORTIR')
#print(gens_sort)

file_out.write('#GEN\tCHROME\tSTART\tEND\tLENGTH\tNUMBER_OF_POLIMORFISMS\n')
for g in gens_kom:
    file_out.write('{gen}\t{ch}\t{start}\t{end}\t{length}\t{polim}\n'.format(gen=g[0],ch=g[1][0],start=g[1][1],end=g[1][2],length=g[1][3],polim=g[1][4]))
file_out.close()
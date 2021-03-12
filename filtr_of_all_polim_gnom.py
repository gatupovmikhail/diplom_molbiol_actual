# Отфильтровывает полиморфизмы. В новом файле окажутся только полиморфизмы, которые располагаются в генах
from sys import exit
gens = open('gens_spliceAI_sorted_concantenated.txt','r')
#polim = open('num_pol_new.txt','r')
#polim = open('gnomad_polim_form.vcf','r')
#file_out = open('polim_in_gens.txt','w')
polim = open('gnomad_polim_all.vcf','r') # там все полиморфизмы!
file_out = open('gnomad_polim_all_filtr.vcf','w') # а здесь только те, что в генах.
pol_gen = 0
pol_all = 0

zag_g = gens.readline()
pol = polim.readline()
file_out.write(pol[0:-1]+'\tGEN\n')

order = [1,2,3,4,5,6,7,'X',8,9,10,11,12,13,14,15,16,17,18,20,'Y',19,22,21]
empty_list1 = [[] for i in range(len(order))]
empty_list2 = [[] for i in range(len(order))]
empty_list3 = [[] for i in range(len(order))]
#chg_m = {str(k):val for k,val in zip(order,empty_list)}

gen_m = {str(k):val for k,val in zip(order,empty_list1)}
start_m = {str(k):val for k,val in zip(order,empty_list2)}
end_m = {str(k):val for k,val in zip(order,empty_list3)}

for genst in gens:
    genm = genst.split('\t')
    chg = genm[1]
    gen_m[chg].append(genm[0])
    start_m[chg].append(int(genm[3]))
    end_m[chg].append(int(genm[4]))
print(gen_m)
print(start_m)
print(end_m)

chp0 = '0'
for pol in polim:
    pol_all += 1
    # if pol_gen > 500:
    #     break
    chp = pol.split('\t')[0].replace('chr', '')
    chp = chp.replace('$', '')
    if not(chp0 == chp):
        print(chp,end=' ')
        chp0 = chp
    pos = int(pol.split('\t')[1])

    for i in range(len(gen_m[chp])):
        if (start_m[chp][i] <= pos <= end_m[chp][i]):
            pol_gen+=1
            file_out.write(pol[0:-1] + '\t{}\n'.format(gen_m[chp][i]))
            break
        if (pos < start_m[chp][i]):
            break

# file_log = open('polimorf_in_gens_log.txt','w')
# file_log.close()
print('pol_gen {}\n'.format(pol_gen))
print('pol_negen {}\n'.format(pol_all-pol_gen))
print('pol_all {}\n'.format(pol_all))
print('persent gen {}\n'.format(pol_gen/pol_all))

polim.close()
gens.close()
file_out.close()



# ch_m = []
# start_m = []
# end_m = []
# chp = '2'
# ch = '0'
# while not ch == chp:
#     gen = gens.readline()
#     genm = gen.split('\t')
#     ch = genm[1]
#     if ch == chp:
#         ch_m.append(ch)
#         start_m.append(int(genm[3]))
#         end_m.append(int(genm[4]))
# while ch == chp:
#     gen = gens.readline()
#     genm = gen.split('\t')
#     ch = genm[1]
#     if ch == chp:
#         ch_m.append(ch)
#         start_m.append(int(genm[3]))
#         end_m.append((genm[4]))


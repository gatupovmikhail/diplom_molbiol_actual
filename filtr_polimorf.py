# Отфильтровывает полиморфизмы. В новом файле окажутся только полиморфизмы, которые располагаются в генах
from sys import exit
gens = open('gens_spliceAI_sorted_concantenated.txt','r')
#polim = open('num_pol_new.txt','r')
polim = open('gnomad_polim_form.vcf','r')
file_out = open('polim_in_gens.txt','w')
chp = '1'
chg = '0'
gen_last = ''
polim_last = ''
pol_gen = 0
pol_all = 0
fl = 0
zag_g = gens.readline()
for pol in polim:
    if fl == 0:
        fl =1
        continue
    pol_all += 1
    chp = pol.split('\t')[0].replace('chr', '')
    pos = int(pol.split('\t')[3]) * 50 + int(pol.split('\t')[4].split(',')[0])

    if not(chg == chp):
        gen_m = []
        start_m = []
        end_m = []
        if not(gen_last == ''):
            print(gen_last)
            gen_m.append(gen_last.split('\t')[0])
            start_m.append(int(gen_last.split('\t')[3]))
            end_m.append(int(gen_last.split('\t')[4]))
        chg = chp
        while chg == chp:
            gen = gens.readline()
            if len(gen.split('\t')) < 2:
                break
            try:
                genm = gen.split('\t')
            except IndexError:
                print('Error')
                print(gen)
                print(chg)
                exit()
            chg = genm[1]
            if chg == chp:
                gen_m.append(genm[0])
                start_m.append(int(genm[3]))
                end_m.append(int(genm[4]))
            else:
                gen_last = gen
        chg = chp
        #for i in range(len(gen_m)):
            #print('{}\t{}\t{}'.format(gen_m[i],start_m[i],end_m[i]))
    for i in range(len(gen_m)):
        if start_m[i] <= pos <= end_m[i]:
            pol_gen+=1
            file_out.write(pol[0:-1] + '||{}\n'.format(gen_m[i]))
            break
file_log = open('polimorf_in_gens_log.txt','w')
file_log.write('pol_gen {}\n'.format(pol_gen))
file_log.write('pol_negen {}\n'.format(pol_all-pol_gen))
file_log.write('pol_all {}\n'.format(pol_all))
file_log.write('persent gen {}\n'.format(pol_gen/pol_all))
file_log.close()





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
polim.close()
gens.close()
file_out.close()

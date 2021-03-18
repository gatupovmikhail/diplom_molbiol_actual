#строит гистограммы зависимостей полим(длина), диф.пред(полим), диф.пред(длина)
import numpy as np
import matplotlib.pyplot as plt
gens_stat = open('gens_statistic_polim.vcf','r')
zag = gens_stat.readline()
gens = {}
for st in gens_stat:
    stm = st[:-1].split(('\t'))
    gen,chr,length,polim = (stm[0],stm[1],stm[4],stm[5])
    gens[gen] = [int(length),int(polim)]
print(gens)
gens_stat.close()

dif_pred = open('statistic_dist_polims.vcf','r')
name_gen = [np.nan]*11002
length_gen = [np.nan]*11002
polim_gen = [np.nan]*11002
pred_gen = [np.nan]*11002
n = 0
print('NO gens:')
ng = 0
for st in dif_pred:
    stm = st.split('\t')
    gen = stm[0]
    kolvoPred = int(stm[1])
    if st=='':
        break
    try:
        gens[gen].append(kolvoPred)
        name_gen[n],length_gen[n],polim_gen[n],pred_gen[n] = (gen,gens[gen][0],gens[gen][1],gens[gen][2])
        n+=1
    except KeyError:
        ng+=1
        print(gen,end=' ')
print(ng)
dif_pred.close()
print(length_gen)
print(polim_gen)
#print(length_gen[len(name_gen)-1])
# with open('errors_in_gens','r') as err:  ######
#     zag = err.readline()
#     for st in err:
#         stm = st[:-1].split('\t')


# plt.scatter(length_gen,polim_gen)
# plt.grid(True)
# plt.title('Length and polimorfisms of gens')
# plt.xlabel('Length of gen')
# plt.ylabel('Number of polimorfisms')
# plt.show()
#
# plt.scatter(length_gen,pred_gen)
# plt.grid(True)
# plt.title('Length and different predictions in gens')
# plt.xlabel('Length of gen')
# plt.ylabel('Number of different predictions')
# plt.show()
#
# #plt.scatter(np.log(np.array(polim_gen)+1),np.log(np.array(pred_gen)+1))
# plt.scatter(polim_gen,pred_gen)
# plt.grid(True)
# plt.title('Polimorfisms and different predictions in gens')
# plt.xlabel('Number of polimorfisms')
# plt.ylabel('Number of different predictions')
# plt.show()
# err = open('errors_in_gens','w')
#
# err.write('#GEN\tLENGTH\tNUMBER_OF_POLIMORFISMS\tPREDICTIONS\n')
# for n in range(len(name_gen)):
#     if polim_gen[n] == 0 and not(pred_gen[n] == 0):
#         err.write('{}\t{}\t{}\t{}\n'.format(name_gen[n],length_gen[n],polim_gen[n],pred_gen[n]))
#
# err.close()
help(plt.axes)


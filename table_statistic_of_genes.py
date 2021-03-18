# Подсчет различной статистики по различающимся предсказаниям. ТАМ КУЧА ВЫХОДНЫХ ФАЙЛОВ!
# https://habr.com/ru/post/468295/ 50 оттенков matplotlib
import matplotlib.pyplot as plt
import numpy as np
# from prettytable import PrettyTable
# from prettytable import DEFAULT, MSWORD_FRIENDLY, MARKDOWN, PLAIN_COLUMNS, ORGMODE
# import matplotlib.pyplot as plt
import pandas as pd
from sys import exit
import openpyxl


#difference_0 - все, в которых разница в позициях нуль
#difference_1 - все, в которых разница в позициях нуль
#difference_2 - все, в которых разница в позициях нуль
#difference_3 - все, в которых разница в позициях нуль
# position_0.vcf - Все, с позицией ноль.
# 3_4 sites.vcf - 3 and 4 different sites
# ds_dg+ds_dl.vcf - одновременное происхождение донорных и акцепотрных сайтов сплайсинга
# mutations_in_donor_dinucl.vcf - мутации, которые обязательно затрагивают нуклеотид, либо пол. рядом с ними затрагивает динукл.
# при этом мутации обязаны лежать в GGTA
# polim_in_dinucl.vcf мутация не лежит в GGTA, но при этом полиморфизм лежит в GGTA

def new_raznica(chr, pos, prob_ref, prob_alt, razn, pos_sites_ref, pos_sites_alt, pos_snp,st_ref,st_alt,file_izv,two_sites):
    fl = 0
    si = 0
    for i in range(4):
        if (abs(prob_alt[i] - prob_ref[i]) >= 0.5):  # here
            si = i
            fl+=1
    if fl == 1:
        razn[si]+=1
    if fl == 2: ### fl > 1 всего 2 с более чем 2 сайтами
        razn[4]+=1
def in_ss_pos(mut_gen,mut_ss,pol_gen): # система координат -2-1+1+2 не используется! вместо нее -2-1,0,+1+2. То есть 0 - это +1 и т. д.
    delta = pol_gen - mut_gen
    if mut_ss > 0:
        mut_ss = mut_ss - 1
    if mut_ss == 0:
        return 10**4
    return mut_ss + delta

def app_disapp_case(prob_ref, prob_alt,lessmore,st_ref,st_alt):
# подсчитывает кол-во предсказаний, в которых вероятность больше 50% и меньше 50 % По словам Скоблова. эта статистика бесполезна
    fl = -1
    for i in range(4):
        if ((prob_alt[i] - prob_ref[i]) >= 0.5):
            if fl==1 or fl==2:
                fl = 2
            else:
                fl = 0
        if ((prob_ref[i] - prob_alt[i]) >= 0.5):
            if fl == 0 or fl==2:
                fl = 2
            else:
                fl = 1
    if not fl == -1:
        lessmore[fl]+=1
    if fl == -1:
        #file_izv.write(st_ref+st_alt)
        print('ERROR')

def dinucl_new(chr, pos, prob_ref, prob_alt,pos_snp,pos_sites_ref,pos_sites_alt,din,fign,st_ref,st_alt,file_izv):
    f = 0
    pos_snp_p = pos_snp[0] # только для файла с одним полиморфизмом !
    dist = pos - pos_snp_p # тоже !
    flag_don = [0] * 4
    pos_dist = [(-1, -1), (1, 1), (1, -1), (2, 1), (2, -1), (3, 1)]
    for i in [2, 3]:  # ds_dg and ds_dl
        if ((prob_alt[i] - prob_ref[i]) >= 0.5):
            flag_don[i] = 1
    for i in [2, 3]:  # ds_dg and ds_dl
        if ((prob_ref[i] - prob_alt[i]) >= 0.5):
            flag_don[i - 2] = 1
    if sum(flag_don) == 1:
        ind = flag_don.index(1)
        if ind < 2:

            for (k,(ps,delta)) in enumerate(pos_dist):
                if pos_sites_alt[p] == ps and dist == delta:
                    din[k]+=1





def dinucl(chr, pos, prob_ref, prob_alt,pos_snp,pos_sites_ref,pos_sites_alt,din,fign,st_ref,st_alt,file_izv):
    ## ['mpTA','pmTA','GmpA','GpmA','GGmp','GGpm','other'] #GGTA [(-1,-1),(1,1),(1,-1),(2,1),(2,-1),(3,1)]
    p = -1
    fl = 0
    pos_snp_p = pos_snp[0] # только для файла с одним полиморфизмом !
    dist = pos - pos_snp_p # тоже !


    pos_dist = [(-1,-1),(1,1),(1,-1),(2,1),(2,-1),(3,1)]
    fl_site = 0
    if p > -1 and fl > 0: # fl == 1
        for (k,(ps,delta)) in enumerate(pos_dist):
            if pos_sites_alt[p] == ps and dist == delta:
                din[k]+=1
                fl_site = 1
                #file_izv.write(st_alt+st_ref)
                break

        if fl_site == 0 and ( (in_ss_pos(pos,pos_sites_alt[p],pos_snp_p)==0) or (in_ss_pos(pos,pos_sites_alt[p],pos_snp_p)==1) ):
            assert p >-1
            fl_site=1
            din[6]+=1
            #file_izv.write(st_ref+st_alt)
        if fl_site == 0:
            din[7] += 1

        p = -1
        fl = 0
        pos_snp_p = pos_snp[0]  # только для файла с одним полиморфизмом !
        dist = pos - pos_snp_p  # тоже !
        for i in range(2, 4):  # ds_ag and ds_dl
            if ((prob_ref[i] - prob_alt[i]) >= 0.5):
                fl += 1
                p = i

        pos_dist = [(-1, -1), (1, 1), (1, -1), (2, 1), (2, -1), (3, 1)]
        fl_site = 0
        if p > -1 and fl > 0:  # fl == 1
            for (k, (ps, delta)) in enumerate(pos_dist):
                if pos_sites_ref[p] == ps and dist == delta:
                    din[k] += 1
                    fl_site = 1
                    # file_izv.write(st_alt+st_ref)
                    break

            if fl_site == 0 and ((in_ss_pos(pos, pos_sites_ref[p], pos_snp_p) == 0) or (
                    in_ss_pos(pos, pos_sites_ref[p], pos_snp_p) == 1)):
                assert p > -1
                fl_site = 1
                din[6] += 1

        if fl_site == 0:
            din[7] += 1

    if fl == 2:
        fign+=1
        #file_izv.write(st_ref+st_alt)










def raznica(chr, pos, prob_ref, prob_alt, razn, pos_sites_ref, pos_sites_alt, pos_snp,st_ref,st_alt,file_izv,two_sites):
    fla = 0
    flr = 0
    pos_snp = np.array(pos_snp)
    dist = min(abs(pos_snp-pos))
    if 0 <= dist <= 5:
        j = dist

    num_re = -1
    num_al = -1
    num_x = -1
    num_y = -1
    for i in range(4):
        if ((prob_alt[i] - prob_ref[i]) >= 0.5):
            #razn[j][i] += 1
            fla += 1
            if fla==1:
                num_al=i
                if num_x == -1:
                    num_x = i
                else:
                    num_y = i
            if fla==2:
                num_y = i
            if -5 <= pos_sites_alt[i] <= 5:
                pos_stat_alt[j][str(pos_sites_alt[i])] += 1
                # if pos_sites_alt[i] == 0 and not(fl > 1): ###
                #     file_izv.write(st_ref+st_alt)
            else:
                pos_stat_alt[j]['more'] += 1
        if ((prob_ref[i] - prob_alt[i]) > 0.5):
            #razn[j][i + 4] += 1
            flr += 1
            if flr==1:
                num_re = i
                if num_x ==-1:
                    num_x = i+4
                else:
                    num_y=i+4
            if flr==2:
                num_y=i+4
            if -5 <= pos_sites_ref[i] <= 5:
                pos_stat_ref[j][str(pos_sites_ref[i])] += 1
                # if pos_sites_ref[i] == 0 and not(fl > 1):  ###
                #     file_izv.write(st_ref+st_alt)
            else:
                pos_stat_ref[j]['more'] += 1
    if flr==1 and fla==0:
        razn[j][num_re + 4] += 1
        two_sites[num_y][num_x]+=1
    if flr==0 and fla==1:
        razn[j][num_al] += 1
    if 1 < flr+fla <= 2:
        razn[j][8] += 1
    if 2 < flr+fla <= 3:   # всего 2 позиции
        razn[j][9] += 1
        file_izv.write(st_ref+st_alt)
    if flr+fla > 3:
        razn[j][10] += 1
        file_izv.write(st_ref + st_alt)
    #num_razn.append(chr+pos)


def gen_razn(gen, gens_stat):
    if not (gen in gens_stat.keys()):
        gens_stat[gen] = 1
    else:
        gens_stat[gen] += 1


file_izv = open('def.vcf','w')
#prediction = open('results_un.vcf','r')
prediction = open('pred_filtr.vcf','r')
# prediction = open('results.vcf','r')
file_out = open('statistic_dist_polims.vcf', 'w')
zag = prediction.readline()
file_izv.write(zag)
print(zag)
razn = [[0] * 11 for i in range(6)]  # различающиеся предсказания
razn_sum = [0]*5
num_razn = []  # для мутаций, у которых отличия в двух вероятностях
gens_stat = {}  # для подсчета кол-ва отличий в предсказаниях по генам
pos_stat_alt = [{} for i in range(6)] # для статистики по позициям. В каком нуклеотиде изменение
pos_stat_ref = [{} for i in range(6)]
two_sites = [[0]*8 for i in range(8)]
din = [0]*8
lessmore = [0]*3
lab_lessmore=['appearance of event','disappearance of event','appearance+disappearance \n of different events']
for j in range(-5, 6):
    for i in range(6):
        pos_stat_alt[i][str(j)] = 0
for j in range(-5, 6):
    for i in range(6):
        pos_stat_ref[i][str(j)] = 0
for i in range(6):
    pos_stat_ref[i]['more'] = 0
    pos_stat_alt[i]['more'] = 0

nst = 0
for st in prediction:
    # if nst > 10000:
    # break
    nst += 1
    st_ref = st
    stm = st[:-1].split('\t')
    type = stm[0]
    chr = stm[1].replace('chr', '')
    pos = int(stm[2])
    ref_ref = stm[3]
    alt_ref = stm[4]
    snp = stm[5]
    pos_snp = []
    for el in snp.split(','):
        pos_snp.append(int(el.split('|')[2]))
    info = stm[6]
    infom = info.split('|')
    gen = infom[1]
    prob_ref = []
    prob_ref.append(float(infom[2]))  # ds_ag
    prob_ref.append(float(infom[3]))  # ds_al
    prob_ref.append(float(infom[4]))  # ds_ag
    prob_ref.append(float(infom[5]))  # ds_dl
    pos_sites_ref = []
    for k in range(6, 10):
        pos_sites_ref.append(int(infom[k]))
    st = prediction.readline()  # четное кол-во строк должно быть
    st_alt = st
    nst += 1
    stm = st[:-1].split('\t')
    type_alt = stm[0]
    ref_alt = stm[3]
    alt_alt = stm[4]
    #snp = stm[5]
    info = stm[6]
    infom = info.split('|')
    prob_alt = []
    prob_alt.append(float(infom[2]))  # ds_ag
    prob_alt.append(float(infom[3]))  # ds_al
    prob_alt.append(float(infom[4]))  # ds_dg
    prob_alt.append(float(infom[5]))  # ds_dl
    pos_sites_alt = []
    for k in range(6, 10):
        pos_sites_alt.append(int(infom[k]))
    # podschet of predictions
    #raznica(chr, pos, prob_ref, prob_alt, razn, pos_sites_ref, pos_sites_alt, pos_snp,st_ref,st_alt,file_izv,two_sites)
    new_raznica(chr, pos, prob_ref, prob_alt, razn_sum, pos_sites_ref, pos_sites_alt, pos_snp, st_ref, st_alt, file_izv,two_sites)
    gen_razn(gen, gens_stat)
    fign = 0
    dinucl(chr, pos, prob_ref, prob_alt,pos_snp,pos_sites_ref,pos_sites_alt,din,fign,st_ref,st_alt,file_izv)
    app_disapp_case(prob_ref, prob_alt, lessmore,st_ref,st_alt)


lab_din = ['mpTA','pmTA','GmpA','GpmA','GGmp','GGpm','Polimorfism\nin GT','Other\ndonor\nsites'] #GGTA [(-1,-1),(1,1),(1,-1),(2,1),(2,-1),(3,1)]
# нужна сортировка количества мутаций по генам
print(str(razn) + '\trazn')
gens_stat = sorted(gens_stat.items(), key=lambda x: x[1], reverse=True)
for g in gens_stat:
    file_out.write('{}\t{}\n'.format(g[0],g[1]))

print(str(pos_stat_alt) + '\tpos_stat_alt\n')
print(str(pos_stat_ref) + '\tpos_stat_ref\n')
prediction.close()
file_out.close()
col = ['ds_ag_alt', 'ds_al_alt', 'ds_dg_alt', 'ds_dl_alt', 'ds_ag_ref', 'ds_al_ref', 'ds_dg_ref','ds_dl_ref']
#### DataFrames
razn_d = pd.DataFrame(razn,columns = ['ds_ag_alt', 'ds_al_alt', 'ds_dg_alt', 'ds_dl_alt', 'ds_ag_ref', 'ds_al_ref', 'ds_dg_ref','ds_dl_ref', '2 sites','3 sites','4 sites'])
#razn_d.to_csv('raznica_statistic.csv')
# for i in range(len(razn)):
#     razn_d.loc[i] = razn[i]
print(razn_d)
pos_stat_ref_d = pd.DataFrame(pos_stat_ref)
print(pos_stat_ref_d)
print()
pos_stat_alt_d = pd.DataFrame(pos_stat_alt)
print(pos_stat_alt_d)
two_sites_d = pd.DataFrame(two_sites,columns =col,index=col)
print(two_sites_d)
two_sites_d.to_csv('two_sites.csv')
# https://python-school.ru/pandas-excel/








# razn_t = PrettyTable()
# razn_t.field_names = ['ds_ag_alt', 'ds_al_alt', 'ds_dg_alt', 'ds_dl_alt', 'ds_ag_ref', 'ds_al_ref', 'ds_dg_ref',
#                       'ds_dl_ref', '2 sites']
# razn_t.add_row(razn)
# razn_t.align = 'r'
# print(razn_t)

# pos_stat_ref_t = PrettyTable()
# pos_stat_ref_t.field_names = ['Position in splicing site', 'Number of mutations']
# for g in pos_stat_ref.keys():
#     pos_stat_ref_t.add_row([g, pos_stat_ref[g]])
# pos_stat_ref_t.align = 'r'
# print(pos_stat_ref_t)
# pos_stat_alt_t = PrettyTable()
# pos_stat_alt_t.field_names = ['Position in splicing site', 'Number of mutations']
# for g in pos_stat_alt.keys():
#     pos_stat_alt_t.add_row([g, pos_stat_alt[g]])
# pos_stat_alt_t.align = 'r'
# print(pos_stat_alt_t)
# gens_stat_t = PrettyTable()
# gens_stat_t.field_names = ['Gen', 'Number of mutations']
# n = 0
# for g in gens_stat:
#     gens_stat_t.add_row(list(g))
#     n += 1
#     if n == 20: break
# gens_stat_t.align = 'r'
# # gens_stat_t.set_style(ORGMODE)
# print(gens_stat_t)
#
# fig, ax = plt.subplots(figsize=(10, 10))
# plt.bar(['ds_ag_alt', 'ds_al_alt', 'ds_dg_alt', 'ds_dl_alt', 'ds_ag_ref', 'ds_al_ref', 'ds_dg_ref', 'ds_dl_ref', '2 sites'],razn)
# plt.grid(True)
# plt.show()
# plt.bar(list(pos_stat_ref.keys()), list(pos_stat_ref.values()))
# plt.grid(True)
# plt.show()
# plt.bar(list(pos_stat_alt.keys()), list(pos_stat_alt.values()))
# plt.grid(True)
# plt.show()
file_izv.close()
plt.bar(['AG', 'AL', 'DG', 'DL','two_sites'],razn_sum)
for i,t in enumerate(razn_sum):
    plt.text(i,t+0.01*t,(str(t)),horizontalalignment='center')
plt.xlabel('sites')
plt.ylabel('Number of predictions')
plt.title('Appearing/disappearing of sites')
#plt.grid(True)
plt.show()
print(sum(razn_sum))
print('fign={}'.format(fign))
plt.bar(lab_din,din)
for i,t in enumerate(din):
    plt.text(i,t+0.01*t,(str(t)),horizontalalignment='center')
plt.text(i,-50,'GGTA')
plt.xlabel('Sites')
plt.ylabel('Number of predictions')
plt.title('Mutations in different positions of donor sites')
#plt.grid(True)
plt.show()
lab_din2 = ["Mutations or polimorfisms, \n located in GT","Mutations and polimorfisms, \n which don't interrupt GT"]
S_loc= sum(din[:-1])
ss = sum(din)
print(ss)
print(din[len(din)-1])
plt.pie([S_loc,din[len(din)-1]],labels=lab_din2,autopct=lambda x: int(round(x/100*ss)))
plt.show()
# s_lessmore = sum(lessmore)
# print(s_lessmore)
# plt.pie(lessmore,labels=lab_lessmore,autopct=lambda x: int(round(x/100*s_lessmore)))
# plt.show()
#print(lab_din)
#print(din)

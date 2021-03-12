# Считает score для генов

import openpyxl

def zagprint(name_file):
    with open(name_file) as mfile:
        zag = mfile.readline()
        first_str=mfile.readline()
        first_str=first_str.split('\t')
        zag=zag.split('\t')
        for j in range(len(zag)):
            print('{} [{}] | {}'.format(zag[j],j,first_str[j]))

def cheq_freq(stm):
    flag = 0
    for j in range(10, 44):
        if (stm[j] == '.'):
            continue
        else:
            flag = 1
    if (flag == 1):
        return True
    else:
        return False

genes_ad={}
genes_ar={}
genes_adar={}

allgenes_ad={}
allgenes_ar={}
allgenes_adar={}

wb = openpyxl.load_workbook(filename = 'my_genes.xlsx')
sheet=wb['AD mapped']
for cell in sheet['C']:
    genes_ad[cell.value]=0
    allgenes_ad[cell.value] = 0

sheet=wb['AR mapped']
for cell in sheet['C']:
    genes_ar[cell.value]=0
    allgenes_ar[cell.value] = 0

sheet=wb['AD_AR mapped']
for cell in sheet['C']:
    genes_adar[cell.value]=0
    allgenes_adar[cell.value] = 0

# print(genes_ad.keys())
# print(genes_ar.keys())
# print(genes_adar.keys())
name_file='itog_annotate.txt'
#zagprint(name_file)



with open(name_file) as mfile:
    zag=mfile.readline()

    print(len([]))
    for st in mfile:
        stm=st.split('\t')
        if(stm[55][0:-1]=='AD'):
            allgenes_ad[stm[6]]+=1
            if (cheq_freq(stm)):
                genes_ad[stm[6]]+=1

        if (stm[55][0:-1] == 'AR'):
            allgenes_ar[stm[6]] += 1
            if (cheq_freq(stm)):
                genes_ar[stm[6]] += 1

        if (stm[55][0:-1] == 'AD_AR'):
            allgenes_adar[stm[6]] += 1
            if (cheq_freq(stm)):
                genes_adar[stm[6]] += 1

name_file_out='genes_score_ad'
file_out=open(name_file_out,'w')
file_out.write('AD genes \n')
for k in genes_ad.keys():
    if not(allgenes_ad[k]==0):
        file_out.write('{}: {} all_rows: {} \n'.format(k,genes_ad[k]/allgenes_ad[k],allgenes_ad[k]))
    else:
        file_out.write('{}: {} all_rows: {} \n'.format(k,0,0))
file_out.close()

name_file_out='genes_score_ar'
file_out=open(name_file_out,'w')
file_out.write('AR genes \n')
for k in genes_ar.keys():
    if not(allgenes_ar[k]==0):
        file_out.write('{}: {} all_rows: {} \n'.format(k,genes_ar[k]/allgenes_ar[k],allgenes_ar[k]))
    else:
        file_out.write('{}: {} all_rows: {} \n'.format(k,0,0))
file_out.close()

name_file_out='genes_score_adar'
file_out=open(name_file_out,'w')
file_out.write('AD_AR genes \n')
for k in genes_adar.keys():
    if not(allgenes_adar[k]==0):
        file_out.write('{}: {} all_rows: {} \n'.format(k,genes_adar[k]/allgenes_adar[k],allgenes_adar[k]))
    else:
        file_out.write('{}: {} all_rows: {} \n'.format(k,0,0))
file_out.close()










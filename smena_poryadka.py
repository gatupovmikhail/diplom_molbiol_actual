from sys import exit
from my_library import writting_file, checkfile, zagprint, few_columns

file_ref=open('genom.fa','r')

file_out=open('gens_spliceAI_sorted.txt','w')

chgm=[]
for st in file_ref:
    if st[1:-1]=='chr6_ssto_hap7':
        break
    if ('>' in st):
        if not(st[1:-1] in chgm):
            chgm.append(st[1:-1])
file_ref.close()

print(chgm)

with open('gens_spliceAI.txt','r') as file_change:
    zag=file_change.readline()
    file_out.write(zag)


ch_ch=[]

for chg in chgm:
    with open('gens_spliceAI.txt','r') as file_change:
        fl = 0
        for st in file_change:
            stm=st.split('\t')
            ch='chr'+stm[1]
            if chg==ch and fl==1:
                file_out.write(st)
            fl=1



file_out.close()

# file_out=open('gens_all_sorted.txt','r')
#
# ch_ch = []
# ch0 = ''
# for st in file_out:
#     stm = st.split('\t')
#     if not (stm[2] == ch0):
#         ch_ch.append(stm[2])
#         ch0 = stm[2]
#
# print(ch_ch)
#
# file_out.close()
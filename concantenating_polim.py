# Соединяет перекрывающиеся области у полиморфизмов.
from sys import exit
#polim = open('polim_in_gens_form_razn.txt','r')
polim = open('polim_in_gens_form_razn_5.txt','r')
#file_out = open('polim_in_gens_form_concan.txt','w')
file_out = open('polim_in_gens_form_concan_5.txt','w')
# polim = open('polim_in_gens_form_concan.txt','r')    FOR CHECKING
# file_out = open('polim_in_gens_form_check.txt','w')
zag = polim.readline()
print(repr(zag))
file_out.write(zag)
num = 0
st0 = polim.readline()
num+=1
stm0 = st0[0:-1].split('\t')
ch0 = stm0[1]
pos0 = int(stm0[4])
pos_out0 = str(pos0)
refalt0 = stm0[5]
idd0 = stm0[6]
af0 = stm0[7]
refalt_out0 = refalt0
polim_odinak = 0
st_l = st0
pos_l = pos0
refalt_l=refalt0
idd_l = idd0
af_l = af0
for st in polim:
    num+=1
    stm = st[0:-1].split('\t')
    ch = stm[1]
    pos = int(stm[4])
    refalt = stm[5]
    idd = stm[6]
    af = stm[7]
    if ((pos - pos0) > 10) or not(ch == ch0):
        file_out.write(st0)
        st_l = st0
        pos_l = pos0
        refalt_l = refalt0
        idd_l = idd0
        af_l = af0
        st0 = st
        stm0 = st0[0:-1].split('\t')
        ch0 = stm0[1]
        #pos0 = int(stm0[4])
        pos0 = pos
        refalt0 = refalt
        pos_out0 = str(pos0)
        refalt_out0 = refalt0
        idd_out0 = idd0
        af_out0 = af0
    else:
        # if ch == ch0:
        #     print('WARNING')
        #     print(num)
        #     exit()
        gen = stm[0]
        start = stm0[2]
        end = stm[3]
        refalt = stm[5]
        idd = stm[6]
        af = stm[7]
        pos_out = '{},{}'.format(pos_out0,pos)
        refalt_out = '{},{}'.format(refalt_out0,refalt)
        idd_out = '{},{}'.format(idd_out0,idd)
        af_out = '{},{}'.format(af_out0,af)
        st_l = st0
        pos_l = pos0
        refalt_l = refalt0
        st0 = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(gen, ch, start, end, pos_out, refalt_out, idd_out, af_out)
        stm0 = st0[0:-1].split('\t')
        ch0 = stm0[1]
        pos0 = pos
        refalt0 = refalt
        pos_out0 = pos_out
        refalt_out0 = refalt_out
        idd_out0 = idd_out
        af_out0 = af_out

st0 = st_l
stm0 = st0[0:-1].split('\t')
ch0 = stm0[1]
pos0 = pos_l
refalt0 = refalt_l
pos_out0 = stm0[4]
refalt_out0 = stm0[5]
idd_out0 = stm0[6]
af_out0 = stm0[7]
if (pos - pos0 > 10):
    file_out.write(st)
else:
    gen = stm[0]
    start = stm0[2]
    end = stm[3]
    refalt = stm[5]
    idd = stm[6]
    af = stm[7]
    pos_out = '{},{}'.format(pos_out0, pos)
    refalt_out = '{},{}'.format(refalt_out0,refalt)
    idd_out = '{},{}'.format(idd_out0,idd)
    af_out = '{},{}'.format(af_out0,af)
    st0 = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(gen, ch, start, end, pos_out, refalt_out, idd_out, af_out)
    file_out.write(st0)

print(polim_odinak)
print(num)
polim.close()
file_out.close()
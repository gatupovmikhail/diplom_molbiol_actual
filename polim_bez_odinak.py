# Убирает полиморфизмы, имеющие одну и ту же позицию
#polim = open('polim_in_gens_form.txt','r')
polim = open('polim_in_gens_form_5.txt','r')
#file_out = open('polim_in_gens_form_razn.txt','w')
file_out = open('polim_in_gens_form_razn_5.txt','w')
zag = polim.readline()
file_out.write(zag)
num = 0
st0 = polim.readline()
num+=1
stm0 = st0.split('\t')
ch0 = stm0[1]
pos0 = int(stm0[4])
polim_odinak = 0
st_l = ''
for st in polim:
    num+=1
    stm = st.split('\t')
    ch = stm[1]
    pos = int(stm[4])
    if not(pos == pos0) or not(ch == ch0): # Полиморфизмы с одинаковыми позициями. Убираем.
        file_out.write(st0)
    else:
        polim_odinak+=1

    st_l = st0
    st0 = st
    stm0 = st0.split('\t')
    ch0 = stm0[1]
    pos0 = int(stm0[4])

st0 = st_l
stm0 = st0.split('\t')
ch0 = stm0[1]
pos0 = int(stm0[4])
if not(pos == pos0) or not(ch == ch0): # Полиморфизмы с одинаковыми позициями. Убираем.
    file_out.write(st)
else:
    polim_odinak+=1
print(polim_odinak)
polim.close()
file_out.close()
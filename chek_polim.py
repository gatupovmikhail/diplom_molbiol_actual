from sys import exit
polim = open('polim_in_gens_form_concan.txt','r')
#file_out = open('polim_in_gens_form_concan.txt','w')
zag = polim.readline()
num = 0
st0 = polim.readline()
num+=1
stm0 = st0[0:-1].split('\t')
ch0 = stm0[1]
start0 = int(stm0[3])
end0 = int(stm0[4])
st_l = st0
for st in polim:
    num+=1
    stm = st[0:-1].split('\t')
    ch = stm[1]
    start = int(stm[3])
    end = int(stm[4])
    if (start <= end0) and (ch == ch0):
        print('WARNING')
        print(num)
        print(start)
        print(end0)
        exit()
    st0 = st
    stm0 = st0[0:-1].split('\t')
    ch0 = stm0[1]
    start0 = int(stm0[3])
    end0 = int(stm0[4])
    st_l = st0



print(num)
polim.close()
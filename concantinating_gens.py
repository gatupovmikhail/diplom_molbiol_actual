from sys import exit
from my_library import writting_file, checkfile, zagprint, few_columns

name_fgens='gens_spliceAI_sorted.txt'
zagprint(name_fgens)
name_file_out='gens_spliceAI_sorted_concantenated.txt'
file_out=open(name_file_out,'w')
with open(name_fgens) as mfile:
    num=0
    zag=mfile.readline()
    file_out.write(zag)
    st0=mfile.readline()
    stm0=st0.split('\t')
    ch0 = stm0[1]
    start0=int(stm0[3])
    end0=int(stm0[4])
    for st in mfile:
        num+=1
        #print(num)
        stm=st.split('\t')
        ch=stm[1]
        start=int(stm[3])
        end=int(stm[4])
        fl=0
        if start<=end0 and end0<=end and ch0==ch:
            st_out=''
            for j in range(3):
                st_out+=stm0[j]+'\t'
            st_out+=str(start0)+'\t'+str(end)+'\t'
            for j in range(5,len(stm)-1):
                st_out+=stm[j]+'\t'
            st_out+=stm[len(stm)-1]
            fl=1
            #file_out.write(st_out)

            st0=st_out
            stm0 = st0.split('\t')
            start0 = int(stm0[3])
            end0 = int(stm0[4])
            ch0=stm0[1]
        if start <= end0 and end0 > end and fl==0 and ch0==ch:
            st_out = ''
            for j in range(3):
                st_out += stm0[j] + '\t'
            st_out += str(start0)+'\t' + str(end0)+'\t'
            for j in range(5, len(stm) - 1):
                st_out += stm[j] + '\t'
            st_out += stm[len(stm) - 1]
            fl = 1
            #file_out.write(st_out)

            st0 = st_out
            stm0 = st0.split('\t')
            start0 = int(stm0[3])
            end0 = int(stm0[4])
            ch0 = stm0[1]
        if fl==0:
            file_out.write(st0)
            st0 = st
            stm0 = stm
            start0 = start
            end0 = end
            ch0=ch
file_out.write(st)
file_out.close()
print(num)
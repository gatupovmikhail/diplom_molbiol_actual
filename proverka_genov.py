file_out=open('gens_splice_er.txt','w')
with open('gens.txt') as mfile:
    st0=''
    for st in mfile:
        if ('>' in st):
            st0=st
        if ('$' in st):
            stm=st.split('\t')
            ref=int(stm[2])
            rel=int(stm[4][1:])
            if not(ref+1==rel):
                file_out.write(st0)
                file_out.write(str(rel-ref+1) + '\t' + st)

file_out.close()
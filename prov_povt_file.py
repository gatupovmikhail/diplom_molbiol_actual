povt = 0
with open('splice_onegen_alt1.tsv','r') as mfile:
    st = '#'
    while ('#' in st):
        st = mfile.readline()
    pos0 = int( st.split('\t')[1])
    i = 1
    for st in mfile:
        pos =int( st.split('\t')[1])
        if pos == pos0:
            i+=1
            if i > 3:
                povt += 1
        else:
            i = 1
        pos0 = pos
print(povt)


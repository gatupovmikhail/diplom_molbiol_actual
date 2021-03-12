file_ref = open('important_gens.txt','r')
polim = open('polim_in_gens_form_razn.txt','r')
file_out = open('polim_in_gens_razn_otobr.txt','w')
zag = file_ref.readline()
gens = []
for st in file_ref:
    gen = st.split('\t')[0]
    gens.append(gen)
file_ref.close()
zag = polim.readline()
file_out.write(zag)
gen0 = 'q'
for st in polim:
    genp = st.split('\t')[0]
    fl = 0
    if genp == gen0:
        fl = 1
    else:
        for gen in gens:
            if genp == gen:
                gen0 = gen
                fl = 1
                break
    if fl == 1:
        file_out.write(st)


polim.close()
file_out.close()
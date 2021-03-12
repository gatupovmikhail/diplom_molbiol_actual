def chek(st):
    # 8 nu в последовательности
    fl = 0
    # if st[0] == 'a': # всего 62 %
    #     fl+=1
    fl+=1
    if st[1] == 'g':
        fl+=1
    if st[2] == 'g':
        fl+=1
    if st[3] == 't':
        fl+=1
    if st[4] == 'a' or st[4] == 'g':
        fl+=1
    if st[5] == 'a' or st[5] == 'g':
        fl+=1
    if st[6] == 'g':
        fl+=1
    # последний t с вер 0,5
    if fl == 7:
        return 1
    fl = 0
    if (st[0] == 't' or st[0] == 'c'):
        fl+=1
    if (st[1] == 't' or st[1] == 'c'):
        fl+=1
    if (st[2] == 't' or st[2] == 'c'):
        fl+=1
    # 3-й это N
    if (st[4] == 't' or st[4] == 'c'):
        fl+=1
    if st[5] == 'a':
        fl+=1
    if st[6] == 'g':
        fl+=1
    if not(st[7] == 't'):
        fl+=1
    if fl == 7:
        return 2
    else:
        return 0
def positions_pol(): # возвращет 4 массива с значениями полиморфизмов и позициями
    #anal_mod = open('anal_from_spl_modif.vcf', 'r')# модификация
    anal_mod = open('alt20_analis_from_splice_0.5.vcf','r')
    zag = anal_mod.readline()
    pos_mut = []  # position for mutation
    buk_mut = []  # sama zamena
    pos_var = []  # position of variation (polim)
    buk_var = []  # variation
    for st in anal_mod:
        if 'alt' in st:
            stm = st.split('\t')
            pos_mut.append(int(stm[2]))
            buk_mut.append('{ref}|{alt}'.format(ref=stm[5], alt=stm[6]))
            # for pol in stm[4].split(','):
            #     pos_var.append(int(pol))
            # for vari in stm[5].split(','):
            #     buk_var.append(vari)
    anal_mod.close()
    ########## измененный блок №№№№№№№№№№№№№№№№№№
    polim = open('pax6_comp_ref.txt','r')
    zag = polim.readline()
    for st in polim:
        stm = st.split('\t')
        pos_var.append(int(stm[1]))
        buk_var.append(stm[2])
    polim.close()

    return (pos_mut,buk_mut,pos_var,buk_var)

def sites_spl(name_gen_file): # записывает текст с выделенными сайтами сплайсинга в pax6_sites.txt
    print('#DON/AKC_REF/ALT_POSL\tPOSITION_OF_SITES\tPOSITION_OF_POLIMORF\tALLELE')
    gen_file = open('pax6.txt','r') # основной ген
    #gen_file = open(name_gen_file,'r')
    #gen_sites = open(name_gen_file.replace('.txt','_spl.txt'),'w') # файл с выделенными сайтами сплайсинга
    for i in range(2):
        zag = gen_file.readline()
        #gen_sites.write(zag)
    gen0 = ''
    for st in gen_file:
        st=st[:-1]
        gen0+=st
    gen_file.close()
    i=0
    gen1 = ''
    pos_sites_don = []
    pos_sites_akc = []
    while i+7 < len(gen0): # поиск сайтов сплайсинга
        if(chek(gen0[i:i+8])==1):
            pos_sites_don.append(i)
        if (chek(gen0[i:i + 8]) == 2):
            pos_sites_akc.append(i)
        i+=1
    pos0 = 31810457
    for k in range(len(pos_sites_akc)):
        pos_sites_akc[k] = pos0 + pos_sites_akc[k]
    for k in range(len(pos_sites_don)):
        pos_sites_don[k] = pos0 + pos_sites_don[k]
    # for site in pos_sites_akc:
    #     print(gen0[site-pos0:site-pos0+8])
    (pos_mut, buk_mut, pos_var, buk_var) = positions_pol()
    var_spl = []
    mut_spl = []
    ind = 0
    for vari in pos_var:
        alt = buk_var[ind][0:-1].split('/')[1]
        ref = buk_var[ind].split('/')[0]
        ind+=1
        for site in pos_sites_akc:
            if site <= vari < (site + 8):
                gen2 = gen0[0:vari - pos0] + gen0[vari - pos0].upper() + gen0[vari - pos0 + 1:len(gen0)]
                gen3 = gen0[0:vari - pos0] + alt.upper() + gen0[vari - pos0 + 1:len(gen0)]
                var_spl.append(vari)
                print('a_ref\t{}-{}\t{}\t{}\t{}'.format(site, (site + 8), vari, gen2[(site - pos0):(site - pos0 + 8)], ref))
                print('a_alt\t{}-{}\t{}\t{}\t{}'.format(site, (site + 8), vari, gen3[(site - pos0):(site - pos0 + 8)], alt))
                print()
        for site in pos_sites_don:
            if site <= vari < (site + 8):
                gen2 = gen0[0:vari-pos0]+gen0[vari-pos0].upper()+gen0[vari-pos0+1:len(gen0)]
                gen3 = gen0[0:(vari - pos0)] + alt.upper() + gen0[(vari - pos0 + 1):len(gen0)]
                var_spl.append(vari)
                print('d_ref\t{}-{}\t{}\t{}\t{}'.format(site,(site+8),vari,gen2[(site-pos0):(site-pos0+8)],ref))
                print('d_alt\t{}-{}\t{}\t{}\t{}'.format(site, (site + 8), vari, gen3[(site - pos0):(site - pos0 + 8)], alt))
                print()

    for mut in pos_mut:
        for site in pos_sites_akc:
            if site <= mut < (site + 8):
                mut_spl.append(mut)
        for site in pos_sites_don:
            if site <= mut < (site + 8):
                mut_spl.append(mut)
    print(mut_spl)
    print(var_spl)

sites_spl('h')
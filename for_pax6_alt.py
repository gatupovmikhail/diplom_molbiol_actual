import gen_exons
def out_red(text): # for mutation
    return "\033[31m {}".format(text)
def out_yellow(text):  # for polimorf
    return "\033[33m {}".format(text)
# def out_blue(text):
#     return "\033[34m {}" .format(text)
def donor(text):
    return "\033[32m\033[43m {}".format(text)
def akceptor(text):
    return "\033[31m\033[43m {}".format(text)
def sbros(text):
    return "\033[0m {}".format(text)
def chekbuk(buk):
    buk = buk.upper()
    if (buk == 'A') or (buk == 'T') or (buk == 'G') or (buk == 'C'):
        return True
    else:
        return False
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

anal = open('mod_analis_from_splice_0.5.vcf','r') # все предсказания
#gen_file = open('pax6.txt','r') # просто ген
gen_file = open('pax6_alt.txt','r')
gen_sites = open('pax6_sites.txt','w') # ген с выделенными сайтами сплайсинга
#file_out = open('pax6_spl.txt','w') #ген с сайтами сплайсинга и заменами
file_out = open('pax6_spl_alt.txt','w')
anal_mod = open('anal_from_spl_modif.vcf','w') # отобранные предсказания
zag = anal.readline()
anal_mod.write('#ID\t'+zag[1:len(zag)])  #### отбор строк без None и добавление порядкового номера
num=0
for st in anal:
    stm = st.split('\t')
    if not(stm[3] == 'NONE'):
        if 'alt' in st:
            num+=1
        anal_mod.write('N{}\t'.format(num)+st)
anal.close()
anal_mod.close()

anal_mod = open('anal_from_spl_modif.vcf','r') # модификация
zag = anal_mod.readline()
pos_mut = [] # position for mutation
buk_mut = [] # sama zamena
pos_var = [] # position of variation (polim)
buk_var = [] # variation
for st in anal_mod:
    if 'alt' in st:
        stm = st.split('\t')
        pos_mut.append(int(stm[3]))
        buk_mut.append('{ref}|{alt}'.format(ref=stm[6],alt=stm[7]))
        for pol in stm[4].split(','):
            pos_var.append(int(pol))
        for vari in stm[5].split(','):
            buk_var.append(vari)
anal_mod.close()

for i in range(2):
    zag = gen_file.readline()
    gen_sites.write(zag)
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

for i in pos_sites_don: # выделение сайтов сплайсинга
    gen0=gen0[0:i] + gen0[i:i+8].upper()  + gen0[i+8:len(gen0)]
for i in pos_sites_akc: # выделение сайтов сплайсинга
    gen0=gen0[0:i] + gen0[i:i+8].upper() + gen0[i+8:len(gen0)]

gen_pr = ''
fl = 0
for k in range(len(gen0)):
    if k%50==0 and not(k==0):
        gen_pr+='\n'
    buk = gen0[k]
    if not(buk.isupper()) and fl == 0:
        gen_pr += buk
        continue
    if buk.isupper() and fl == 0:
        gen_pr+= '|*' + buk
        fl = 1
        continue
    if buk.isupper() and fl == 1:
        gen_pr+= buk
        continue
    if not(buk.isupper()) and fl == 1:
        gen_pr+= '*|'+buk
        fl = 0
gen0 = gen_pr

# i=0
# while i+50 < len(gen0): # разделение на строчки по 50 символов
#     gen_sites.write(gen0[i:i+50]+'\n')
#     i+=50
# gen_sites.write(gen0[i:len(gen0)])
gen_sites.write(gen0)
gen_sites.close()
gen_sites = open('pax6_sites.txt','r')
# gen_exons.exon() # выделение экзонов
# gen_sites = open('pax6_ex.txt','r')

pos = 31810457 - 1 # первая буква гена
for i in range(2): # избавление от заголовочных строк
    zag = gen_sites.readline()
    file_out.write(zag)

gen=''
for st in gen_sites:   # внемене самих меток полиморфизмов
    st = st[0:-1]
    for k in range(len(st)):
        fl=0
        buk = st[k]
        if (chekbuk(buk)):
            pos += 1
        for i in range(len(pos_mut)):
            if pos_mut[i] == pos: # мутации
                mut = buk_mut[i].split('|')[1]
                gen+= '|@' + mut.upper()  + '@|' #+'[{}]'.format(buk_mut[i])
                fl = 1
                break
        for i in range(len(pos_var)): # полиморфизмы
            if pos_var[i] == pos:
                gen += '|&' + buk.upper() + '&|' # + '({})'.format(buk_var[i])
                fl = 1
                break
        if fl == 0: # обычные буквы
            gen += buk

    gen += '\t' + str(pos) + '\n'
print(pos)
file_out.write(gen)


file_out.close()
gen_sites.close()

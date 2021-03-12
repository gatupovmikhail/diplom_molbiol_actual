# files: pax6_nul, pax6_mut, pax6_pol, pax6_mut_pol
global nh
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
def otobr_prediction(): # отбирает нужные предсказания
    anal = open('mod_analis_from_splice_0.5.vcf', 'r')  # все предсказания
    anal_mod = open('anal_from_spl_modif.vcf', 'w')  # отобранные предсказания
    zag = anal.readline()
    #anal_mod.write('#ID\t' + zag[1:len(zag)])  #### отбор строк без None и добавление порядкового номера
    anal_mod.write(zag)
    num = 0
    for st in anal:
        stm = st.split('\t')
        if not (stm[3] == 'NONE'):
            if 'alt' in st:
                num += 1
            anal_mod.write(st)
    anal.close()
    anal_mod.close()
def sites_spl(name_gen_file): # записывает текст с выделенными сайтами сплайсинга в pax6_sites.txt
    #gen_file = open('pax6.txt','r') # основной ген
    gen_file = open(name_gen_file,'r')
    gen_sites = open(name_gen_file.replace('.txt','_spl.txt'),'w') # файл с выделенными сайтами сплайсинга
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
        if k%50 == 0 and not(k==0):
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
    gen_sites.write(gen0)
    gen_sites.close()
def to_html(name_file): # преобраз в html.
    def zamen(st):
        global nh
        st = st.replace('|*', '<span class="splice">')
        st = st.replace('[&', '<span class="var">')
        if '(@' in st:
            nh+=1
            print(nh)
        st = st.replace('(@', '<span class="mut" id="N{}">'.format(nh))
        st = st.replace('|+', '<span class="exon">')
        st = st.replace('*|', '</span>')
        st = st.replace('&]', '</span>')
        st = st.replace('@)', '</span>')
        st = st.replace('+|', '</span>')
        return st
    zag_f = open('zag_html.html', 'r')
    gen = open(name_file, 'r')
    file_out = open(name_file.replace('.txt', '.html'), 'w')
    zag = zag_f.read()
    zag = zag.replace('NAME', name_file)
    file_out.write(zag)
    idm = ''
    for i in range(3):
        idm+='<a href="#N{n}">{n}</a> '.format(n=str(i+1))
    idm = '<p id="smut">'+'mutations: <br>'+idm + '</p>\n'
    file_out.write(idm)
    num = 31810457 # позиция ПЕРВОЙ буквы в строке
    i = 0
    for st in gen:
        if i < 2:
            if not i==1:
                file_out.write('<p> ' + zamen(st)[0:-1] + ' </p>'+'\n')
            i+=1
            continue
        #file_out.write('<p> ' + zamen(st)[0:-1] + '\t'+ str(num) + ' </p>'+'\n')
        file_out.write( zamen(st)[0:-1] + '\t' + str(num) + ' <br>' + '\n')
        num+=50
    file_out.write('\n\t</body>\n')
    file_out.write('</html>')
    gen.close()
    file_out.close()
    zag_f.close()
    print('Записано в '+ name_file.replace('.txt', '.html') )
def positions(): # возвращет 4 массива с значениями полиморфизмов и позициями
    anal_mod = open('anal_from_spl_modif.vcf', 'r')  # модификация
    #anal_mod = open('mod_from_spl_modif.vcf', 'r')
    #anal_mod = open('mod_analis_from_splice_0.5.vcf', 'r')
    zag = anal_mod.readline()
    pos_mut = []  # position for mutation
    buk_mut = []  # sama zamena
    pos_var = []  # position of variation (polim)
    buk_var = []  # variation
    for st in anal_mod:
        if 'alt' in st:
            stm = st[0:-1].split('\t')
            pos_mut.append(int(stm[2]))
            buk_mut.append('{ref}|{alt}'.format(ref=stm[5], alt=stm[6]))
            if stm[3] == 'NONE':
                pos_var.append(-1)
                buk_var.append(-1)
            else:
                for pol in stm[3].split(','):
                    pos_var.append(int(pol))
                for vari in stm[4].split(','):
                    buk_var.append(vari)
    anal_mod.close()
    return (pos_mut,buk_mut,pos_var,buk_var)
def positions_pol(): # возвращет 4 массива с значениями полиморфизмов и позициями
    #anal_mod = open('anal_from_spl_modif.vcf', 'r')  # модификация
    anal_mod = open('mod20_analis_from_splice_0.5.vcf','r')
    zag = anal_mod.readline()
    pos_mut = []  # position for mutation
    buk_mut = []  # sama zamena
    pos_var = []  # position of variation (polim)
    buk_var = []  # variation
    for st in anal_mod:
        if 'alt' in st:
            stm = st[0:-1].split('\t')
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
        stm = st[0:-1].split('\t')
        pos_var.append(int(stm[1]))
        buk_var.append(stm[2])
    polim.close()

    return (pos_mut,buk_mut,pos_var,buk_var)
# ismen and emphasize
def izmen(name_target,file_gen):
    def answer(name,buk,var,cs):
        if 'nul' in name:
            return buk
        if ('mut' in name) and ('pol' in name):
            return var
        if ('mut' in name) and (cs==1):
            return var
        if ('mut' in name) and (cs==2):
            return buk
        if ('pol' in name) and (cs==1):
            return buk
        if ('pol' in name) and (cs==2):
            return var
    gen_target = open(file_gen, 'r')
    file_out = open(name_target,'w')
    (pos_mut, buk_mut, pos_var, buk_var) = positions_pol()

    pos = 31810457 - 1  # первая буква гена
    for i in range(2):  # избавление от заголовочных строк
        zag = gen_target.readline()
        file_out.write(zag)

    gen = ''
    for st in gen_target:  # внемене самих меток полиморфизмов
        st = st[0:-1]
        for k in range(len(st)):
            fl = 0
            buk = st[k]
            if (chekbuk(buk)):
                pos += 1
            for i in range(len(pos_mut)):
                if pos_mut[i] == pos:  # мутации
                    mut = buk_mut[i].split('|')[1]
                    gen += answer(name_target,buk,mut,1)  # +'[{}]'.format(buk_mut[i])
                    fl = 1
                    break
            for i in range(len(pos_var)):  # полиморфизмы
                if not(pos_var[i] == -1):
                    if pos_var[i] == pos:
                        vari = buk_var[i].split('/')[1]
                        gen += answer(name_target, buk, vari, 2)  # + '({})'.format(buk_var[i])
                        fl = 1
                        break
            if fl == 0:  # обычные буквы
                gen += buk

        gen += '\n' # '\t' + str(pos) +
    file_out.write(gen)

    file_out.close()
    gen_target.close()
def emphasize(name_target):
    gen_target = open(name_target, 'r')
    file_out = open(name_target.replace('_spl.txt', '_emph.txt'),'w')
    (pos_mut, buk_mut, pos_var, buk_var) = positions_pol()

    pos = 31810457 - 1  # первая буква гена
    for i in range(2):  # избавление от заголовочных строк
        zag = gen_target.readline()
        file_out.write(zag)

    gen = ''
    for st in gen_target:  # внемене самих меток полиморфизмов
        st = st[0:-1]
        for k in range(len(st)):
            fl = 0
            buk = st[k]
            if (chekbuk(buk)):
                pos += 1
            for i in range(len(pos_mut)):
                if pos_mut[i] == pos and (chekbuk(buk)):  # мутации
                    gen += '(@' + buk.upper() + '@)'  # +'[{}]'.format(buk_mut[i])
                    fl = 1
                    break
            for i in range(len(pos_var)):  # полиморфизмы
                if not(pos_var[i] == -1):
                    if pos_var[i] == pos and (chekbuk(buk)):
                        gen += '[&' + buk.upper() + '&]'  # + '({})'.format(buk_var[i])
                        fl = 1
                        break
            if fl == 0:  # обычные буквы
                gen += buk

        gen += '\n' # '\t' + str(pos) +
    file_out.write(gen)

    file_out.close()
    gen_target.close()
def exon(gen_name):
    gen_gr = open('gens_dominant.txt','r')
    gen = open(gen_name,'r')
    file_ex = open(gen_name.replace('_emph.txt','_ex.txt'), 'w')
    zag = gen_gr.readline()
    start = []
    end = []
    gran = gen_gr.readline().split('\t')
    print(gran[5].split(',')[0:-1])
    print(gran[6].split(',')[0:-1])
    for el in gran[5].split(',')[0:-1]:
        start.append(int(el))
    for el in gran[6].split(',')[0:-1]:
        end.append(int(el))

    for i in range(2):
        zag = gen.readline()
        file_ex.write(zag)
    pos = 31810457 - 1
    gen_t = ''
    for st in gen:
        st = st[0:-1]
        for k in range(len(st)):
            buk = st[k]
            if (chekbuk(buk)):
                pos+=1
            fl = 0
            for i in range(len(start)):
                if (start[i] < pos) and (pos < end[i]):
                    fl = 1
                    break
                if (start[i] == pos):
                    gen_t += '|+'+st[k]
                    break
                if (end[i] == pos):
                    gen_t += st[k] +'+|'
                    break
                if pos < start[i]:
                    break
            if fl == 1:
                gen_t+=st[k]
            else:
                gen_t+=st[k]

        gen_t+='\n'
    file_ex.write(gen_t)

    file_ex.close()
    gen_gr.close()
    gen.close()
otobr_prediction()
names = ['pax6_nul.txt', 'pax6_mut.txt', 'pax6_pol.txt', 'pax6_mut_pol.txt']
#file_out_name = names[3]
for file_out_name in names:
    nh=0
    izmen(file_out_name,'pax6.txt') # один из 4-х записали в file_out_name из pax6.txt
    sites_spl(file_out_name) # pax6_mod.txt
    emphasize(file_out_name.replace('.txt','_spl.txt'))
    #exon(file_out_name.replace('.txt', '_emph.txt'))
    #to_html(file_out_name.replace('.txt', '_ex.txt'))
    to_html(file_out_name.replace('.txt', '_emph.txt'))
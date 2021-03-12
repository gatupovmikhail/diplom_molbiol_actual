def chekbuk(buk):
    buk = buk.upper()
    if (buk == 'A') or (buk == 'T') or (buk == 'G') or (buk == 'C'):
        return True
    else:
        return False
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
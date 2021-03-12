# Вычисляет длину каждой хромосомы
chrom = []
endh = [] # общая длина
ends = [] # кол-во полных строк
endp = [] # длина посл строчки
num_st = 0
absm = [] # Строка в геноме, на которой хромосома кончается 
len0 = 0
abs_st = 0
flag = 0
with open('genom.fa','r') as genom:
    for st in genom:
        abs_st += 1
        if '>' in st:
            if flag == 0:
                ch = st[1:].rstrip()
                chrom.append(ch)
                flag = 1
                continue
            ends.append(num_st)
            endp.append(len0)
            endh.append(num_st*50 + len0)
            absm.append(abs_st)
            ch = st[1:].rstrip()
            chrom.append(ch)
            num_st = 0
        else:
            num_st+=1
            len0 = len(st) - 1
absm.append(abs_st)
ends.append(num_st)
endp.append(len0)
endh.append(num_st*50 + len0)
file_out = open('genom_startend.txt','w')
file_out.write('#CHROM\tEND\tEND_ST\tEND_POS\tABS_ST\n')
print(chrom)
print(endh)
print(ends)
print(endp)
print(absm)
for i in range(len(chrom)):
    file_out.write('{}\t{}\t{}\t{}\t{}\n'.format(chrom[i],endh[i],ends[i],endp[i],absm[i]))
    print('{}\t{}\t{}\t{}\t{}\n'.format(chrom[i], endh[i], ends[i], endp[i], absm[i]))
file_out.close()



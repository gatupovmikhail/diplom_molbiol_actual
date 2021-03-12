import sys
file_tri = open('/media/gatupov/Elements1/splice_ref_tri.vcf','r')
file_out = open('/media/gatupov/Elements1/splice_ref_one.vcf','w')
# file_tri = open('pax6_from_razrab','r')
# file_out = open('pax6_form_razrab_one.vcf','w')
#file_error = open('/media/gatupov/Elements1/errors_big.txt','w')
#file_error = open('/media/gatupov/Elements1/errors_repeat.txt','w')

zag= file_tri.readline()
file_out.write(zag)
p=0
st0 = ''
n_st = 0
gran = 21822000
per = 2
prob = 0
pos0 = -2
ch0 = 'na'
n_out = 0
ref = 'K'
n_p = 0
i_p = 0
for st in file_tri:
    n_st+=1
    if n_st > gran: # the line of downloading
        gran+= 21822000
        print('{}'.format(per),end=' ')
        per+=2

    stm = st[:-1].split('\t')
    ch = stm[0]
    pos = stm[1]
    if not(ch==ch0 and pos == pos0):
        if not(ref == 'N') and not(n_st==1):
            file_out.write(st0 + '\t' + ','.join(alt) + '\t' + center + '\t' + ','.join(predict) + '\n')
            n_out+=1
        if p == 5 or p==6:
            n_p+=1
            # file_error.write(st0 + '\t' + ','.join(alt) + '\t' + center + '\t' + ','.join(predict) + '\n')
        if p > 7:
            i_p=1
        p = 0
        alt = []
        predict = []
        ref = stm[3]
        st0 = '\t'.join(stm[0:4])
        alt.append(stm[4])
        center = '\t'.join(stm[5:7])
        predict.append(stm[7])
    else:
        alt.append(stm[4])
        predict.append(stm[7].replace('SpliceAI=',''))
        p+=1
    ch0 = ch
    pos0 = pos


print(n_out) # сколько переписали.
print(n_st) # сколько было
print(n_p) # сколько с повторяющимися.
print(i_p) # есть ли p>8
#file_error.close()
file_out.close()
file_tri.close()
#3	60104769
#1164 N rows or 291 N

# file_tri = open('/media/gatupov/Elements1/splice_ref_tri.vcf','r')
# zag = file_tri.readline()
# st = '\td\t'
# while not(st.split('\t')[0]=='1' and st.split('\t')[1]=='861580'):
#     st = file_tri.readline()
# print(st,end='')
# for t in range(100):
#     st = file_tri.readline()
#     print(st,end='')
# file_tri.close()
# 363474929 переписали всего #363648083  в alt! разница = 173154
# 1119125784 всего было
# 7672358 дву- и мультиполярные
# 1 есть мультиполярные                                                                                ссссссссссссссссссссссссссссссссссссссссссссссссссчсвс
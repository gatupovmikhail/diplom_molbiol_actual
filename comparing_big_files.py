import sys # 21	48084862 ref_file 70 - alt
reference = open('/media/gatupov/Elements1/for_splice_sorted_full.vcf','r')
alternative = open('for_splice_ai_alt20.vcf','r')
st_r='#'
while '#' in st_r:
    st_r = reference.readline()
st_a = '#'
while '#' in st_a:
    st_a = alternative.readline()
if not(st_a.split('\t')[0]==('chr'+st_r).split('\t')[0]) or not(st_a.split('\t')[1]==('chr'+st_r).split('\t')[1]):
    print('NO!')
    print(st_a)
    print(st_r)
    reference.close()
    alternative.close()
    sys.exit()
nst=1
gran = 7269498
per = 2
for st_a in alternative:
    nst+=1
    if nst > gran: # the line of downloading
        gran+= 7270000
        print('{}'.format(per),end=' ')
        per+=2
    st_r = reference.readline()
    if st_r=='':
        print(st_r, end='')
        print(st_a, end='')
        print(nst)
        reference.close()
        alternative.close()
        sys.exit()
    if not(st_a.split('\t')[0] == ('chr'+st_r).split('\t')[0]) or not(st_a.split('\t')[1] == ('chr'+st_r).split('\t')[1]):
        print(st_r0, end='')
        print(st_a0, end='')
        print(st_r,end='')
        print(st_a,end='')
        st_r = reference.readline()
        st_a = alternative.readline()
        print(st_r, end='')
        print(st_a, end='')
        st_r = reference.readline()
        st_a = alternative.readline()
        print(st_r, end='')
        print(st_a, end='')
        print(nst)
        reference.close()
        alternative.close()
        sys.exit()
    st_r0 = st_r
    st_a0 = st_a
# 738532


reference.close()
# n_a = 1
# for st_a in alternative:
#     n_a+=1
# print(n_a)
alternative.close() #FHIT    3       60104720-60104891  546695
# 3	60104769	.	E
# chr3	60104770	.	G	A,T,C	100	PASS	MQ=50;SNP=chr3|rs201219564|60104770|T/G|0.662637	AF:GT	0.5:0/1
# 3	60104770	.	T	A,C,G	.	.	SpliceAI=A|FHIT|0.00|0.00|0.00|0.00|-3|-26|13|-26,C|FHIT|0.00|0.00|0.00|0.00|13|-26|-1|-26,G|FHIT|0.00|0.00|0.00|0.00|-3|-26|-10|-26
# chr3	60104771	.	C	A,T,G	100	PASS	MQ=50;SNP=chr3|rs201219564|60104770|T/G|0.662637	AF:GT	0.5:0/1
# 3	60104771	.	C	A,G,T	.	.	SpliceAI=A|FHIT|0.00|0.00|0.00|0.00|-3|-27|12|-27,G|FHIT|0.00|0.00|0.00|0.00|-3|-27|12|-27,T|FHIT|0.00|0.00|0.00|0.00|-27|-4|12|-27
# chr3	60104772	.	A	T,G,C	100	PASS	MQ=50;SNP=chr3|rs201219564|60104770|T/G|0.662637	AF:GT	0.5:0/1
# 70596573
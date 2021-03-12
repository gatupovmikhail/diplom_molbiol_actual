import sys
import time
t1 = time.time()
#file = open('/media/gatupov/Elements1/spliceai_scores.masked.snv.hg19.vcf','r')
file = open('/media/gatupov/Elements1/spliceai_scores.masked.snv.hg19.vcf','r')
st = '#'
while('#' in st):
    st= file.readline()
st00 = ''
st0 = '1'
stm = st.split('\t')
num = '51117630'
while not((stm[0]=='22') and (stm[1]==num)) and not(stm[0]=='X'):
    st = file.readline()
    stm = st.split('\t')
    if len(stm)<2:
        print(st00, end='')
        print(st0, end='')
        print(repr(st))
        st = file.readline()
        print(st, end='')
        st = file.readline()
        print(st, end='')
        sys.exit()
    if not(stm[1]==num):
        st00=st0
        st0 = st
print(st00,end='')
print(st0,end='')
print(st,end='')
st = file.readline()
print(st,end='')
st = file.readline()
print(st,end='')
st = file.readline()
print(st,end='')


file.close() #chr22	51117630
t2=time.time()
print(str(t2-t1))

# 22	51117629	.	G	C	.	.	SpliceAI=C|SHANK3|0.00|0.00|0.07|0.01|-26|1|2|-15
# 22	51117629	.	G	T	.	.	SpliceAI=T|SHANK3|0.00|0.00|0.00|0.00|-43|-6|-15|2
# 22	51117630	.	A	C	.	.	SpliceAI=C|SHANK3|0.00|0.00|0.00|0.00|-6|-27|-16|1
# 22	51117630	.	A	G	.	.	SpliceAI=G|SHANK3|0.00|0.00|0.00|0.00|-39|-16|-16|1
# 22	51117630	.	A	T	.	.	SpliceAI=T|SHANK3|0.00|0.00|0.00|0.00|-6|-27|-16|1
# 22	51117631	.	G	A	.	.	SpliceAI=A|SHANK3|0.00|0.00|0.00|0.00|2|0|-17|0
# 2587.9105508327484

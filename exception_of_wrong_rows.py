import sys
#big_file = open('/media/gatupov/Elements1/for_splice_sorted_full.vcf','r')
# big_file=open('for_splice_ai_alt20.vcf','r')
# file_out = open('areas_of_big.vcf','w')
# file_log = open('log_of_big.vcf','w')
big_file=open('pax6_ref_alg.vcf','r')
file_out = open('areas_of_pax6.vcf','w')
file_log = open('log_of_pax6.vcf','w')
for i in range(44): #43
    zag = big_file.readline()
n_st = 0
#ch0='chr1'
ch0 = 'chr11' #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
pos0 = -1
st0 = 'NAN'
fl = 0
for st in big_file:
    n_st+=1
    stm = st.split('\t')
    ch = stm[0]
    pos = int(stm[1])

    if ch0 == ch and pos0 == pos and fl < 150: # search of equals rows
        fl +=1
        file_log.write(str(n_st)+' '+st0)
        file_log.write(st)

    if (pos - pos0) > 1 or ( not(ch==ch0) and ((pos-pos0)<=1) ): # forms of intervals
        if not(st0 == 'NAN'):
            file_out.write('\t{}\n'.format(pos0))
        file_out.write('{}\t{}'.format(ch,pos))
    if pos < pos0 and ch0==ch:
        print('oyzhas')
        print(n_st)
        print(st0)
        print(st)
        sys.exit()

    ch0 = ch
    pos0 = pos
    st0 = st

file_out.write('\t{}\n'.format(pos))
print(n_st)
file_log.close()
big_file.close()
file_out.close()
file_gen=open('gens_spliceAI_sorted_concantenated.txt','r')
#mfile=open('splice_ai.txt','r')
file_out = open('gens_dominant.txt','w') # Записывает один ген с заданным названием в этот файл с шапкой.
#file_zag = open('part_splice_ai.vcf','r')

# zag = ''
# for i in range(42):
#    zag += file_zag.readline()
# file_zag.close()
# file_out.write(zag)

zag='#NAME\tCHROM\tSTRAND\tTX_START\tTX_END\tEXON_START\tEXON_END\n'
file_out.write(zag)
gen_r='PAX6'
for st in file_gen:
    stm=st.split('\t')
    gen=stm[0]
    if gen == gen_r:
        file_out.write(st)
        # chrom=stm[1].lower()
        # start = int(stm[3])
        # end = int(stm[4])
        break
file_gen.close()
file_out.close()

# ch0='133'
# num_st = 0
# ch_s = '0'
# zag_1 = mfile.readline()
#
# while not(chrom == ch_s):
#     num_st+=1
#     if (num_st % 10**8) == 0:
#         print((num_st//10**8),end=' ')
#     st = mfile.readline()
#     stm = st.split('\t')
#     ch_s = stm[0].replace('chr','')
#     ch_s = ch_s.lower()
#     pos_s=int(stm[1])
#     if chrom == ch_s and (start <= pos_s <= end):
#         file_out.write(st)
#     if not(ch0 == ch_s):
#         print('chr' +str(ch_s),end=' ')
#         ch0=ch_s
#
# print(num_st)
# while (chrom == ch_s):
#     num_st+=1
#     st=mfile.readline()
#     stm = st.split('\t')
#     ch_s=stm[0].replace('chr','')
#     ch_s = ch_s.lower()
#     pos_s = int(stm[1])
#     if start <= pos_s <= end:
#         file_out.write(st)
#     if not(ch0==ch_s):
#         print(ch_s,end=' ')
#         ch0=ch_s
# print(num_st)
#
#
#
#
# print(zag_1)
#
#
# mfile.close()


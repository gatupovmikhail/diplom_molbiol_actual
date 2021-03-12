# #polim = open('gnomad_polim_all.vcf','r')
# polim = open('gnomad_polim_all_filtr.vcf','r')
# #file_out = open('/media/gatupov/Elements1/Миши_Диплом/polimorfs_gnomad_all.vcf','w')
# file_out = open('polimorfs_gnomad_all_filtr.vcf','w')
# with open('manual_new.vcf','r') as file_man:
#     for st in file_man:
#         # if not('CHROM' in st) and not('PASS' in st):
#         if not('100340787' in st):
#             file_out.write(st)
#         else:
#             break
# file_man.close()
# n = 0
# fl = 0
# for st in polim:
#     if fl == 0:
#         fl = 1
#         continue
#     st = st[:-1]
#     stm = st.split('\t')
#     ch = stm[0].replace('$','')
#     pos = stm[1]
#     ref = stm[2]
#     alt = stm[3]
#     af = stm[4]
#     id = stm[5]
#     gen = stm[6]
#     st_out = '{ch}\t{pos}\t{id}\t{ref}\t{alt}\t100\tPASS\tMQ=50;AF={af};GEN={gen}\tAF:GT\t0.5:0/1\n'.format(ch=ch, pos=pos, id=id, ref=ref, \
#                                                                                                   alt=alt, af=af,gen=gen)
#     file_out.write(st_out)
#
# polim.close()
# file_out.close()
polim = open('gnomad_polim_all_filtr.vcf','r')
n = -1
for st in polim:
    n+=1
print(n)
polim.close()
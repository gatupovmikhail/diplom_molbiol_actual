#big_file = open('/media/gatupov/Elements1/spliceai_scores.masked.snv.hg19.vcf','r')
# areas = open('polim_in_gens_form_concan.txt','r')
areas = open('/media/gatupov/Elements1/splice_ref_one.vcf','r')
#
# mas_ar = []
# ch0 = '1'
# st='#'
zag = areas.readline()
# f = 1
# mas_ar.append('1')
# file_f = open('/media/gatupov/Elements1/swapping/ref_chr{}.txt'.format(f),'w')
# for st in areas:
#     ch = st.split('\t')[0] # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     if not ch0==ch:
#         print(ch,end=' ')
#         file_f.close()
#         f = ch
#         file_f = open('/media/gatupov/Elements1/swapping/ref_chr{}.txt'.format(f), 'w')
#         file_f.write(zag)
#         mas_ar.append(ch)
#         ch0=ch
#     file_f.write(st)
# file_f.close()
#
# print(mas_ar)

sp = ['1', '2', '3', '4', '5', '6', '7', 'X', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '20', 'Y', '19', '22', '21']
file_out = open('/media/gatupov/Elements1/for_splice_sorted.vcf','w')
file_out.write(zag)
for f in sp:
    file_f = open('/media/gatupov/Elements1/swapping/ref_chr{}.txt'.format(f), 'r')
    for st in file_f:
        file_out.write(st)
    file_f.close()
file_out.close()



areas.close()
#['1', '2', '3', '4', '5', '6', '7', 'X', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '20', 'Y', '19', '22', '21']
#['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 'X', 'Y']
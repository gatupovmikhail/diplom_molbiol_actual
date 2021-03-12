### разделяет большой файл на файлы по 100000 строк
import time
t1 = time.time()
#big_file = open('for_splice_ai_alt20.vcf','r')
#big_file = open('/media/gatupov/Elements1/for_splice_sorted_full.vcf','r')
#big_file = open('for_splice_ai_alt30.vcf','r')
big_file = open('polimorfs_gnomad_all_filtr.vcf','r')
st = '#'

while '#' in st:
    st = big_file.readline()

#zag_f = open('zagn.txt','r')
zag_f = open('manual_new.vcf','r')
zag = zag_f.read()
zag_f.close()
# info_file = open('/media/gatupov/Elements1/splice/info_files.txt','w')
# file_out = open('/media/gatupov/Elements1/splice/for_splice_ref_1.vcf','w')
# info_file = open('splice_alt/info_files.txt','w')
# file_out = open('splice_alt/for_splice_alt_1.vcf','w')
info_file = open('splice_polimorfs/info_files.txt','w')
file_out = open('splice_polimorfs/for_splice_polim_1.vcf','w')
file_out.write(zag)
file_out.write(st)
abs_p = 1
otn_p = 1
f = 1
info_file.write('for_splice_polim_{}.vcf\t{}'.format(f,abs_p))
pom = []
pom.append(st.split('\t')[0])
pom.append(st.split('\t')[1])
for st in big_file:
    abs_p += 1
    otn_p += 1
    if (otn_p == 100001 and not(f==1)) or (otn_p==100000 and f==1):
        file_out.close()
        otn_p = 1
        f+=1
        # file_out = open('/media/gatupov/Elements1/splice/for_splice_ref_{}.vcf'.format(f),'w')
        file_out = open('splice_polimorfs/for_splice_polim_{}.vcf'.format(f), 'w')
        file_out.write(zag)
        pom=[]
        pom.append(st.split('\t')[0])
        pom.append(st.split('\t')[1])
        info_file.write('for_splice_polim_{}.vcf\t{}'.format(f,abs_p))
    file_out.write(st)
    if (otn_p == 100000 and not(f==1)) or (otn_p == 99999 and f==1):
        pom.append(st.split('\t')[0])
        pom.append(st.split('\t')[1])
        info_file.write('-{}\t{}|{}\t{}|{}\n'.format(abs_p,pom[0],pom[1],pom[2],pom[3]))

file_out.close()
pom.append(st.split('\t')[0])
pom.append(st.split('\t')[1])
info_file.write('-{}\t{}|{}\t{}|{}\n'.format(abs_p,pom[0],pom[1],pom[2],pom[3]))
info_file.write('\n')
t2=time.time()
info_file.write(str(t2-t1))
info_file.close()





# while p < pos:
#     st = big_file.readline()
#     p+=1
# while not('chr10\t100370630' in st)or(st==''):
#     st = big_file.readline()
#     p+=1
# print(st)
print(abs_p)
big_file.close()
print(t2-t1)



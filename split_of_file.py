mfile = open('splice_ai.txt','r')
file_out = open('part_splice_ai.vcf','w')
for j in range(4000):
    st=mfile.readline()
    file_out.write(st)
mfile.close()
file_out.close()

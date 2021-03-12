num=0
zag=''
with open('part_splice_ai_hg19.vcf','r') as mfile:
    for i in range(42):
        zag += mfile.readline()
    for i in range(20):
        file_out=open('p{}_splice_ai_hg19.vcf'.format(i),'w')
        file_out.write(zag)
        while num <= 900:
            file_out.write(mfile.readline())
            num+=1
        num = 0
        file_out.close()

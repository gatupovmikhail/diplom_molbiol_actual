gnom = open('gnomad_polim.vcf','r')
file_out = open('gnomad_polimchr.vcf','w')
zag = gnom.readline()
file_out.write(zag)
for st in gnom:
    st1 = 'chr'+st
    file_out.write(st1)
gnom.close()
file_out.close()

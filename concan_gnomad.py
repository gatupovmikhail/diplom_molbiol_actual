# соединение в порядке следования в геноме
Nm = [1,2,3,4,5,6,7,'X',8,9,10,11,12,13,14,15,16,17,18,20,'Y',19,22,21]
#Nm = [1,2,3,4,5,6,7,'X',8,9,10,11,12,13,14,15,16,17,18,20,19,22,21]
#file_out = open('gnomad_polim.vcf','w')      # файл с af>0.01
# file_out = open('gnomad_polim_all.vcf','w') # файл со всеми af
# for N in Nm:
#     polim = open('gnomad_polim_chr{}.vcf'.format(N))
#     for st in polim:
#         file_out.write(st)
#     polim.close()
# file_out.close()
file_out = open('gnomad_polim_all.vcf','r')
num = -1
for st in file_out:
    num+=1
file_out.close()
print('POLIMS:')
print(num)

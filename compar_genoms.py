# ищет совпадающие и отличающиеся полиморфизмы из двух баз dbSNP и gnomAD
from sys import exit
gnom = open('genom_comp_gnom.txt','r')
dbsnp = open('genom_comp_db.txt','r')
db_otl = open('db_otl.txt','w')
gnom_otl = open('gnom_otl.txt','w')
num = -1
pos = 0
ch = 'a'
for stg in gnom:
    std = dbsnp.readline()
    if '>' in stg:
        ch = stg[1:-1]
        print(ch,end=' ')
        num = -1
    else:
        num+=1
    for k in range(len(stg)):
        if not(stg[k].upper() == std[k].upper()):
            if (stg[k] == 'M') and (std[k] == 'D'):
                continue
            if not(stg[k] == 'M') and (std[k] == 'D'):
                db_otl.write('{}\t{}\t{}\t{}\n'.format(ch,str(num*50+k+1),stg[k],std[k]))
            if (stg[k] == 'M') and not(std[k] == 'D'):
                gnom_otl.write('{}\t{}\t{}\t{}\n'.format(ch,str(num*50+k+1),stg[k],std[k]))
            if not(stg[k] == 'M') and not(std[k] == 'D'):
                print('ERROR')
                print(num)
                print(ch)
                print(k)
                exit()


gnom_otl.close()
db_otl.close()
gnom.close()
dbsnp.close()
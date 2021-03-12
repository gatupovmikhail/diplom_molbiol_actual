#name_file = 'itog_annotate.txt' Находит неповторяющиеся названия всех генов в файле
file_ad=open('file_ad_spisok.txt','w')
file_ar=open('file_ar_spisok.txt','w')
file_adar=open('file_adar_spisok.txt','w') # 6

def ref_gen(name_file,file_out,title):
    genes=[]
    with open(name_file) as mfile:
        zag=mfile.readline()
        for str in mfile:
            flag=0
            str_m=str.split('\t')
            for g in genes:
                if(str_m[6]==g):
                    flag=1
            if flag==0:
                genes.append(str_m[6])
    file_out.write(title + '\n')
    for g in genes:
        file_out.write(g+'\n')
    file_out.close()

ref_gen('file_ad.txt',file_ad,'AD genes')
ref_gen('file_ar.txt',file_ar,'AR genes')
ref_gen('file_adar.txt',file_adar,'AD and AR genes')



import subprocess
def clean(name_file,file_out):
    ofile = open(file_out,'w')
    with open(name_file) as mfile:
        zag=mfile.readline()
        ofile.write(zag)
        for str in mfile:
            str_m=str.split('\t')
            flag=0
            for j in range(10,44):
                if(str_m[j]=='.'):
                    continue
                else:
                    flag=1
            if(flag==1):
                ofile.write(str)
    print('Результаты записаны в '+ file_out)
    ofile.close()

clean('file_ad.txt','file_ad_clean.txt')
clean('file_ar.txt','file_ar_clean.txt')
clean('file_adar.txt','file_adar_clean.txt')


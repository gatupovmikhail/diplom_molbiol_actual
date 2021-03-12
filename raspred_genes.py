# Раскидывает итоговый файл по трем файлам AD AR AD_AR
name_file = 'itog_annotate.txt'
file_ad=open('file_ad.txt','w')
file_ar=open('file_ar.txt','w')
file_adar=open('file_adar.txt','w') # 6
with open(name_file) as mfile:
    zag=mfile.readline()
    file_ad.write(zag)
    file_ar.write(zag)
    file_adar.write(zag)
    for str in mfile:
        str_m=str.split('\t')

        if (str_m[54].split()[1]=='AD'):
            file_ad.write(str)

        if (str_m[54].split()[1]=='AR'):
            file_ar.write(str)

        if (str_m[54].split()[1]=='AD_AR'):
            file_adar.write(str)
file_ad.close()
file_ar.close()
file_adar.close()
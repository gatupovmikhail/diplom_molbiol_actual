# Устранит подозрительные SNP и выделит нужные столбцы.
from sys import exit

def zagprint(name_file):
    with open(name_file) as mfile:
        st1 = mfile.readline().split('\t')
        st2 = mfile.readline().split('\t')
        if len(st1) == len(st2):
            print('Number of columns is correct \n')
        else:
            print('DANGER not all data with columns \n')
            print('1 ' + str(len(st1)))
            print('2 ' + str(len(st2)))

    with open(name_file) as mfile:
        zag = mfile.readline()
        first_str=mfile.readline()
        first_str=first_str.split('\t')
        zag=zag.split('\t')
        for j in range(len(zag)):
            print('{} [{}] | {}'.format(zag[j],j,first_str[j]))
# напечатает заголовки столбцов
def few_columns(name_file,columns,numberC):

    with open(name_file) as mfile:
        st1 = mfile.readline().split('\t')
        st2 = mfile.readline().split('\t')
        if len(st1) == len(st2):
            print('Number of columns is correct \n')
        else:
            print('DANGER not all data with columns \n')

    for num in columns:
        with open(name_file) as mfile:
            zag = mfile.readline().split('\t')
            j = 0
            print(str(zag[num] + ' | '),end='')
            while j < numberC:
                j+=1
                st=mfile.readline()
                stm=st.split('\t')
                print(stm[num]+'\t',end='')
        print()
# напечатает numberC строчек для колонок с номерами из списка columns из name_file
def checkfile(name_file):
    try:
        m=open(name_file,'r')
        m.close()
    except(FileExistsError):
        print("File not found")
        exit()


# проверяет существование файла
def writting_file(name_file,name_file_out):
    print()
    print('Из файла '+name_file)
    print('Результаты записаны в файл '+name_file_out)
# Сообщение назавния выходного файла

if __name__=="__main__":

    name_file='genome_variation_single_event.txt'
    name_file_out='genome_var_snp.txt'
    file_out=open(name_file_out,'w')
    checkfile(name_file)
    zagprint(name_file)
    few_columns(name_file,[7,9,22,23],40) # 7 9 % 22
    zapret=[7,9,22]

    with open(name_file) as mfile:

        zag=mfile.readline().split('\t')
        new_st=''
        for j in range(len(zag)):
            if not j in zapret and not (j == len(zag) - 1):
                new_st += zag[j] + '\t'
            if j == 22:
                ref = 'Ref'
                alt = 'Alt'
                new_st += ref + '\t' + alt + '\t'
            if (j == len(zag) - 1):
                new_st += zag[j]
        file_out.write(new_st)

        for st in mfile:
            stm=st.split('\t')
            if (sum([ float(k) for k in stm[23].split(',')[:-1]]) >= 200):
                new_st=''
                for j in range(len(zag)):
                    if not j in zapret and not(j==len(zag)-1): # не печатает столбцы с номерами из списка
                        new_st+=stm[j]+'\t'

                    if j==22: # делает из столбца 2
                        sp=stm[j].split(',')
                        ref=sp[0]
                        alt=''
                        for i in range(1,len(sp)):
                            if i == 1 and len(sp)<4:
                                alt+=sp[i]
                            else:
                                if i < len(sp)-1:
                                    alt+=sp[i] +'/'
                                if i == len(sp)-1:
                                    alt+=sp[i]
                        new_st+=ref+'\t'+alt+'\t'

                    if(j == len(zag) - 1): # избегает двойного перевода строки в конце
                        new_st+=stm[j]
                file_out.write(new_st)




    zagprint(name_file_out)
    few_columns(name_file_out, [22], 40)  # 7 9 % 22

    file_out.close()
    checkfile(name_file_out)
    writting_file(name_file, name_file_out)


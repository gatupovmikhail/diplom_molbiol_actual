from sys import exit
def my_counter(name_file,column): # считает сколько какие значения встретились в файле
    count={}
    count['all']
    with open(name_file) as mfile:
        zag=mfile.readline()
        for st in mfile:
            stm=st.split('\t')
            count['all']+=1
            if not(stm[column] in list(count.keys())):
                count[stm[column]]=0
            else:
                count[stm[column]]+=1
    print('Results \n')
    for el in list(count.keys()):
        print('{}: {} | {} %'.format(el,count[el],str(count[el]/count['all']*100)))

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
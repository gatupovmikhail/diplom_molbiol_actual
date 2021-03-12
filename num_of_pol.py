from sys import exit
# Часть 1 - перевод формата pos из формата позиции от начала хромосомы в формат номер строки + позиция в строке.
# Часть 2 - перевод всех полиморфизмов, следующих друг за другом в одной строке на одну строку документа.

from my_library import writting_file, checkfile, zagprint, few_columns

# name_file='genom_var_single_sorted.txt'
# name_file_out='num_pol_new.txt'
# file_out=open(name_file_out,'w')
# zagprint(name_file)
# with open(name_file) as mfile:
#     zag=mfile.readline()
#     for st in mfile:
#         stm=st.split('\t')
#         num_st=int(stm[3])//50
#         if int(stm[3])%50==0:
#             ost_st =50
#             num_st-=1
#         else:
#             ost_st=int(stm[3])%50
#         ref = stm[20]
#         alt=stm[21]
#         ch=stm[1]
#         strand=stm[6]
#         locType=stm[14]
#         loc='o'
#         if locType=='exact':
#             loc='e'
#         allel_freq=stm[23].split(',')
#         al_f=''
#         if float(allel_freq[0]) > float(allel_freq[1]):
#             al_f='ref'
#         else:
#             al_f='alt'
#         file_out.write('{}\t{}\t{},{}/{},{},{},{}\n'.format(ch,num_st,ost_st,ref,alt,strand,loc,al_f))
#
#
#
# file_out.close()
#                           previous version

##                          version 2.0           ##


name_file='num_pol_new.txt'
name_file_out='num_pol_new_2.txt'
file_out=open(name_file_out,'w')
#zagprint(name_file)
strok=''
with open(name_file) as mfile:
    flag=0
    num=1
    st='a'
    st0 = mfile.readline()
    st0=st0[:-1]
    stm = st0.split('\t')
    ch0 = stm[0]
    num_st0 = int(stm[1])
    third0 = stm[2]
    while not st=='' and num < 11239786:
        st=mfile.readline()
        num+=1
        st=st[:-1]
        stm=st.split('\t')
        ch=stm[0]
        try:
            num_st=int(stm[1])
        except IndexError:
            print('numer {}'.format(num))
        third = stm[2]
        # third=stm[2].split(',')
        # ost_st=int(third[0])
        # ref=third[1].split('/')[0]
        # alt=third[1].split('/')[1]
        if num_st0==num_st and ch0==ch and flag==1:
            strok+='|{}'.format(third0)
        if num_st0==num_st and ch0==ch and flag==0:
            strok=st0
            flag=1
        if not(num_st0 == num_st and ch0 == ch) and flag==0:
            file_out.write(st0+'\n')
        if not(num_st0 == num_st and ch0 == ch) and flag==1:
            strok += '|{}'.format(third0)
            file_out.write(strok+'\n')
            flag=0
        st0 = st
        ch0 = ch
        num_st0 = num_st
        third0 = third
file_out.write(st0+'\n')


file_out.close()

# name_file='polimorf_full_errors.txt' #14 23
# zagprint(name_file)
# kol=0
# er=0
# with open(name_file) as mfile:
#     zag=mfile.readline()
#     for st in mfile:
#         kol+=1
#         if not(st.split('\t')[6]=='-'):
#             print(st)
#             er+=1
# print(kol)
# print(er)

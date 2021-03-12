#                          version 2.0           ##
from sys import exit

name_file='gnomad_polim_form.vcf'
name_file_out='gnomad_polim_itog.vcf'
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
    for st in mfile:
        num+=1
        st=st[:-1]
        stm=st.split('\t')
        ch=stm[0]
        try:
            num_st=int(stm[1])
        except IndexError:
            print('numer {}'.format(num))
            exit()
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
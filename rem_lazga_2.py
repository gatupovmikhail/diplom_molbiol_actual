from sys import exit

from my_library import writting_file, checkfile, zagprint, few_columns

#__name__='ha'

if __name__=="__main__":

    name_file='genome_var_single_ispr.txt'
    name_file_out='genome_var_single_ispr.txt'
    #few_columns(name_file,[9,20,21],3000)




    #file_out=open(name_file_out,'w')
    checkfile(name_file)

    zagprint(name_file)
    wrong=[]
    with open(name_file) as mfile:
        zag=mfile.readline()
        #file_out.write(zag)
        cend=0
        ch='chr1'
        s=1

        for st in mfile:
            stm=st.split('\t')
            s+=1
            fl=0
            if (float(stm[3])<cend) and (stm[1]==ch):
                wrong.append(s)
            if not(stm[1]==ch):
                ch=stm[1]

            cend=float(stm[3])

            if not(stm[9]=='single'):
                wrong.append(s)
                fl+=1

            if (stm[9]=='single') and not(int(stm[2])==int(stm[3])-1):
                wrong.append(s)
                fl+=1



    print(len(wrong))
    print(s)

    # with open(name_file) as mfile:
    #     zag = mfile.readline()
    #     file_out.write(zag)
    #     s=1
    #     for st in mfile:
    #         s+=1
    #         if not(s in wrong):
    #             file_out.write(st)
    # print(s)
    #
    #
    # writting_file(name_file, name_file_out)
    # # Error
    # # in456452, Error
    # # in5330996,
    # file_out.close()
    

from sys import exit

from my_library import writting_file, checkfile, zagprint, few_columns

# __name__='ha'

if __name__ == "__main__":

    name_file = 'genome_var_snp_2.txt'
    name_file_out = 'genome_var_single.txt'
    # few_columns(name_file,[9,20,21],3000)

    file_out=open(name_file_out,'w')
    checkfile(name_file)

    zagprint(name_file)

    with open(name_file) as mfile:
        zag = mfile.readline()
        file_out.write(zag)
        all=0
        sin=0
        for st in mfile:
            all+=1
            stm = st.split('\t')
            if (len(stm[20])==1) and (len(stm[21])==1) and not(stm[20]=='-') and not (stm[21]=='-'):
                file_out.write(st)
                sin+=1
    print('Single:{}'.format(str(sin/all)))


    writting_file(name_file, name_file_out)

    # file_out.close()


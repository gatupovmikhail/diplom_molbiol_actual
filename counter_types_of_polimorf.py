from my_library import writting_file, checkfile, zagprint, few_columns

# __name__='ha'

if __name__ == "__main__":
    name_file = 'genome_var_snp_2.txt'

    few_columns(name_file, [9, 20, 21], 3000)
    count={}
    count['single']=0
    count['insertion']=0
    count['deletion']=0
    count['all']=0


    checkfile(name_file)

    #zagprint(name_file)

    with open(name_file) as mfile:
        zag=mfile.readline()
        for st in mfile:
            count['all']+=1
            stm=st.split('\t')
            for elem in list(count.keys()):
                if elem==stm[9]:
                    count[elem]+=1
    print('results: \n single: {} | {} \n insertion: {} | {} \n deletion: {} | {} \n'.format(count['single'],count['single']/count['all'], \
                                                                                             count['insertion'],count['insertion']/count['all'], \
                                                                                             count['deletion'],count['deletion']/count['all'],))





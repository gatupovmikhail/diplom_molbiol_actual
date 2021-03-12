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

#['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chrX', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr20', 'chrY', 'chr19', 'chr22', 'chr21']


if __name__=="__main__":
    # name_file = 'genome_variation_single_event.txt'
    # name_file_out = 'genome_var_snp.txt'
    # few_columns(name_file,[23],5)
    #name_file = 'genome_var_single.txt'
    name_file= 'genom_var_single_sorted.txt'
    polim=[]
    with open(name_file) as mfile:
        zag=mfile.readline()
        num=1
        ref='ha'
        minh=1000000000
        maxh=-2
        for st in mfile:
            num+=1
            stm=st.split('\t')
            # if maxh<float(stm[3]):
            #     maxh=float(stm[3])
            # if minh>float(stm[3]):
            #     minh=float(stm[3])

            if not(stm[1]==ref):
                #print('{} st {} \n min {} max {}'.format(stm[1],num,minh,maxh))
                #print('{}'.format(stm[1]))
                polim.append(stm[1])
                ref=stm[1]
                minh = 1000000000
                maxh = -2
            # if(float(stm[3])<hoho):
            #     print('num_hoho {} | {} {}'.format(num,hoho,stm[3]))
            #     hoho=float(stm[3])

    name_file = 'genom.fa'
    gen=[]

    with open(name_file) as mfile:
        num=1
        for st in mfile:
            num+=1
            if ('>' in st) or ('chr' in st):
                gen.append(st[1:-1])
    print(gen)
    print(polim)   # 10271902 in sorted file
    # l=0
    # for elg in gen:
    #     for elp in polim:
    #         if elg==elp:
    #             l+=1
    #             print(elg)
    # print(l)
    # print(len(polim))

    #file_out=open('sravnim.txt','w')  61 013 542



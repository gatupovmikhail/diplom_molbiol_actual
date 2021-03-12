from my_library import writting_file, checkfile, zagprint, few_columns

if __name__=='__main__':
    name_file= 'genome_var_single.txt'
    name_file_out='genom_var_single_sorted.txt'
    file_out=open(name_file_out,'w')
    with open(name_file) as mfile:
        zag=mfile.readline()
        file_out.write(zag)
        for st in mfile:
            stm = st.split('\t')
            if (stm[1]=='chr8'):
                break
            file_out.write(st)

    with open(name_file) as mfile: # chrX
        zag=mfile.readline()
        for st in mfile:
            stm = st.split('\t')
            if (stm[1]=='chrX'):
                file_out.write(st)
            if (stm[1]=='chrY'):
                break

    with open(name_file) as mfile: #
        zag=mfile.readline()
        fl=0
        for st in mfile:
            stm = st.split('\t')
            if (stm[1]=='chr8') or (stm[1]=='chr9'):
                file_out.write(st)
                fl=1
            if (stm[1]=='chrX') or (stm[1]=='chrY'):
                continue
            if fl==1 and not(stm[1]=='chr19'):
                file_out.write(st)
            if (stm[1]=='chr19'):
                break
    with open(name_file) as mfile: # chrX
        zag=mfile.readline()
        for st in mfile:
            fl=0
            stm = st.split('\t')
            if not(stm[1] == 'chr20' ) and fl==0:
                continue
            if (stm[1]=='chr20'):
                file_out.write(st)
                fl=1
            if (stm[1]=='chr21'):
                break

    with open(name_file) as mfile: # chrY
        zag=mfile.readline()
        for st in mfile:
            fl=0
            stm = st.split('\t')
            if not(stm[1] == 'chrY') and fl==0:
                continue
            if (stm[1]=='chrY'):
                file_out.write(st)
                fl=1
            if (stm[1]=='chr10'):
                break

    with open(name_file) as mfile: # chr19
        zag=mfile.readline()
        for st in mfile:
            fl=0
            stm = st.split('\t')
            if not(stm[1] == 'chr19') and fl==0:
                continue
            if (stm[1]=='chr19'):
                file_out.write(st)
                fl=1
            if (stm[1]=='chr20'):
                break

    with open(name_file) as mfile: # chrY
        zag=mfile.readline()
        for st in mfile:
            fl=0
            stm = st.split('\t')
            if not(stm[1] == 'chr22') and fl==0:
                continue
            if (stm[1]=='chr22'):
                file_out.write(st)
                fl=1
            if (stm[1]=='chr6_apd_hap1'):
                break
    with open(name_file) as mfile: # chrY
        zag=mfile.readline()
        for st in mfile:
            fl=0
            stm = st.split('\t')
            if not(stm[1] == 'chr21') and fl==0:
                continue
            if (stm[1]=='chr21'):
                file_out.write(st)
                fl=1
            if (stm[1]=='chr22'):
                break






    file_out.close()
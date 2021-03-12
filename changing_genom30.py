from sys import exit
from my_library import writting_file, checkfile, zagprint, few_columns

if __name__=="__main__":
    name_file = 'num_pol_new_2.txt'
    name_genome_file='genom.fa'
    name_file_out = 'changing_genome.txt'
    file_error=open('polimorf_errors.txt','w')
    full_error=open('polimorf_full_errors.txt','w')
    file_error.write('Хромосома\tchromEnd\tНомер_строки\tПозиция_в_строке\tНомер_строки_в_документе_с_полиморфизмами\tРеференсное_основание\tЗамена\tБуква,_стоящая_в геноме\n')

    name_file_pol = 'genom_var_single_sorted.txt'
    file_pol=open(name_file_pol,'r')
    zagp=file_pol.readline()
    full_error.write(zagp)

    genom=open(name_genome_file,'r')
    file_out = open(name_file_out, 'w')



    zagprint(name_file)

    with open(name_file) as mfile:
        fl2=0
        er=0
        num_pol=0
        num_gen=0
        num_st_pol=0
        chg = 'chr1'
        info=[]

        for st in mfile:
            num_pol += 1
            st=st[:-1]
            stm=st.split('\t')
            ch=stm[0] # ch - название хромосомы полифорфизма
            numst=int(stm[1]) # строка в геономе
            polim=stm[2].split('|')

            while ((num_gen<=numst) or not(ch==chg)):# Пока положение не перевалит за cе И пока хромосома не равна нужной
                stg=genom.readline()[:-1]
                fl2=0
                if not('>' in stg):
                    num_gen+=1
                else:
                    num_gen = 0
                    fl2 = 1
                    chg = stg.rstrip()[1:]
                    info.append('ch {} chg {}'.format(ch,chg))
                    print('{}'.format(ch),end=' ')

                if (fl2==0) and ((num_gen <= numst) or not(ch == chg)): # writting str without replacing !
                    file_out.write(stg + '\n')
                # else:
                #     print(num_gen)
                #     exit()

                if (fl2==1): # writting str with chr without replacing !
                    file_out.write(stg + '\n')
                # while pos<ce
            fl3=0
            for po in polim:
                ed_pol=file_pol.readline()
                num_st_pol+=1
                if fl3==0:
                    nstg = stg.upper()
                    fl3+=1
                else:
                    nstg=nstg1[:-1]
                third = po.split(',')  # one third part
                ost_st = int(third[0]) - 1  #
                strand=third[2]
                loc=third[3]
                al_f=third[4]
                ref = third[1].split('/')[0]
                alt = third[1].split('/')[1]
                if strand=='-':
                    buk=ref.upper()
                    if buk=='A':
                        ref='T'
                    if buk=='T':
                        ref='A'
                    if buk=='G':
                        ref='C'
                    if buk=='C':
                        ref='G'
                    buk = alt.upper()
                    if buk == 'A':
                        alt = 'T'
                    if buk == 'T':
                        alt = 'A'
                    if buk == 'G':
                        alt = 'C'
                    if buk == 'C':
                        alt = 'G'
                pol=ost_st
                refg=nstg[pol] # position from genom

                if ref == refg:
                    if not(pol==0) and not(pol==49):
                        nstg1=nstg[0:pol]+alt+nstg[pol+1:]
                        nstg1 = nstg1 + '\n'
                    if (pol==0):
                        nstg1=alt+nstg[1:]
                        nstg1 = nstg1 + '\n'
                    if (pol==49):
                        nstg1=nstg[0:49]+alt
                        nstg1=nstg1+'\n'


                if (alt == refg):
                    if not(pol==0) and not(pol==49):
                        nstg1=nstg[0:pol]+ref+nstg[pol+1:]
                        nstg1 = nstg1 + '\n'
                    if (pol==0):
                        nstg1=ref+nstg[1:]
                        nstg1 = nstg1 + '\n'
                    if (pol==49):
                        nstg1=nstg[0:49]+ref
                        nstg1=nstg1+'\n'


                if not(alt == refg) and not(ref == refg) and (loc=='e'):
                    if al_f=='ref':
                        rep=ref
                    if al_f=='alt':
                        rep=alt

                    if not(pol==0) and not(pol==49):
                        nstg1=nstg[0:pol]+rep+nstg[pol+1:]
                        nstg1 = nstg1 + '\n'
                    if (pol==0):
                        nstg1=rep+nstg[1:]
                        nstg1 = nstg1 + '\n'
                    if (pol==49):
                        nstg1=nstg[0:49]+rep
                        nstg1=nstg1+'\n'

                if not(alt == refg) and not(ref == refg) and (loc=='o'):
                    nstg1=nstg+'\n'
                    er+=1
                    full_error.write(ed_pol)
                    star=numst * 50 + (ost_st + 1)
                    file_error.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(ch,star,numst+1,ost_st+1,num_st_pol+1,ref,alt,refg))


                if (alt == refg) and (ref == refg):
                    print('Eto kidalovo')
                    exit()
                # for po in polim
            file_out.write(nstg1)
            # for st in mfile

        while not('>' in st):
            st=genom.readline()
            if not ('>' in st):
                file_out.write(st)
        # with open as
    writting_file(name_file,name_file_out)
    genom.close()
    file_out.close()
    for el in info:
        print(el)
    # if name==_main_
    print(num_pol)
    print('er {}'.format(er))

    file_error.close()
    full_error.close()
    file_pol.close()
from sys import exit
from my_library import writting_file, checkfile, zagprint, few_columns



if __name__=="__main__":
    name_file = 'genom_var_single_sorted.txt'
    name_genome_file='genom.fa'
    name_file_out = 'changing_genome.txt'


    genom=open(name_genome_file,'r')
    file_out = open(name_file_out, 'w')



    zagprint(name_file)

    with open(name_file) as mfile:
        pos=0
        fl2=0
        ce50_do=0
        num_pol=0
        info2=[]
        info1=[]
        chg = 'chr1'
        nstg0=''
        info=[]
        zag = mfile.readline()

        for st in mfile:
            num_pol += 1
            st=mfile.readline()
            stm=st.split('\t')
            ch=stm[1] # ch - название хромосомы полифорфизма
            ce=int(stm[3]) # Его положение в геноме (1 начинается с хромосомы)
            ce50=ce//50
            stg0='rororo'
            stg='hahaha'
            pol=-1

            if not(stg0==stg):
                while ((pos<ce) or not(ch==chg)) and not(ce50_do==ce50):# Пока положение не перевалит за cе И пока хромосома не равна нужной
                    stg=genom.readline()[:-1]
                    fl2=0
                    if not('>' in stg):
                        pos += 50
                    else:
                        pos = 0
                        fl2 = 1
                        chg = stg.rstrip()[1:]
                        info.append('ch {} chg {}'.format(ch,chg))
                        print('{}'.format(ch),end=' ')

                    if (fl2==0) and ((pos < ce) or not(ch == chg)): # writting str without replacing !
                        # if (stg.upper()==stg0.upper()) and not('N' in stg):
                        #     print('do| ce: {} \n ce_do: {} \n ce50 {} \n pol: {} \n num_st {} \n '.format(ce, ce50_do, ce50, pol, num_pol))
                        #     print(stg0)
                        #     print(stg)
                        #     genom.close()
                        #     file_out.close()
                        #     exit()
                        file_out.write(stg + '\n')
                        stg0=stg

                    if (fl2==1): # writting str with chr without replacing !
                        file_out.write(stg + '\n')
                        stg0=stg
                    # while pos<ce

            if ce50_do == ce50:
                nstg=nstg0
            else:
                nstg = stg.upper()
            pol=ce-pos+50-1
            refg=nstg[pol] # position from genom

            if stm[20] == refg:
                if not(pol==0) and not(pol==49):
                    nstg1=nstg[0:pol]+stm[20]+nstg[pol+1:]
                    nstg1 = nstg1 + '\n'
                if (pol==0):
                    nstg1=stm[20]+nstg[1:]
                    nstg1 = nstg1 + '\n'
                if (pol==49):
                    nstg1=nstg[0:49]+stm[20]
                    nstg1=nstg1+'\n'
                # if not ce50_do == ce50:
                #     if (nstg1.upper()==stg0.upper()):
                #         print('do| ce: {} \n ce_do: {} \n ce50 {} \n pol: {} \n num_st {} \n '.format(ce, ce50_do, ce50, pol, num_pol))
                #         genom.close()
                #         file_out.close()
                #         exit()
                file_out.write(nstg1)
                stg0=nstg1

            if (stm[21] == refg):
                if not(pol==0) and not(pol==49):
                    nstg1=nstg[0:pol]+stm[21]+nstg[pol+1:]
                    nstg1 = nstg1 + '\n'
                if (pol==0):
                    nstg1=stm[21]+nstg[1:]
                    nstg1 = nstg1 + '\n'
                if (pol==49):
                    nstg1=nstg[0:49]+stm[21]
                    nstg1=nstg1+'\n'
                # if not ce50_do == ce50:
                #     if (nstg1.upper()==stg0.upper()):
                #         print('do| ce: {} \n ce_do: {} \n ce50 {} \n pol: {} \n num_st {} \n '.format(ce, ce50_do, ce50, pol, num_pol))
                #         genom.close()
                #         file_out.close()
                #         exit()
                file_out.write(nstg1)
                stg0=nstg1

            if not(stm[21] == refg) and not(stm[20] == refg):
                # if not ce50_do == ce50:
                #     if (nstg1.upper()==stg0.upper()):
                #         print('do| ce: {} \n ce_do: {} \n ce50 {} \n pol: {} \n num_st {} \n '.format(ce, ce50_do, ce50, pol, num_pol))
                #         genom.close()
                #         file_out.close()
                #         exit()
                file_out.write(nstg+'\n')
                stg0=nstg1

            if (stm[21] == refg) and (stm[20] == refg):
                print('Eto kidalovo')
                exit()
            ce50_do=ce50

            if ce%50 ==0:
                ce50_do-=1
            nstg0=nstg
            # for st in mfile

        while not('>' in st):
            st=genom.readline()
            if not ('>' in st):
                file_out.write(st)
        # with open as
    writting_file(name_file,name_file_out)
    genom.close()
    file_out.close()
    for el in info2:
        print(el)
    # if name==_main_


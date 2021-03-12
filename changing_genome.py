from sys import exit
from my_library import writting_file, checkfile, zagprint, few_columns

#__name__='ha'

if __name__=="__main__":
    name_file = 'genom_var_single_sorted.txt'
    name_genome_file='genom.fa'

    #file_num=open('num_repeat_rep_str.txt','w')
    genom=open(name_genome_file,'r')

    name_file_out = 'changing_genome.txt'
    file_out = open(name_file_out, 'w')
    checkfile(name_file)

    ref_file=open('num_pol.txt','r')

    zagprint(name_file)
    #few_columns(name_file,[0,1,2,3,9,20,21],500)

    ref_nstg1=[]
    ref_nstgp=[]
    with open(name_file) as mfile:
        fl1=0
        fl3=0
        fl4=0
        pos=0
        nstg1=''
        nstg=''
        info1=[]
        zag=mfile.readline()

        ref_st= ref_file.readline()
        ref_num0=int(ref_st.split('\t')[0])  # nomer pedydychei zamenyi
        #print(ref_num0)    #############################
        p_pravo=0
        p_levo=0
        pol_error=0
        pol_right=0
        pol_error_f = 0
        pol_right_f = 0
        num_st_pol=1
        num_st_gen=0
        chg = 'chr1'
        info=[]
        chg0=''
        num_st_gen0=0
        num_st_gen_new=0
        num_p=0
        flp=0
        fl_rep=0
        ref_mas=[]
        ref_par=[]
        beg=0
        ref_num = 0

        for st in mfile:
            st=mfile.readline()

            if beg==0:
                ref_st=ref_file.readline()
                ref_num=int(ref_st.split('\t')[0])  # nomer stroki zamenyi ot nachala chromosomyi
            num_st_pol+=1
            stm=st.split('\t')
            ch=stm[1] # ch - название хромосомы полифорфизма
            ce=int(stm[3]) # Его положение в геноме (1 начинается с хромосомы)
            frec=[]
            frec.append(float(stm[23].split(',')[0]))
            frec.append(float(stm[23].split(',')[1]))


            while (((pos<ce) or (not(ch==chg))) and ((not(ref_num == ref_num0)) or (beg==0))): # Пока положение не перевалит за cе И пока хромосома не равна нужной
                num_st_gen+=1
                #flp=0

                stg=genom.readline()[:-1]
                fl2=0
                if not('>' in stg):
                    pos+=50
                else:
                    pos=0
                    chg0=chg
                    fl2=1

                    if not( (len(stg)==len(ch)+1) or (len(stg)+1==len(ch)+1) or (len(stg)-1==len(ch)+1) ): #checking
                        print('Breaking len in num_st_gen: {}'.format(num_st_gen))
                        print('num_st_pol: {}'.format(num_st_pol))
                        print('pos: {}'.format(pos))
                        print('ce: {}'.format(ce))
                        print('ch: {}'.format(ch))
                        print('chg: {}'.format(chg))
                        exit()


                    chg = stg.rstrip()[1:]
                    info.append('ch {} chg {}'.format(ch,chg))
                    #print('ch {} chg {}'.format(ch,chg))
                    print('{}'.format(ch),end=' ')

                    if ch==chg0 and not(ch=='chr1'): # checking
                        print('Breaking in num_st_gen: {}'.format(num_st_gen))
                        print('num_st_pol: {}'.format(num_st_pol))
                        print('pos: {}'.format(pos))
                        print('ce: {}'.format(ce))
                        print('ch: {}'.format(ch))
                        print('chg: {}'.format(chg))
                        exit()


                if (fl2==0) and ((pos < ce) or not(ch == chg)): # writting str without replacing !
                    file_out.write(stg + '\n')
                    num_st_gen_new += 1

                # if (fl2==0) and (pos < ce): # writting str without replacing !
                #     file_out.write(stg + '\n')
                #     num_p+=1
                #     num_st_gen_new += 1
                #
                # if (fl2==0) and not(ch == chg): # writting str without replacing !
                #     file_out.write(stg + '\n')
                #     num_p += 1
                #     num_st_gen_new += 1

                if (fl2==1): # writting str with chr without replacing !
                    file_out.write(stg + '\n')
                    num_p += 1
                    num_st_gen_new += 1


            # if not num_st_gen==num_st_gen0:
            #     if fl3>0:
            #         file_num.write('#'+str(fl3)+'\n')
            #     nstg=stg.upper() # row from genom
            #     fl3 = 0
            # else:
            #     nstg=nstg1[:-1]
            #     fl3+=1
            #     if fl3==1:
            #         file_num.write(str(num_st_gen_new) + '\n')
            # if not num_st_gen == num_st_gen0:
            #     nstg=stg.upper() # row from genom
            #
            # else:
            #     nstg=nstg1[:-1]
            #     file_num.write(str(num_st_gen_new) + '\n')




                #file_num.write(str(num_st_gen_new) + '\n')




            if not(ref_num == ref_num0) and flp==0:
                nstg = stg.upper()

            if not(ref_num == ref_num0) and flp==1:
                nstg=nstg1[:-1]
                flp=0

            if (ref_num == ref_num0) and flp==1:
                nstg=nstg1[:-1]

            if (ref_num == ref_num0) and flp == 0:
                nstg = stg.upper()  # row from genom
                flp = 1
                # file_num.write(str(num_st_gen_new) + '\n')

            if fl_rep<20:
                ref_mas.append(nstg)
                ref_par.append(' posle: ref_num {} ref_num0 {} flp {}'.format(ref_num,ref_num0,flp))
                fl_rep+=1

            print()
            print(beg)
            print(ref_num0)
            print(ref_num)
            print(nstg)
            pol=ce-pos+50-1
            print(ce)
            print(pos)
            print(pol)
            refg=nstg[pol] # position from genom


            if (stm[20] == refg):# or (stm[21] == refg):
                pol_right+=1
                if (frec[0]>=frec[1]):
                    pol_right_f+=1
                if not(pol==0) and not(pol==49):
                    nstg1=nstg[0:pol]+stm[20]+nstg[pol+1:]
                    nstg1 = nstg1 + '\n'
                if (pol==0):
                    nstg1=stm[20]+nstg[1:]
                    nstg1 = nstg1 + '\n'
                if (pol==49):
                    nstg1=nstg[0:49]+stm[20]
                    nstg1=nstg1+'\n'
                if True or not (ref_num == ref_num0):
                    file_out.write(nstg1)
                    if fl_rep < 20:
                        ref_nstgp.append(nstg1)
                    num_p += 1
                    num_st_gen_new += 1
            if (stm[21] == refg):# or (stm[21] == refg):
                pol_right+=1
                if (frec[0]>=frec[1]):
                    pol_right_f+=1
                if not(pol==0) and not(pol==49):
                    nstg1=nstg[0:pol]+stm[21]+nstg[pol+1:]
                    nstg1 = nstg1 + '\n'
                if (pol==0):
                    nstg1=stm[21]+nstg[1:]
                    nstg1 = nstg1 + '\n'
                if (pol==49):
                    nstg1=nstg[0:49]+stm[21]
                    nstg1=nstg1+'\n'
                if True or not (ref_num == ref_num0):
                    file_out.write(nstg1)
                    if fl_rep < 20:
                        ref_nstgp.append(nstg1)
                    num_p += 1
                    num_st_gen_new += 1
            if not(stm[21] == refg) and not(stm[20] == refg):
                pol_error+=1
                if True or not (ref_num == ref_num0):
                    file_out.write(nstg+'\n')
                    if fl_rep < 20:
                        ref_nstgp.append(nstg1)
                    num_p += 1
                    num_st_gen_new += 1
                if (frec[0]<=frec[1]):
                    pol_error_f+=1
            if (stm[21] == refg) and (stm[20] == refg):
                print('Eto kidalovo')
                print(num_st_pol)
                exit()
            if fl_rep < 20:
                ref_nstg1.append(nstg1)
            num_st_gen0=num_st_gen
            ref_num0=ref_num
            ref_st = ref_file.readline()
            ref_num = int(ref_st.split('\t')[0])  # nomer stroki zamenyi ot nachala chromosomyi
            beg=1
            # if not(num_p==num_st_gen) and fl4<5:
            #     info1.append(num_st_gen)
            #     info1.append(pos)
            #     info1.append(ce)
            #     info1.append(ch)
            #     info1.append(chg)
            #     fl4+=1
        while not('>' in st):
            st=genom.readline()
            if not ('>' in st):
                file_out.write(st)





    # print(p_pravo)
    # print(p_levo)
    print('right: {} \n errors: {} \n all: {} \n poll_right_f {} \n pol_error_f {}'.format(pol_right,pol_error,(pol_right+pol_error),pol_right_f,pol_error_f))  ## 777624
    print('num_st_gen: {}'.format(num_st_gen))
    print('num_st_pol: {}'.format(num_st_pol))
    # print(ce)
    # print(pos)
    # print(ch)
    # print(chg)
    # print('info1:')
    # print(info1)
    print(ref_mas)
    print(ref_nstg1)
    print(ref_nstgp)
    print(ref_par)
    genom.close()
    file_out.close()
    #file_num.close()
    ref_file.close()
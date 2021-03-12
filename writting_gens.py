from sys import exit
from my_library import writting_file, checkfile, zagprint, few_columns

# Просто выписывает все гены из списка.



#name_fgens='gens_spliceAI_sorted_concantenated.txt'
name_fgens = 'gens_dominant.txt'
zagprint(name_fgens)
mfile=open(name_fgens,'r')
#name_genom_file='genom.fa'
name_genom_file = 'gnomad_genome.txt'
genom=open(name_genom_file,'r')
#file_out=open('gens.txt','w')
#file_out = open('pax6.txt','w')
file_out = open('pax6_alt.txt','w')
file_er1=open('gens_splice_er.txt','w')
chm=[]
wrong_gens=0
num_gen=0
num_stgen=1
chg='chr1'
const_s='\n'
fl1=0
buk=''
for st in mfile:
    if fl1==0:
        fl1=1
        continue
    fl3=0
    num_stgen+=1
    stm=st.split('\t')
    ch='chr'+stm[1]
    name1=stm[0]
    #name2=stm[12]

    if not(ch in chm):
        chm.append(ch)

    strand=stm[2]
    start=int(stm[3])
    end=int(stm[4])
    num_st=start//50

    if start%50==0:
        ost_st=50
        num_st-=1
    else:
        ost_st=start%50

    # if (num_gen > num_st) and (ch == chg):
    #     genom.close()
    #     name_genom_file = 'genom.fa'
    #     genom = open(name_genom_file, 'r')
    #     num_gen=0
    while ((num_gen <= num_st) or not (ch == chg)):  # Пока положение не перевалит за cе И пока хромосома не равна нужной
        if fl3==1:
            break
        stg = genom.readline()[:-1]
        fl2 = 0
        if not ('>' in stg):
            num_gen += 1
        else:
            num_gen = 0
            fl2 = 1
            chg = stg.rstrip()[1:]
            print('{}'.format(ch), end=' ')

    if not((num_gen == num_st+1) and (ch == chg)): # this is wrong gens
        wrong_gens+=1
        continue

    pos=ost_st-1
    file_out.write('>{}\n'.format(name1))
    file_out.write('${}\t{}\t{}\t{}\t#{}\t{}\t{}\n'.format(ch,start,num_st,ost_st,num_gen,pos+1,str(num_gen*50+pos+1)))

    # if not(num_st==num_gen):
    #     file_er1.write('>{}\n'.format(name1))
    #     file_er1.write('${}\t{}\t{}\t{}\t#{}\t{}\t{}\n'.format(ch,start,num_st,ost_st,num_gen,pos+1,str(num_gen*50+pos+1)))
    pos_out=1
    tkolvo=end-start+1
    kolvo=0
    while (start <= end):
        if pos==50:
            pos=0
            stg = genom.readline()[:-1]
            if not('>' in stg):
                num_gen+=1
            else:
                num_gen=0
                fl2 = 1
                chg = stg.rstrip()[1:]
                print('{}'.format(ch), end=' ')
        try:
            buk=stg[pos]
        except IndexError:
            print('error')
            print(pos)
            print(stg)
            print(st[:-1])
            print(num_stgen)
            print(num_gen)
            print()
            file_out.write('&&\n')
            fl3 = 1
            break
            # if buk.upper=='N':
            #     file_out.write('\n')
            #     fl3=1
            #     break

        if pos_out==50:
            pos_out=1
            file_out.write('\n')
        file_out.write(buk.lower())
        kolvo+=1
        pos_out+=1
        pos += 1
        start+=1
    file_out.write('\n')
    #file_out.write('%t={}\tr={}\n'.format(str(tkolvo), str(kolvo)))

print(chm)
mfile.close()
genom.close()
file_out.close()
file_er1.close()
print('wrong_gens {}'.format(wrong_gens))
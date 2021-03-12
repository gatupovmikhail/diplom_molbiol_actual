from sys import exit
from my_library import writting_file, checkfile, zagprint, few_columns

def revers(buk):
    if buk.upper()=='A':
        return 'T'
    if buk.upper()=='T':
        return 'A'
    if buk.upper()=='G':
        return 'C'
    if buk.upper()=='C':
        return 'G'
    if buk.upper()=='N':
        return 'N'

def zapis(buk):
    tri=[]
    if buk.upper()=='N':
        tri.append('N')
    if not(buk.upper()=='A'):
        tri.append('A')
    if not(buk.upper()=='T'):
        tri.append('T')
    if not(buk.upper()=='G'):
        tri.append('G')
    if not(buk.upper()=='C'):
        tri.append('C')

    return tri



#########name_fgens='gens_spliceAI_sorted_concantenated.txt' nuzna modificaciya
#################name_fgens = 'gens_dominant.txt'
#name_fgens = 'polim_in_gens_form_concan.txt' # 911 557 506
name_fgens = 'polim_in_gens_form_concan_5.txt'
#name_fgens = 'gens_dominant.txt'
zagprint(name_fgens)
mfile=open(name_fgens,'r')
#name_genom_file='alt_gnom_genom.fa'
name_genom_file='genom.fa'
genom=open(name_genom_file,'r')
file_out=open('for_splice_ai_ref30.vcf','w')
# file_out=open('for_splice_ai_alt20.vcf','w')
#file_out=open('for_splice_ai_ref20.vcf','w')
#file_out = open('splice_polimorfs_alt.vcf','w')
with open('manual.vcf','r') as file_man:
    for st in file_man:
        if not('CHROM' in st) and not('PASS' in st):
            file_out.write(st)
file_out.write('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tSAMPLE\n')
chm=[]
num_gen=0
num_stgen=1
chg='chr1'
fl1=0
buk=''
st_out = 0
for st in mfile:
    if  fl1==0:
        fl1=1
        continue
    fl3=0
    num_stgen+=1
    stm=st.split('\t')
    ch = 'chr' + stm[1]
    pos_var = stm[4].split(',')
    allel = stm[5].split(',')
    idd = stm[6].split(',')
    af = stm[7][0:-1].split(',')



    if not(ch in chm):
        chm.append(ch)

    start=int(stm[2]) ##!
    end=int(stm[3])
    num_st=start//50

    if start%50==0:
        ost_st=50
        num_st-=1
    else:
        ost_st=start%50

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
            print('{}'.format(ch), end=' ')

            chg = stg.rstrip()[1:]
    if not((num_gen == num_st+1) and (ch == chg)):
        continue

    pos=ost_st-1
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
            fl3=1
            if buk.upper=='N':
                fl3=1
                break
        # if strand=='-':
        #     buk=revers(buk)
        bukvas=zapis(buk)
        if not(bukvas[0]=='N'):
            buk_m = '{},{},{}'.format(bukvas[0], bukvas[1], bukvas[2])
            vstavka = ''
            fl_v = 0
            for j in range(len(pos_var)):
                if fl_v == 0:
                    if abs(start - int(pos_var[j])) <= 5:
                        vstavka += 'SNP={ch}|{idd}|{pos_var}|{allel}|{af}'.format(ch=ch, idd=idd[j], pos_var=pos_var[j],allel=allel[j], af=af[j])
                        fl_v = 1
                        continue
                if fl_v > 0:
                    if abs(start - int(pos_var[j])) <= 5:
                        vstavka += ',{ch}|{idd}|{pos_var}|{allel}|{af}'.format(ch=ch, idd=idd[j], pos_var=pos_var[j],allel=allel[j], af=af[j])

            if fl_v == 1:
                const_s = '\t100\tPASS\tMQ=50;{}\tAF:GT\t0.5:0/1\n'.format(vstavka)
                file_out.write('{}\t{}\t.\t{}\t{}'.format(ch,start,buk.upper(),buk_m) + const_s)
                st_out += 1
            else:
                print('WARNING {}'.format(st_out))
        pos += 1
        start += 1


print(chm)
print(st_out) # 363648083    49898743
mfile.close()
genom.close()
file_out.close()
import sys
#areas = open('polim_in_gens_form_concan.txt','r')
areas = open('areas_of_big.vcf','r')
bigf = open('/media/gatupov/Elements1/for_splice_sorted.vcf','r')
file_zag = open('for_splice_ai_alt20.vcf','r')
file_out = open('/media/gatupov/Elements1/for_splice_sorted_full.vcf','w')
# areas = open('areas_of_pax6.vcf','r')
# bigf = open('pax6_ref_alg.vcf','r')
# file_zag = open('pax6_from_razrab_one.vcf','r')
# file_out = open('pax6_razrab_dopis.vcf','w')
#for i in range(44):
zagb = bigf.readline()  ## !!!!!!!!!!!!
#zaga = areas.readline()
stz = '#'
pos = -1
pos0 = -2
chb = '1' #!!!!!!!!!!!!!!!!!!!!!!!!!!
while '#' in stz:
    stz = file_zag.readline()
    if not(stz=='#') and '#' in stz:
        file_out.write(stz)
st0 = 'AR'
gran = 2784646//20
per = 5
n_ar = 0
st = 'A'
for ar in areas:
    n_ar+=1
    if n_ar > gran:
        print('{}'.format(per),end=' ')
        gran+=2784646//20
        per+=5
    arm = ar.split('\t')
    cha = arm[0].replace('chr','')
    start = int(arm[1])
    end = int(arm[2])
    flag = 0
    while chb==cha and pos<=end and not st=='':
        pos0 = pos
        if st0 == 'AR':
            st = bigf.readline()
            if st[0]=='#':
                continue
        else:
            st = st0
            st0 = 'AR'
        stm = st.split('\t')
        chb = stm[0]
        pos = int(stm[1])
        if flag==0 and not(pos==start):
            pos0 = start
            while (pos - pos0) > 0:
                file_out.write('{}\t{}\t.\t{}\n'.format(chb, pos0, 'E'))
                pos0+=1
            file_out.write(st)
        if flag==0 and pos==start:
            file_out.write(st)
        if flag == 1 and (pos - pos0) > 1 and pos<=end:
            while (pos-pos0) > 1:
                pos0+=1
                file_out.write('{}\t{}\t.\t{}\n'.format(chb, pos0, 'E'))
        if flag == 1 and (pos - pos0) == 1 and pos<=end:
            file_out.write(st)
        flag = 1
    while pos0 < end:
        pos0+=1
        file_out.write('{}\t{}\t.\t{}\n'.format(cha, pos0, 'E'))
    st0 = st

file_out.close()
file_zag.close()
bigf.close()
areas.close()
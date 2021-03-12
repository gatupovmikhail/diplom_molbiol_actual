#big_file = open('/media/gatupov/Elements1/spliceai_scores.masked.snv.hg19.vcf','r') ### перед исп привести в порядок
big_file = open('pax6_from_razrab_one.vcf','r')
# areas = open('polim_in_gens_form_concan_sort.txt','r')
#areas = open('gens_dominant.txt','r')
areas = open('areas_of_pax6.vcf','r')
#file_out = open('/media/gatupov/Elements1/splice_ref_tri.vcf','w')
file_out = open('pax6_from_razrab_filtr.vcf','w')
#zag_a = areas.readline()
n_ar = 1
file_error = open('/media/gatupov/Elements1/errors_big.txt','a')
file_error.write('\n pax6\n')
st = 'ho'
while not('#CHROM' in st):
    st = big_file.readline()
file_out.write(st)
pos = -1
chr = '11' #!!!
gran = 140000
per = 5
for ar in areas:
    n_ar+=1
    if n_ar > gran:
        print('{}'.format(per),end=' ')
        gran+=140000
        per+=5
    arm = ar[:-1].split('\t')
    ch_a = arm[0].replace('chr','')
    start = int(arm[1])
    end = int(arm[2])
    while pos < start or not(ch_a==chr):
        st = big_file.readline()
        if not(len(st.split('\t'))<2):
            chr = st.split('\t')[0]
            pos = int(st.split('\t')[1])
        else:
            file_error.write(str(n_ar))
            file_error.write('\n')
            file_error.write(st)
            continue
    if pos > end and ch_a==chr:
        file_error.write('oyzhas '+str(n_ar)+'\n')
    while start<=pos<=end and ch_a == chr:
        if not(len(st.split('\t'))<2):
            file_out.write(st)
        st = big_file.readline()
        if not(len(st.split('\t')) < 2):
            chr = st.split('\t')[0]
            pos = int(st.split('\t')[1])
        else:
            file_error.write(str(n_ar))
            file_error.write('\n')
            file_error.write(st)
            continue

file_error.close()
file_out.close()
areas.close()
big_file.close()
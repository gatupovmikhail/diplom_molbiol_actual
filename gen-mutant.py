from sys import  exit
file_sbork = open('for_splice_ai_alt.vcf','r')
file_out = open('pax6_mut_alt.txt','w')
st = '#'
file_out.write('>PAX6\n$chr11\t31810457\t636209\t7\t#636210\t7\t31810507\n')
while '#' in st:
    st=file_sbork.readline()
stm = st.split('\t')
ref = stm[3]
alt = stm[4]
if ref == alt:
    print('yps')
    print(st)
    exit()
#file_out.write(ref.lower())
i=0
povt = 1
for st in file_sbork:
    stm = st.split('\t')
    ref = stm[3]
    alt = stm[4]
    if ref == alt:
        print('yps')
        print(st)
        exit()
    povt+=1
    if povt == 3:
        file_out.write(ref.lower())
        povt = 0
        i+=1
        if i==49:
            file_out.write('\n')
            i = 0


file_out.close()
file_sbork.close()
name_file='splice_onegen_alt.vcf'
name_file_ref='splice_onegen_alt1.tsv'
file_ref=open(name_file_ref,'r')
file_out=open('splice_onegen_razn.txt','w')
schet = 0
num_st=0
with open(name_file,'r') as mfile:
    for st in mfile:
        num_st+=1
        st_ref = file_ref.readline()
        p_izm=[]
        p_ref=[]
        if '#' in st:
            if 'CHROM' in st:
                print(st[0:-1])
                print(st_ref[0:-1])
        if not('#' in st):
            stm=st[0:-1].split('\t')
            stm_ref=st_ref[0:-1].split('\t')
           # print(stm_ref)
            info=stm[7]
            info_ref=stm_ref[7]
            if len(info.split(';')) > 1 and len(info_ref.split(';')) > 1:
                print(info)
                splice=info.split(';')[1].split('|')
                splice_ref=info_ref.split(';')[1].split('|')
                for i in range(2,6):
                    p_izm.append(splice[i])
                    p_ref.append(splice_ref[i])
                if num_st < 70:
                    print(p_izm)
                    print(p_ref)
                flag=0
                deltam = 0
                for i in range(4):
                    delta = abs(float(p_izm[i]) - float(p_ref[i]))
                    if delta >= 0.05:
                        flag+=1
                        if deltam <= delta:
                            deltam = delta 
                if flag > 0:
                    schet+=1
                    file_out.write(st)
                    file_out.write(st_ref)
                    file_out.write('%{}\n'.format(deltam))
                    #file_out.write('{}|{}|{}|{}\n'.format(p_ref[0],p_ref[1],p_ref[2],p_ref[3]))
                    #file_out.write('{}|{}|{}|{}\n'.format(p_izm[0],p_izm[1],p_izm[2],p_izm[3]))
print('Кол-во отличающихся строк')
print(schet)
file_ref.close()
file_out.close()

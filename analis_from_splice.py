from sys import exit
#long = open('splice_onegen_alt.vcf','r') # более длинный
#long = open('splice_ai_alt_com.vcf','r')
long = open('pax6_alt_20.vcf','r')

# num_short = 56
# num_long = 43
# num_short = 56
# num_long = 46
st_razl = 0
num_short = 43
num_long = 43
probability = 0.5
p_max = [-1]*4
p_min = [2]*4
#file_out = open('alt_analis_from_splice_{:.2}.vcf'.format(probability),'w')
file_out = open('alt20_analis_from_splice_{:.2}.vcf'.format(probability),'w')
file_out.write('#GENOM\tCHROM\tPOS\tREF\tALT\tPROBABILITY(Format: GEN|DS_AG|DS_AL|DS_DG|DS_DL|DP_AG|DP_AL|DP_DG|DP_DL)\n')

# with open('splice_onegen_ref.vcf','r') as short:  # более короткий
#with open('for_splice_ai_ref.norm.filtered.splice_ai.vcf','r') as short:  # более короткий
with open('pax6_ref_20.vcf','r') as short:
    for i in range(num_long):
        stlongz = long.readline()
    for i in range(num_short):
        stshort = short.readline()

    pos_long = [-1]*3
    ref_long = ['H']*3
    alt_long = ['H']*3
    stlong = ['']*3
    info_long = [''] * 3
    for stshort in short:
        num_short+=1
        pos_short = int(stshort.split('\t')[1])
        ref_short = stshort.split('\t')[3]
        alt_short = stshort.split('\t')[4]
        info_short = stshort.split('\t')[7]
        p_short = []
        if not(len(info_short.split('|')) < 2):
            for i in range(2, 6):
                p_short.append(float(info_short.split('|')[i]))
            for i in range(4):
                if p_short[i] < p_min[i]:
                    p_min[i] = p_short[i]
                if p_short[i] > p_max[i]:
                    p_max[i] = p_short[i]
        else:
            p_short.append('.')
        povt = 0
        #while not((pos_short == pos_long) and (alt_short == alt_long) and (ref_short == ref_long)):
        fl = 5
        fl_p = 0
        for k in range(3):
            if (pos_short == pos_long[k]):
                fl_p = 1
            if (pos_short == pos_long[k]) and (alt_short == alt_long[k]) and (ref_short == ref_long[k]):
                fl = k
        #print('1#{}'.format(fl))
        if fl == 5 and fl_p == 0:
            for k in range(3):
                stlong[k] = long.readline()
                num_long+=1
                povt+=1
                pos_long[k] = int(stlong[k].split('\t')[1])
                ref_long[k] = stlong[k].split('\t')[3]
                alt_long[k] = stlong[k].split('\t')[4]
                info_long[k] = stlong[k].split('\t')[7]

            for k in range(3):
                if (pos_short == pos_long[k]):
                    fl_p = 1
                if (pos_short == pos_long[k]) and (alt_short == alt_long[k]) and (ref_short == ref_long[k]):
                    fl = k
                    #print('2#{}'.format(fl))
        #print('3#{}'.format(fl))
        if fl_p == 1 and fl==5:
            # for m in range(3):
            #     print(stlong[k][0:-1])
            # print(stshort[0:-1])
            # print()
            continue

        if fl == 5 and fl_p == 0:
            print('Error: {}\t{}'.format(num_short,num_long))
            for j in range(3):
                print(stlong[j],end='')
            print(stshort)
            exit()


        p_long = []
        if not(len(info_long[fl].split('|')) < 2):
            for i in range(2,6):
                p_long.append(float(info_long[fl].split('|')[i]))
        else:
            p_long.append('.')
        flag = 0
        if not(p_long[0] == '.') and not(p_short[0] == '.'):
            for i in range(4):
                if abs(p_long[i] - p_short[i]) >= probability:
                    flag = 1
        if flag == 1:
            p_long_s = ''
            p_short_s = ''
            for i in range(4):
                p_long_s+=str(p_long[i])+'\t'
                p_short_s+=str(p_short[i])+'\t'
            p_long_s = p_long_s[0:-1]
            p_short_s = p_short_s[0:-1]
            st_razl+=1
            # file_out.write('alt\tchr11\t{}\t{}\t{}\t{}\t{}\n'.format(pos_long[fl],ref_long[fl],alt_long[fl],p_long_s,info_long[fl]))
            # file_out.write('ref\tchr11\t{}\t{}\t{}\t{}\t{}\n'.format(pos_short, ref_short, alt_short,p_short_s,info_short))
            infos_long = info_long[fl].replace('MQ=50;SpliceAI=','')
            infos_long = infos_long[1:len(infos_long)]
            infos_short = info_short.replace('MQ=50;SpliceAI=', '')
            infos_short = infos_short[1:len(infos_short)]
            file_out.write('alt\tchr11\t{}\t{}\t{}\t{}\n'.format(pos_long[fl], ref_long[fl], alt_long[fl],infos_long))
            file_out.write('ref\tchr11\t{}\t{}\t{}\t{}\n'.format(pos_short, ref_short, alt_short, infos_short))

            #file_out.write('\n')
            
print('probability: {}'.format(probability))
print('st_razl: {}'.format(st_razl))
print('p_min: {}'.format(p_min))
print('p_max: {}'.format(p_max))

file_out.close()
long.close()

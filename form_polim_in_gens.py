# Делает из полиморфизмов диапазон позиция +-5
#file_out = open('polim_in_gens_form.txt','w')
file_out = open('polim_in_gens_form_5.txt','w')
file_check = open('genom_startend.txt','r')
check = {}
fl = 0
for st in file_check:
    if fl == 0:
        fl = 1
        continue
    stm = st.split('\t')
    check[stm[0]] = int(stm[1])
file_check.close()
file_out.write(('#GEN\tCHROM\tSTART\tEND\tPOS\tREF/ALT\tID\tAF\n'))
with open('polim_in_gens.txt','r') as polim:
    for st in polim:
        stm = st.split('\t')
        idd = stm[1]
        af = stm[2]
        gen = stm[4].split('||')[1][0:-1]
        ch = stm[0]
        pos = int(stm[3])*50 + int(stm[4].split(',')[0])
        #strand = stm[2].split(',')[2]
        refalt = stm[4].split(',')[1].split('||')[0]
        start = pos - 5
        end = pos + 5
        if start < 1:
            start = 1
        if end >= check[ch]:
            end = check[ch] - 1
        ch_out = ch.replace('chr','')
        file_out.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(gen,ch_out,start,end,pos,refalt,idd,af))

file_out.close()

file0 = open('polim_in_gens_form_concan.txt','r')
zag0 = file0.readline()
file_out = open('areas_for_skoblov.txt','w')
file_out.write(zag0)
const1 = 'OR4F5\t2\t'
const2 = '\t69270\tA/G\trs201219564\t0.662637\n'
# Intron 4
# chr2:166915199\t166929867
# Intron 23
# chr2:166859264\t166866228
# Intron 25
# chr2:166854686\t166856232
ch_pos = ['166854686\t166856232','166859264\t166866228','166915199\t166929867']
for i in range(len(ch_pos)):
    file_out.write(const1+ch_pos[i]+const2)
file_out.close()
file0.close()

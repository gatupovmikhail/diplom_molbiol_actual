# сравнивает геномы
ref_genom = open('genom.fa','r')
alt_genom = open('gnomad_genome.txt','r')
#num = -2 chr1
num = -1 # все ост хромосомы
nesovp = 20
i = 0
refs='a'
while not('chrY' in refs):
    refs = ref_genom.readline()
    alts = alt_genom.readline()
while i <= nesovp:
    num+=1
    refs = ref_genom.readline()
    alts = alt_genom.readline()
    if not(refs == alts):
        refs = refs.lower()
        alts = alts.lower()
        #alts0 = alts
        #print(refs[0:-1])
        for k in range(len(refs)):
            if not(refs[k] == alts[k]):
                refs = refs[0:k] + refs[k].upper() + refs[k+1:len(refs)]
                alts = alts[0:k] + alts[k].upper() + alts[k+1:len(refs)]
        print(num)
        print(refs[0:-1])
        print(alts[0:-1])
        #print(alts0[0:-1])
        print()
        i+=1
ref_genom.close()
alt_genom.close()

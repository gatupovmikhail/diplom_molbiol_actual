from my_library import zagprint
# Всего лишь проверка того, какая ситема позиционирования используется: начинается ли отсчет заного от начала каждой из хромосом, либо же он продолжается,
# а не обнуляется. Оказалось первое верно. Бесполезная прога.
name_file= 'gens_spliceAI_sorted.txt'
polim=[]
with open(name_file) as mfile:
    zag=mfile.readline()
    num=1
    ref='ha'
    minh=1000000000
    maxh=-2
    for st in mfile:
        num+=1
        stm=st.split('\t')
        if maxh<float(stm[3]):
            maxh=float(stm[3])
        if minh>float(stm[3]):
            minh=float(stm[3])
        if not (stm[1] == ref):
            print('{} st {} \n min {} max {}'.format(stm[1],num,minh,maxh))
            print('{}'.format('chr'+stm[1]))
            polim.append(stm[1])
            ref = stm[1]
            minh = 1000000000
            maxh = -2


from sys import exit
import click

@click.command()
@click.argument('number')
def main(number):
    exons = {}
    N = number
    for i in range(1,23):
        exons[str(i)] = []
    exons['X'] = []
    exons['Y'] = []
    razmer_count = 0 # сколько генов с первым экзоном меньше 50
    with open('gens_spliceAI_sorted_concantenated.txt','r') as genf:
        zag = genf.readline()
        print(zag)
        for st in genf:
            fl_razmer = 1
            stm = st[:-1].split('\t')
            gen = stm[0]
            chr = stm[1]
            ex_start = int(stm[5].split(',')[0])
            ex_end = int(stm[6].split(',')[0])
            if ex_end - ex_start <= 50:
                fl_razmer = 0
                razmer_count += 1
            exons[chr].append([gen, ex_start, ex_end, fl_razmer])
    print(exons.keys())
    print(f'Генов с размером 1 экзона меньше 50: {razmer_count}')
    # Проверка, отсортированы ли гены
    # for mas in exons.values():
    #     for i in range(len(mas) - 1):
    #         if mas[i][1] > mas[i+1][1]:
    #             print('oyzhas')
    #             print(mas[i])
    #             print(mas[i+1])


    file_ind = open('ind.txt', 'r')
    ind = int(file_ind.read())
    file_ind.close()
    file_ind = open('ind.txt', 'w')
    file_ind.write(str(ind + 1))
    file_ind.close()
    num_ind = [i for i in range(1, 23)]
    num_ind.append('X')
    num_ind.append('Y')

    #N = num_ind[ind]
    #print(f'Индекс файла: {num_ind[ind]}')
    #N = 1 #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # N = 'Y'
    path = '/media/gatupov/Elements1/Миши_Диплом/'
    name_file = path + 'gnomad.genomes.r2.0.2.sites.chr{}.vcf'.format(N)
    # name_file = 'gnomad.exomes.r2.1.1.sites.Y.vcf'
    gnom = open(name_file, 'r')
    file_out = open(path + 'gnomad_filtr_1exons/gnomad_polim_1exon_chr{}.vcf'.format(N), 'w')
    file_log = open(path + 'gnomad_log.txt', 'a')
    num = 0
    st = '#'
    zag = '#'
    af_ind = 1
    if N == 'Y':
        af_ind = 2

    while ('#' in st):
        zag = st
        st = gnom.readline()
        num += 1
    if ind == 0:
        file_out.write('#CHROM\tPOS\tREF\tALT\tAF\tID\tGEN\n')

    stm = st.split('\t')
    if len(stm) < 7:
        print('fail')
        gnom.close()
        file_out.close()
        file_log.close()
        exit()
    ch = stm[0]
    pos = int(stm[1])
    # id = stm[2]
    # ref = stm[3]
    # alt = stm[4]
    # af = stm[7].split(';')[af_ind].replace('AF=', '')
    for genm in exons[ch]:
        if (genm[1] - 5) <= pos <= (genm[1] + 50):
            if genm[3] == 1:
                #file_out.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('chr' + ch, pos, ref, alt, af, id, genm[0]))
                file_out.write(st)
            else:
                if pos <= genm[2]:
                    file_out.write(st)
                    #file_out.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('chr' + ch, pos, ref, alt, af, id, genm[0]))
        if pos >= genm[1] + 50:
            break


    for st in gnom:
        num += 1
        stm = st.split('\t')
        if len(stm) < 7:
            file_log.write(st)
            continue

        ch = stm[0]
        pos = int(stm[1])
        # id = stm[2]
        # ref = stm[3]
        # alt = stm[4]
        # af = stm[7].split(';')[af_ind].replace('AF=', '')
        for genm in exons[ch]:
            if (genm[1] - 5) <= pos <= (genm[1] + 50):
                if genm[3] == 1:
                    #file_out.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('chr' + ch, pos, ref, alt, af, id, genm[0]))
                    file_out.write(st)
                else:
                    if pos <= genm[2]:
                        #file_out.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('chr' + ch, pos, ref, alt, af, id, genm[0]))
                        file_out.write(st)
            if pos >= genm[1] + 50:
                break

    print('Файл {} успешно обработан\n'.format(name_file))
    gnom.close()
    file_out.close()
    file_log.close()
if __name__ == '__main__':
    main()

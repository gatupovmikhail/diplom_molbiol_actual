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
            stm = st[:-1].split('\t')
            gen = stm[0]
            chr = stm[1]
            ex_start = int(stm[5].split(',')[0])
            ex_end = int(stm[6].split(',')[0])
            exons[chr].append([gen, ex_start, ex_end])
    #print(exons.keys())
    #print(f'Генов с размером 1 экзона меньше 50: {razmer_count}')
    # Проверка, отсортированы ли гены
    # for mas in exons.values():
    #     for i in range(len(mas) - 1):
    #         if mas[i][1] > mas[i+1][1]:
    #             print('oyzhas')
    #             print(mas[i])
    #             print(mas[i+1])

    path = '/media/gatupov/Elements1/Миши_Диплом/'
    if not N == 'Y':
        name_file ='gnomad.genomes.r2.0.2.sites.chr{}.vcf'.format(N)  ##################################
    else:
        name_file ='gnomad.exomes.r2.1.1.sites.Y.vcf'
    gnom = open(name_file, 'r')
    file_out = open('gnomad_polim_1exon.vcf', 'a')
    file_log = open(path + 'gnomad_log.txt', 'a')
    num = 0
    st = '#'
    zag = '#'

    while ('#' in st):
        zag = st
        st = gnom.readline()
        num += 1
    #     file_out.write('#CHROM\tPOS\tREF\tALT\tAF\tID\tGEN\n')

    stm = st.split('\t')
    if len(stm) < 7:
        print('fail')
        gnom.close()
        file_out.close()
        file_log.close()
        exit()
    ch = stm[0]
    pos = int(stm[1])
    for genm in exons[ch]:
        if (genm[2] - 5) <= pos <= (genm[2] + 50):
            file_out.write(genm[0] + '\t' + st)
        if pos >= genm[2] + 50:
            break


    for st in gnom:
        num += 1
        stm = st.split('\t')
        if len(stm) < 7:
            file_log.write(st)
            continue

        ch = stm[0]
        pos = int(stm[1])
        for genm in exons[ch]:
            if (genm[2] - 5) <= pos <= (genm[2] + 50):
                file_out.write(genm[0] + '\t' + st)
            if pos > genm[2] + 50:
                break

    print('Файл {} успешно обработан\n'.format(name_file))
    gnom.close()
    file_out.close()
    file_log.close()
if __name__ == '__main__':
    main()

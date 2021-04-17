# Функции для izvlech_pred_belongs_gens.py. Не тестировалась
import pandas as pd
import sys


def skip_header(fil):
    st = '#'
    while '#' in st:
        curs_pos = fil.tell()
        st = fil.readline()
    fil.seek(curs_pos)


def finished_function(version):
    file_out = open('pred_for_spec_gens_{}.vcf'.format(version), 'w')
    file_gen = open('gens4.vcf','r')
    target_gens = {}
    for st in file_gen:
        stm = st[:-1].split('\t')
        target_gens[stm[1]] = [stm[0], int(stm[3]), int(stm[4])]
    file_gen.close()
    print(target_gens)

    files_dict = {}
    for file_num in range(1,500):
        name_file = '{}_prediction/for_splice_{}_{}.vcf'.format(version, version.lower(), file_num)
        spl_mut = open(name_file,'r')
        if file_num % 25 == 0:
            print(file_num, end = ' ')
        skip_header(spl_mut)
        n_st = 0
        for st in spl_mut:
            n_st += 1
            stm = st[:-1].split('\t')
            chr = stm[0].replace('chr','')
            try:
                pos = int(stm[1])
            except IndexError:
                continue
            if chr in target_gens.keys():
                if target_gens[chr][1] <= pos <= target_gens[chr][2]:
                    if name_file in files_dict.keys():
                        files_dict[name_file].append(n_st)
                    else:
                        files_dict[name_file] = [n_st]

                    file_out.write(st)
        spl_mut.close()
    file_out.close()
    for key in files_dict.keys():
        print('{}: {}'.format(key,files_dict[key]))

if __name__ == '__main__':
    mut = pd.read_csv('spec_mut_all_skor.csv')

    gen_dict = {}
    spec_chroms = []
    for n, el in enumerate(mut['Gene_Symbol']):
        if el in gen_dict.keys():
            gen_dict[el] += 1
        else:
            gen_dict[el] = 1
            spec_chroms.append(mut['GRCh37_CHR'][n])
    #target_gens = list(gen_dict.keys())
    #print(target_gens)
    print(spec_chroms)
    # обработка DataFrame
    mut['Prediction_Ref'] = 'NaN'
    mut['Prediction_Ref_er'] = 'NaN'
    mut['Prediction_Alt'] = 'NaN'
    mut['Prediction_Alt_er'] = 'NaN'
    #print(mut.shape)  # (4360, 6)
    mut.replace({'GRCh37_CHR': {'X': 30}},inplace=True)
    mut['GRCh37_POS'] = [int(x) for x in mut['GRCh37_POS']]
    mut['GRCh37_CHR'] = [int(x) for x in mut['GRCh37_CHR']]
    mut.sort_values(by=['GRCh37_CHR','GRCh37_POS'], inplace=True)
    mut.reset_index(drop=True,inplace=True)
    #mut['GRCh37_CHR'] = [str(x) for x in mut['GRCh37_CHR']]
    #mut.replace({'GRCh37_CHR': {'30': 'X'}}, inplace=True)
    print(mut['GRCh37_CHR'].value_counts())
    #print(mut.head(30))
    version = 'Alt'
    finished_function(version)

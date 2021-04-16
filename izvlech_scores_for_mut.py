import pandas as pd


def skip_header(fil):
    st = '#'
    while '#' in st:
        curs_pos = fil.tell()
        st = fil.readline()
    fil.seek(curs_pos)


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
    target_gens = list(gen_dict.keys())
    print(target_gens)
    print(spec_chroms)
    print(mut.head())
    mut['Prediction_Ref'] = 'NaN'
    mut['Prediction_Ref_er'] = 'NaN'
    #print(mut.shape)  # (4360, 6)

    #mut.sort_values(by=['GRCh37_CHR','GRCh37_POS'],inplace=True)
    #print(mut.head(30))

    def finished_function(target_gens = target_gens, spec_chroms = spec_chroms, version = 'Ref'):
        file_out = open('pred_for_spec_gens_ref.vcf', 'w')
        files_dict = {}
        for file_num in range(1,500):
            name_file = '{}_prediction/for_splice_ref_{}.vcf'.format(version, file_num)
            spl_mut = open(name_file,'r')
            if file_num % 25 == 0:
                print(file_num, end = ' ')
            skip_header(spl_mut)
            flag = 0
            n_st = 0
            for st in spl_mut:
                n_st += 1
                stm = st[:-1].split('\t')
                chr = stm[0].replace('chr','')
                if chr in spec_chroms:
                    try:
                        gen = stm[7].split(';')[2].split('|')[1]
                    except IndexError:
                        if flag == 1:
                            file_out.write(st)
                        continue
                    if gen in target_gens:
                        if name_file in files_dict.keys():
                            files_dict[name_file].append(n_st)
                        else:
                            files_dict[name_file] = [n_st]

                        file_out.write(st)
                        flag = 1
                        continue
                flag = 0
            spl_mut.close()
        file_out.close()
        for key in files_dict.keys():
            print('{}: {}'.format(key,files_dict[key]))  # 4360


    #finished_function(version='Ref')
    n_st_file = 0
    anal_file = open('pred_for_spec_gens_ref.vcf','r')
    for st in anal_file:
        n_st_file += 1
        if n_st_file == 1000:
            print(n_st_file//1000,end=' ')
        stm = st[:-1].split('\t')
        chr = stm[0].replace('chr','')
        pos = stm[1]
        ref = stm[3]
        alt_mas = stm[4].split(',')
        try:
            pred = stm[7].split(';')[2].replace('SpliceAI=','').split(',')
        except IndexError:
            continue
        alt_gen = pred[0].split('|')[1]
        for nrow in range(mut.shape[0]):
            if mut.loc[nrow]['GRCh37_CHR'] == chr:
                if mut.loc[nrow]['Gene_Symbol'] == alt_gen:
                    if mut.loc[nrow]['GRCh37_POS'] == pos:
                        for n_alt, alt in enumerate(alt_mas):
                            if mut.loc[nrow]['GRCh37_ALT'] == alt:
                                if mut.loc[nrow]['GRCh37_REF'] == ref:
                                    mut['Prediction_Ref'] = pred[n_alt]
                                else:
                                    mut['Prediction_Ref_er'] = pred[n_alt]

    mut.to_csv('annotated_mutations.vcf')
    anal_file.close()
# n of ref_files: 70 , 224, 237, 238, 324

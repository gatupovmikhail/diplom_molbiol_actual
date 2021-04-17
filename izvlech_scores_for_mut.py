# Формирование фрейма данных с аннотрованными предсказаниями на основе файла с мутациями и файла с предсказаниями.

import pandas as pd
import sys
import tqdm



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
    #print(mut['GRCh37_CHR'].value_counts())
    #print(mut.head(30))


    #finished_function()  # it is for creating pred_for_spec_gens_ref.vcf and pred_for_spec_gens_alt.vcf


    for nrow in range(mut.shape[0]):
        row_frame = mut.loc[nrow]
        chr_frame = row_frame['GRCh37_CHR']
        gen_frame = row_frame['Gene_Symbol']
        pos_frame = row_frame['GRCh37_POS']
        alt_frame = row_frame['GRCh37_ALT']
        ref_frame = row_frame['GRCh37_REF']
        n_st_file = 0
        if nrow % 200 == 0:
            print(nrow // 100, end=' ')
            #if nrow // 100 == 10:
                #break
        anal_file = open('pred_for_spec_gens_Ref.vcf', 'r')

        for st in anal_file:
            n_st_file += 1

            stm = st[:-1].split('\t')
            chr = stm[0].replace('chr','')
            if chr == 'X':
                chr = 30
            else:
                chr = int(chr)
            pos = int(stm[1])
            ref = stm[3]
            alt_mas = stm[4].split(',')
            try:
                pred = stm[7].split(';')[2].replace('SpliceAI=','').split(',')
            except IndexError:
                print(st)
            alt_gen = pred[0].split('|')[1]
            if chr_frame == chr:
                if pos_frame == pos:
                    for n_alt, alt in enumerate(alt_mas):
                        if alt_frame == alt:
                            if ref_frame == ref:
                                mut['Prediction_Ref'][nrow] = str(pred[n_alt])
                                #print('yep')
                            else:
                                mut['Prediction_Ref_er'][nrow] = str(pred[n_alt])
            if chr > chr_frame:
                break
            if chr == chr_frame and pos > pos_frame:
                break
        anal_file.close()

    for nrow in range(mut.shape[0]):
        row_frame = mut.loc[nrow]
        chr_frame = row_frame['GRCh37_CHR']
        gen_frame = row_frame['Gene_Symbol']
        pos_frame = row_frame['GRCh37_POS']
        alt_frame = row_frame['GRCh37_ALT']
        ref_frame = row_frame['GRCh37_REF']
        n_st_file = 0
        if nrow % 200 == 0:
            print(nrow // 100, end=' ')
            #if nrow // 100 == 10:
                #break
        anal_file = open('pred_for_spec_gens_Alt.vcf', 'r')

        for st in anal_file:
            n_st_file += 1

            stm = st[:-1].split('\t')
            chr = stm[0].replace('chr','')
            if chr == 'X':
                chr = 30
            else:
                chr = int(chr)
            pos = int(stm[1])
            ref = stm[3]
            alt_mas = stm[4].split(',')
            try:
                pred = stm[7].split(';')[2].replace('SpliceAI=','').split(',')
            except IndexError:
                print(st)
            alt_gen = pred[0].split('|')[1]
            if chr_frame == chr:
                if pos_frame == pos:
                    for n_alt, alt in enumerate(alt_mas):
                        if alt_frame == alt:
                            if ref_frame == ref:
                                mut['Prediction_Alt'][nrow] = str(pred[n_alt])
                                #print('yep')
                            else:
                                mut['Prediction_Alt_er'][nrow] = str(pred[n_alt])
            if chr > chr_frame:
                break
            if chr == chr_frame and pos > pos_frame:
                break
        anal_file.close()

    print()
    mut.head(20)
    mut.to_csv('Annotated_mutations.vcf')


# n of ref_files: 70 , 224, 237, 238, 324

import pandas as pd
mut = pd.read_csv('Annotated_mutations.vcf')
print(mut['Prediction_Ref'].isna().sum())  # 4279
print(mut['Prediction_Alt'].isna().sum())   # 4296
print(mut.shape[0]) # 4360
#print(mut['Gene_Symbol'])
mut_f = mut.loc[mut['Prediction_Alt'].notna()].copy(deep=True)
mut_f2 = mut_f.loc[mut['Prediction_Ref'].notna()].copy(deep=True)
#mut_eralt = mut.loc[mut['Prediction_Alt_er'].notna()]
#mut_erref = mut.loc[mut['Prediction_Ref_er'].notna()]   empty Dataaframe
mut_f.drop(['Prediction_Ref_er', 'Prediction_Alt_er', 'Unnamed: 0'], axis=1, inplace=True)
mut_f.replace({'GRCh37_CHR' : {30:'X'}},inplace=True) # 4196
#print(mut['Gene_Symbol'].value_counts())
print(mut_f.shape[0])
print(mut_f.to_string())
#mut_f.to_csv('Some_annotated_mutations.csv', index=False)

#!/bin/bash
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X
do
date && \
gunzip -c /media/gatupov/Elements1/Миши_Диплом/gnomad.genomes.r2.0.2.sites.chr$i.vcf.gz > gnomad.genomes.r2.0.2.sites.chr$i.vcf && \
python3 gnomad_filtr_1exon_reg.py $i && \
rm gnomad.genomes.r2.0.2.sites.chr$i.vcf
done
gunzip -c /media/gatupov/Elements1/Миши_Диплом/gnomad.exomes.r2.1.1.sites.Y.vcf.bgz > gnomad.exomes.r2.1.1.sites.Y.vcf && \
python3 gnomad_filtr_1exon_reg.py Y && \
rm gnomad.exomes.r2.1.1.sites.Y.vcf && \
exit 0

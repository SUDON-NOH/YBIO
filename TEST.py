
# bioservice python

import pandas as pd
from bioservices import UniProt

u = UniProt(verbose=False)

columns_list = ['entry name', 'genes', 'organism', 'protein names', 'sequence','feature(TOPOLOGICAL DOMAIN)', 'feature(TRANSMEMBRANE)', 'feature(SIGNAL)',
                'feature(PROPEPTIDE)','database(RefSeq)', 'database(GeneID)', 'subcellular locations', 'feature(INITIATOR METHIONINE)', 'id']
columns = ','.join(columns_list)

data = u.search("gene_exact:pdcd1 organism:human AND reviewed:yes", frmt='tab', limit=3,
                columns = columns)

data_replace = data.replace("\n", "\t")
data_split = data_replace.split("\t")
RAW_data = data_split[len(columns_list):]


print(RAW_data)





print(UniProt._valid_columns)
x = UniProt._valid_columns
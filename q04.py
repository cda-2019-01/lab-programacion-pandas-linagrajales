##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd
import numpy as np
import itertools
data = pd.read_csv("tbl1.tsv", sep="\t")
c = sorted(data['_c4'].unique())
print(str(c).upper())

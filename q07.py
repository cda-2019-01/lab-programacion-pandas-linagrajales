##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 
import pandas as pd
import numpy as np
import itertools
data = pd.read_csv("tbl0.tsv", sep="\t")
suma = data['_c0']+data['_c2']
data['suma']=suma
data

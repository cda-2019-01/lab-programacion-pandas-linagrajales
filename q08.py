##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 
import pandas as pd
import numpy as np
import itertools
data = pd.read_csv("tbl0.tsv", sep="\t")
m=data['_c3']
ano = [z.split('-')[0] for z in m]
data['ano']= ano
data

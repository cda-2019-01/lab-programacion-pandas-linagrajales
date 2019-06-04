##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 
import pandas as pd
import numpy as np
import itertools
data = pd.read_csv("tbl0.tsv", sep="\t")
data2 = pd.read_csv("tbl2.tsv", sep="\t")
suma = data2.groupby('_c0').sum()['_c5b']
data['suma']= suma
data.groupby('_c1').sum()['suma']

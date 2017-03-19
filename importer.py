import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing, cross_validation

df = pd.read_excel('./data/titanic.xls')

df.drop(['body', 'name'], 1, inplace=True)
df.convert_objects(convert_numeric=True)
df.fillna(0, inplace=True)
print df
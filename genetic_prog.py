# importing dependencies 
import tpot as tp
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np

# loading the data from a comma separated file (csv)
data = pd.read_csv('train.csv')

#clean the data ( data preprocessing )
data_shuffle = data.iloc[np.random.permutation(len(data))]
data = data_shuffle.reset_index(drop=True) ## it was tele before, is this valid naming 

# obtaining the class values 
data_class = data['Class'].values

# Split data with 75% for training and 25% for testing
trainig_indices,validation_indices = training_indices, testing_indices = train_test_split(data.index,stratify=data_class,train_size=0.75,test_size=0.25)

# Genetic programming begins !!! 
tpot = tp.TPOTClassifier(generations=5,verbosity=2) # optimization runs for 5 generations
tpot.fit(tele.drop('Class',axis=1).loc[training_indices].values,tele.loc[training_indices,'Class'].values)

# Score accuracy
tpot.score(tele.drop('Class',axis=1).loc[validation_indices].values,tele.loc[validation_indices,'Class'].values)

# Export the pipeline (generations) as pipeline.py
tpot.export('pipeline.py')

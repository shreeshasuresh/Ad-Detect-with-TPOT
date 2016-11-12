import numpy as np

from sklearn.ensemble import GradientBoostingClassifier, VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from sklearn.preprocessing import FunctionTransformer, RobustScaler

# This file contains the code generated by TPOT which was modified to save the classification result

# Class labels and the feature set are separated
# NOTE: Make sure that the class is labeled 'class' in the data file
tpot_data = np.recfromcsv('data.csv', delimiter=',', dtype=np.float64)
features = np.delete(tpot_data.view(np.float64).reshape(tpot_data.size, -1), tpot_data.dtype.names.index('class'), axis=1)

# The 75%-25% (train data set-test data set) split is done on the unified data set provided
training_features, testing_features, training_classes, testing_classes = \
    train_test_split(features, tpot_data['class'], random_state=42)

# TPOT has selected the below classifier as the best (most optimized) classification algorithm for the given data set
# The parameters of the chosen classifier has been caliberated by TPOT.
exported_pipeline = make_pipeline(
    RobustScaler(),
    GradientBoostingClassifier(learning_rate=0.27, max_features=0.27, n_estimators=500)
)

# Train the major split on the exported pipeline
exported_pipeline.fit(training_features, training_classes)

# Predict class labels for the minor split  
results = exported_pipeline.predict(testing_features)

np.savetxt(
    'predicted-result-GB.csv', # file name
    results,                   # array to save
    fmt='%d',                  # formatting
    delimiter=',',             # column delimiter
    newline='\n',              # new line character
    footer='',                 # file footer
    comments='#',              # character to use for comments
    header='Class')
    
np.savetxt(
    'actual-result-GB.csv',    # file name
    testing_classes,           # array to save
    fmt='%d',                  # formatting
    delimiter=',',             # column delimiter
    newline='\n',              # new line character
    footer='',                 # file footer
    comments='#',              # character to use for comments
    header='Class')


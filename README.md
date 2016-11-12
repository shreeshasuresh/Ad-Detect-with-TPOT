# Ad-Detect-with-TPOT

TPOT is Python tool that automatically creates and optimizes machine learning pipelines using genetic programming.

TPOT is a python library which intelligently automates the entire process of selection of models,tuning of hyperparameters and finding the best representation of our feature dataset.

TPOT will automatically optimize a series of feature preprocessors and models that maximize the cross-validation accuracy on the data set.

TPOT is built on top of scikitlearn,thus the generated pipeline is compatible with all the scikitlearn classifiers and easy to understand to anyone familiar with the library.

We used the TPOT library to find out the most suitable model and hyperparameters for our problem.
After 5 generations of optimization we were able to get a cross validation score of 0.9652 with the ExtraTreesClassifier using the following parameters:

criterion = "entropy".
max_features = 0.24.
n_estimators = 500

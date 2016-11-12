# Detection of Advirtisment in Radio using Genetic Programming and Tpot genetic learning library

## TPOT

TPOT is Python tool that automatically creates and optimizes machine learning pipelines using genetic programming.

TPOT is a python library which intelligently automates the entire process of selection of models,tuning of hyperparameters and finding the best representation of our feature dataset.
<p align="center"><img src="https://github.com/rhiever/tpot/blob/master/images/tpot-ml-pipeline.png"></p>

TPOT will automatically optimize a series of feature preprocessors and models that maximize the cross-validation accuracy on the data set.

TPOT is built on top of scikitlearn,thus the generated pipeline is compatible with all the scikitlearn classifiers and easy to understand to anyone familiar with the library.

We used the TPOT library to find out the most suitable model and hyperparameters for our problem.
After 5 generations of optimization we were able to get a cross validation score of 0.9652 with the ExtraTreesClassifier using the following parameters:

criterion = "entropy".
max_features = 0.24.
n_estimators = 500

## Genetic Programming

Genetic algorithms are inspired by Darwin's theory about evolution. Solution to a problem solved by genetic algorithms is evolved. 
Algorithm is started with a set of solutions (represented by chromosomes) called population. Solutions from one population are taken and used to form a new population. 

This is motivated by a hope, that the new population will be better than the old one. Solutions which are selected to form new solutions (offspring) are selected according to their fitness - the more suitable they are the more chances they have to reproduce.
The process continues until a criterion is met, at which point the classifier and other parameters which meet the criterion are found.

To learn more about Genetic Algoritms and Genetic Programming
http://www.obitko.com/tutorials/genetic-algorithms/index.php

To learn more about the tpot library
http://www.randalolson.com/2016/05/08/tpot-a-python-tool-for-automating-data-science/

https://rhiever.github.io/tpot/

https://github.com/rhiever/tpot

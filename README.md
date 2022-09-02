# CECAM 2022 - MLQCDyn school 

![python version](https://img.shields.io/badge/python-3.8-blue?logo=python)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maxjr82/CECAM-MLQCDyn/blob/main/tutorial/UL_for_MD.ipynb)

Welcome to the repository for the unsupervised learning tutorial lecture of the [*Machine Learning 
and Quantum Computing for Quantum Molecular Dynamics* - MLQCDyn](https://www.cecam.org/workshop-details/1133) 
school held in September 2022 in the Université Gustave Eiffel, Paris. This repository contains a Jupyter Notebook 
with Python code to demonstrate, in practice, the application of the popular unsupervised learning methods 
(dimensionality reduction and clustering) to analyze molecular dynamics data and extract useful chemical insights. 
The popular [MD17 database](http://www.sgdml.org/#datasets) generated from *ab initio* molecular dynamics 
simulations is used as a motivating example for the analyses presented in the tutorial.


## Main topics covered in this tutorial 

- Dimensionality reduction
  - Principal Component Analysis (PCA);
  - Kernel PCA.

- Clustering analysis
  - Hard partition clustering with K-Means;
  - Evaluation metrics for clustering.

## Requirements

The tutorial was designed to run in a jupyter notebook environment with

- python3 (tested with version 3.8.1)

The following Python packages are necessary to run the tutorial:

- Math and data processing libraries:

  - pandas
  - numpy
  - scikit-learn

- For visualization:

  - seaborn
  - matplotlib

- Specialized packages for chemistry:

  - [ase (atomic simulation environment)](https://wiki.fysik.dtu.dk/ase/)
  - py3Dmol

The tutorial can be also executed on-line via [Google Colab](https://colab.research.google.com/github).

## References

1. A. Glielmo, B. E. Husic, A. Rodriguez, C. Clementi, F. Noé, and A. Laio, *Chem. Rev.*, 2021, **121** (16), 9722-9758
2. M. Ceriotti, *J. Chem. Phys.*, 2019, **150**, 150901
3. T. Hastie, R. Tibshirani, J. Friedman, *The Elements of Statistical Learning: Data Mining, Inference*, and Prediction, 2nd ed., Springer-Verlag, New York, 2009

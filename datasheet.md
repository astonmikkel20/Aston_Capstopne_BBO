# Datasheet for BBO Capstone Dataset

## Motivation

This dataset was created to support the Black-Box Optimisation (BBO) capstone project. The objective is to identify high-performing query points for a set of unknown functions while only observing input-output pairs generated through iterative submissions.

The dataset supports surrogate modelling, optimisation, uncertainty estimation and query selection.

## Composition

The dataset consists of:

* Query coordinates submitted to eight unknown functions.
* Corresponding function evaluations returned by the capstone platform.
* Historical observations collected across ten optimisation rounds.

Current dataset size:

* 8 functions
* Approximately 18 observations per function
* Numerical tabular format

Potential gaps include unexplored regions of the search space due to the limited query budget.

## Collection Process

The dataset was collected iteratively through the BBO challenge platform.

Queries were generated using:

* Gaussian Process surrogate models
* Neural Network surrogate models
* Hyperparameter tuning techniques
* Exploration and exploitation strategies

Data collection occurred over multiple weekly submissions throughout the programme.

## Preprocessing and Uses

Preprocessing steps included:

* Feature scaling
* Candidate generation
* Model fitting
* Surrogate evaluation

Intended uses:

* Black-box optimisation
* Surrogate modelling
* Query selection research
* Bayesian optimisation experimentation

Inappropriate uses:

* General predictive modelling outside the challenge
* Scientific conclusions about the unknown functions

## Distribution and Maintenance

The dataset is maintained by the project author as part of the Imperial College London Professional Certificate in Machine Learning and Artificial Intelligence capstone project.

The dataset is stored within the project GitHub repository and updated after each challenge round.

Access is intended for educational and research purposes.

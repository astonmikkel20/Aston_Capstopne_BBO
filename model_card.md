# Model Card: Hybrid BBO Optimisation Framework

## Overview

Model Name:
Hybrid BBO Optimisation Framework

Version:
v1.0

Model Type:
Surrogate-assisted black-box optimisation

## Intended Use

This framework is designed to identify promising query locations in unknown objective functions under a restricted evaluation budget.

Suitable for:

* Black-box optimisation
* Bayesian optimisation experiments
* Sequential decision making

Not suitable for:

* Safety-critical systems
* Real-time control applications
* High-confidence scientific inference

## Details

The framework evolved across ten optimisation rounds.

Key components included:

1. Gaussian Process Regression

   * Mean prediction
   * Uncertainty estimation
   * Upper Confidence Bound acquisition

2. Neural Network Surrogate Models

   * TensorFlow implementation
   * Non-linear function approximation

3. Hyperparameter Tuning

   * Manual tuning
   * Random search
   * Model comparison

4. Exploration vs Exploitation

   * Early rounds favoured exploration
   * Later rounds increasingly focused on exploitation

## Performance

Performance was evaluated using:

* Best observed function value
* Improvement over previous rounds
* Surrogate model MSE
* Query quality metrics

The framework successfully identified increasingly promising regions across all eight functions as additional observations became available.

## Assumptions and Limitations

Assumptions:

* Similar inputs produce similar outputs.
* Useful local structure exists.
* Historical observations remain informative.

Limitations:

* Small dataset size.
* Limited evaluation budget.
* Possible sampling bias.
* Risk of converging to local optima.

## Ethical Considerations

Transparency is important because optimisation decisions are influenced by model assumptions and sampling history.

Maintaining detailed documentation improves reproducibility, allows independent review of modelling decisions and facilitates adaptation of the framework to future optimisation problems.

Additional documentation would further improve reproducibility, particularly regarding hyperparameter choices and candidate generation strategies.

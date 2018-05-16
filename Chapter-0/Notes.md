# Notes
> About Data Science 

## Statistics
* Simpson's Paradox
  * Correlation's can be misleading (completely wrong) when ignoring confounding variables
  * Correlation only measures a relationship when all other variables are equal (fine for random assignment)
    * Like concluding West Coast people have more friends, when West Coast had many more PhD's than East Coast (multi-variate analysis)
* Correlation doesn't tell you about the strength of a relationship, and only measures a linear relationship.

```python
# These have a perfectly 0 correlation, though there is a relationship (non-linear)
x = [-2,-1,0,1,2]
y = [2,1,0,-1,-2]
```

* You can be more confident of causality if you make random trials, and the independent variable changes the outcome.

## Probability
* Standard normal distribution: $\mu = 0$ and $\sigma = 1$
* Check for normality before determining the p value (or else your data is meaningless)
* Be careful about p tests with Big Data (understand Bayesian inference)

## Gradient descent
* Gradient is a vector of partial derivatives that points to where the function most quickly increases
* If there's an absolute minimum, gradient descent will find it. If there's multiple, gradient descent may find one of the local minima. If there's none, it may run forever
* Derivative is the limit at a point x when the change in x (h) approaches 0. It's the slope of the tangent line at (x, f(x)), while the difference quotient is the slope of the not-quite tangent line.
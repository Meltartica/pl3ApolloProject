# Hippopotamus (Hypothesis Testing Calculator)

## Programming Language:
- [Python](https://www.python.org/) with [Conda Kernel](https://www.anaconda.com/products/distribution)

## Python Libraries Used:
- [NumPy](https://numpy.org/)
  - Modulized Division, Multiplication, Exponents, and Square Root
- [Math](https://docs.python.org/3/library/math.html)
  - Same as NumPy
- [SciPy](https://scipy.org/)
  - Distribution Types Data (Z-Distribution, T-Distribution, etc.)
- [Colorma](https://github.com/tartley/colorama) (Fore, Style)
  - Adding Color to the Font

## Project Description:
- The goal of this project is to develop a program that can perform hypothesis testing for various statistical scenarios. 
- The program should take in user inputs for the statistical data, the level of significance, and the type of test. 
- The program will used the given data to get the scores and critical point then summing up with either rejecting or accepting the null hypothesis.

## Key Features:
- User-friendly interface for inputting statistical data and hypotheses
- Calculation of test statistic and p-value
- Selection of appropriate statistical test based on user input (e.g., t-test, z-test, chi-squared test, etc.)
- Interpretation of results based on user-specified level of significance (e.g., reject or fail to reject null hypothesis)

## Supported Types:
### Single Population
- **Case A**: Single Population Where Sigma is Known or Sample is Large
- **Case B**: Sigma is Unknown or Sample is Small
- **Test for Proportions**: Single Population
- **Variance** For Single Population"

### Two Population
- **Case C**: Two Mean Big Sample Size or Population Standard Deviation is Given
- **Case D**: Two Mean Small Sample Size and Population Sample Standard Deviation assumed Equal
- **Case E**: Two Mean Small Sample Size and Population Sample Standard Deviation not Equal
- **Case F**: Paired Observation
- **Test for Proportions**: Two Population
- **Variance** For Two Populations

## Utilized Statistical Distribution Table Types:
- Z-Distribution
- T-Distribution
- Chi-Square Distribution
- F-Distribution

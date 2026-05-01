"""
This script cointains statistic functions.
"""
import pandas as pd

import scipy.stats as st
from scipy.stats import norm, kstest
from scipy.stats import pearsonr

# mean and standard deviation for normal distribution
mean, std_dev = 0, 1
# the significance level
alpha = 0.05

def check_normality(data):
  """
    This function performs Kolmogorov-Smirnov test for normality.

    The function takes a parameter:
      - data - a dataset.

    The function prints the result of the test.
  """
  for column in data.columns:
    norm_test = kstest(data[column], 'norm', args = (mean, std_dev))
    print(f"{column} - p-value: {norm_test.pvalue:.4f}")
    if norm_test.pvalue < alpha:
      print("Reject the null hypothesis: The sample does NOT follow the normal distribution.")
    else:
      print("Fail to reject the null hypothesis: The sample follows the normal distribution.")

def calculate_corr_and_pvalue(data, continents, oil):
  """
    This function performs scipy.stats.pearsonr to
    calculate correlation coefficient and p-value.

    The function takes three parameters
      - data - a dataset
      - continents - a list of the continents columns
      - oil - the oil column

    The function returns a list of the results for each continent in format
        [continent, correlation coeff, p-value].
  """
  result = []
  for column in continents:
    corr, pvalue = pearsonr(data[column], data[oil])
    result.append([column, corr, pvalue])

  return result


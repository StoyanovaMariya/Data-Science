"""
This script cointains general functions.
"""

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler

from scripts.stat_functions import calculate_corr_and_pvalue
from scripts.plots import plot_correlation_and_pvalue

def z_normalization(data):
  """
  This function standardizes features using StandardScaler.

  The function takes a single parameter:
    - data - a dataset
      
  The result is the transformed data.
  """
  
  scaler_std = StandardScaler()
  scaler_std.fit(data)

  scaled = scaler_std.fit_transform(data)
  res = pd.DataFrame(scaled, columns = data.columns)

  return res

def shift_column_in_dataset(data, column, period):
  """
  This function moves the data values with the passed period.

  The function takes three parameters:
    - data - a dataset
    - column - the column to be shifted
    - period - the number of periods to shift
      
  The result is the transformed data.
  """
    
  data[column] = data[column].shift(period)
  data.dropna(inplace = True)

def correlation_and_p_value(data, continents, oil):
  """
  This function calculates correlation coefficient and p-value and
  plots the results.

  The function takes three parameters:
    - data - a dataset
    - continents - a list of the continents columns
    - oil - the oil column

  The result is printed and visualized by two scatter plots.
  """

  # calculate pearson correlation and p-value
  res = calculate_corr_and_pvalue(data, continents, oil)

  # print "{0:0.2f}".format(round(x, 2))
  # {0.2f} will format a float to 2 decimal places.
  #round(x, 2) will round up to 2 decimal places.
  # print the results
  for sublist in res:
    print(f"{sublist[0]}: correlation coefficient = {sublist[1]:.2f}, p-value = {sublist[2]:.2f}")

  # plot the results
  plot_correlation_and_pvalue(res)
"""
This script cointains functions to visualize data.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_density(data):
    """
    This function visualizes the distribution of observations in a dataset.

    The function takes a parameter:
      - data - a dataset.

    The result is a kernel density estimate plot.
    """
    
    fig, axs = plt.subplots(1, 7, figsize=(24, 4))

    for i, column in enumerate(data.columns):
        sns.kdeplot(data[column], ax = axs[i], fill = False)
        axs[i].set_title(column)
        axs[i].set_xlabel('Price (USD)')

        if i == 0:
            axs[i].set_ylabel('Density')
        else:
            axs[i].set_ylabel('')
 
    plt.show()

def plot_cross_correlation(data, continents):
    """
    This function measures the similarity between oil and grocery prices
    as one month lag is applied to oil prices.

    The function takes two parameters:
      - data - a dataset
      - continents - a list of the continents columns

    The function plots the result.
    """

    lags = np.arange(0, 4)

    plt.figure(figsize=(10, 6))
    # compute cross-correlation
    for column in continents:
        cross_corr = [data[column].corr(data["USO"].shift(lag)) for lag in lags]    
        plt.plot(lags, cross_corr, marker='o', label = column)

    plt.title('Cross-Correlation between oil and breakfast grocery basket prices')
    plt.xlabel('Lag (months)')
    plt.ylabel('Correlation')
    plt.axhline(0, color = 'black', linestyle = '--')
    plt.grid(ls = ':', lw = '2')
    plt.legend()
    plt.show()

def plot_percentage_change(data):
    """
    This function visualizes the similarity between the percentage
    change of oil and grocery prices.

    The function takes a single parameter:
      - data - a dataset
      
    The result is a box plot.
    """

    plt.boxplot(data, tick_labels = data.columns)

    plt.title("Percentage change of oil and breakfast grocery basket prices")
    plt.ylabel("Percentage")
    plt.xticks(rotation=90)
    plt.show()

def plot_correlation_and_pvalue(results):
    """
    This function visualizes the previously calculated 
    correlation coefficient and p-value.

    The function takes a single parameter:
      - results - a list of format 
        [continent, correlation coeff, p-value]
      
    The result is two scatter plots.
    """

    fig, ax = plt.subplots(2, 1, figsize=(8, 10))

    # plot correlation coeficient
    pos_color = 'firebrick'
    neg_color = 'steelblue'
    corr_values = [-1, -0.8, -0.4, 0, 0.4, 0.8, 1]
    corr_levels = [-0.9, -0.6, -0.2, 0.2, 0.6, 0.9]
    corr_labels = ['Strong', 'Moderate', 'Weak', 'Weak', 'Moderate', 'Strong']
    alpha_values = [0.2, 0.5, 0.8]

    ax[0].set_ylim(-1, 1)
    ax[0].set_yticks(corr_levels)
    ax[0].set_title('Correlation between oil and breakfast grocery basket prices')
    ax[0].set_ylabel('Correlation')

    for i in range(len(corr_values)):
        if corr_values[i] == 0:
            alpha_v = alpha_values[i - 3]
            ax[0].axhline(corr_values[i], color='white', linestyle='--')
            ax[0].axhspan(corr_values[i], 
                          corr_values[i + 1], 
                          color = pos_color,
                          alpha = alpha_v
                          )
        elif corr_values[i] > 0:
            ax[0].axhline(corr_values[i], color = pos_color, alpha = alpha_values[i - 4])
            if (i + 1) < len(corr_values):
                ax[0].axhspan(corr_values[i], 
                              corr_values[i + 1], 
                              color = pos_color, 
                              alpha = alpha_values[i - 3]
                              )
        else:
            alpha_v = alpha_values[2 - i]
            ax[0].axhline(corr_values[i], color = neg_color, alpha = alpha_v)
            ax[0].axhspan(corr_values[i], 
                          corr_values[i + 1], 
                          color = neg_color, 
                          alpha = alpha_v)

    ax[0].text(-1.5, 1.0, 'Positive', style='italic', fontsize=16, color = pos_color)
    ax[0].text(-1.5, -1.1, 'Negative', style='italic', fontsize=16, color = neg_color)

    labels = [item.get_text() for item in ax[0].get_yticklabels()]
    for i in range(len(labels)):
        labels[i] = corr_labels[i]

    ax[0].set_yticklabels(labels)
    ax[0].grid(False)

    for sublist in results:
        ax[0].scatter(x = sublist[0], y = sublist[1], c = 'black')

    # plot p-value
    ax[1].scatter(x = [sublist[0] for sublist in results], 
                  y = [sublist[2] for sublist in results]
                  )
    ax[1].axhline(y=0.05, color="red", linestyle="-", label = "Significance level")

    ax[1].set_title('P-value of the correlation')
    ax[1].set_ylabel('P-value')
    ax[1].legend()
    ax[1].set_ylim(0,1)

    plt.show()
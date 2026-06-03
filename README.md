# The Impact of US Oil Price on the Breakfast Grocery Basket Price in Different Continents

This study analyses the impact of US oil price on the grocery breakfast basket prices in different continents and answers the following questions:

  1. Do oil and grocery costs move in the same direction, i.e., an increase of oil prices results in higher grocery costs and a decrease in oil prices results in lower grocery costs?

  2. What is the lagging effect in short term?

  3. Does the grocery basket increase/decrease with the similar percentage with US oil fund?
     

## Features

  1. Data analysis and manipulation: Pandas functions /loc, groupby, pivot, to_datetime, concat, shift/

  2. Preprocessing: sklearn.StandardScaler for Z-score normalization

  3. Statistics implementation:

     - scipy.stats.kstest for performing Kolmogorov-Smirnov test for goodness of fit
    
     - scipy.stats.pearsonr for running Pearson correlation to measure the linear relationship between two datasets

  4. Visualisatios:

     - seaborn.kdeplot for distribution of observations
    
     - matplotlib.pyplot /plot, boxplot, scatter, subplots/ for correlation

  5. Read/write to JSON file

  6. Python package and modules to organize the code
     


## Quick Start

  1. Clone the repository
     
     https://github.com/StoyanovaMariya/Data-Science

  2. Create a virtual environment and install dependencies
     
     requirements.txt
     
  3. For preprocessing run the jupyter notebooks
     
     notebooks\01_grocery_preprocessing.ipynb
     
     notebooks\02_USO_preprocessing.ipynb

  4. For  final results run Main jupyter notebook
     
     Main.ipynb


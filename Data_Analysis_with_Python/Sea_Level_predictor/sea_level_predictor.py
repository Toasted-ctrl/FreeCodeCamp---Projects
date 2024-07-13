
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

##Took some inspiration from (as I did not quite understand how to create the two best fit lines at first):
# https://www.youtube.com/watch?v=mQunppIWH4c
# https://www.youtube.com/watch?v=RJxJEZrx9X0

def draw_plot():
    # Read data from file

    df = pd.read_csv("Data_Analysis_with_Python\Sea_Level_predictor\epa-sea-level.csv")
    print(df.head())
    print('\n')

    # Create scatter plot

    #values for x in linregress
    x = df["Year"]

    #values for y in linregress
    y = df["CSIRO Adjusted Sea Level"]

    fig, ax = plt.subplots(figsize=(10,10))
    ax1 = plt.scatter(x, y)

    # Create first line of best fit

    # regression.slope = a, regression.intercept = b
    regression = linregress(x, y)

    # x_pred = x
    x_pred = pd.Series([i for i in range(1880,2051)])

    # formula is basically ax + b
    y_pred = regression.slope*x_pred + regression.intercept

    ax2 = plt.plot(x_pred, y_pred)

    slope_1 = str(regression.slope)
    intercept_1 = str(regression.intercept)
    print(f"Best fit 1: The slope = {slope_1}.")
    print(f"Best fit 1: The intercept = {intercept_1}.")
    print(f"Best fit 1: Formula = ( {slope_1} * x2_pred ) + {intercept_1}.\n")

    # Create second line of best fit

    # creating new dataframe with only year >= 2000
    df_second_fit = df.loc[df['Year'] >= 2000]

    #values for x in linregress
    x2 = df_second_fit["Year"]

    #values for y in linregress
    y2 = df_second_fit["CSIRO Adjusted Sea Level"]

    #regression_2.slope = a, regression_2.intercept = b
    regression_2 = linregress(x2, y2)

    #x2_pred = x
    x2_pred = pd.Series([i for i in range(2000,2051)])

    #formula is basically ax + b
    y2_pred = regression_2.slope*x2_pred + regression_2.intercept

    #formula is basically ax + b
    ax3 = plt.plot(x2_pred, y2_pred)

    slope_2 = str(regression_2.slope)
    intercept_2 = str(regression_2.intercept)
    print(f"Best fit 2: The slope = {slope_2}.")
    print(f"Best fit 2: The intercept = {intercept_2}.")
    print(f"Best fit 2: Formula = ( {slope_2} * x2_pred ) + {intercept_2}.\n")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()
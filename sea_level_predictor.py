import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')
    #print(df.head())

    # Create scatter plot
    fig=plt.figure(figsize=(10,10),dpi=150)
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Create first line of best fit
    mask=df['Year']>=2000
    res=linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope=res[0]
    intercept=res[1]
    x_pred=pd.Series(range(df['Year'].min(), 2051))
    y_pred=intercept+slope*x_pred
    plt.plot(x_pred, y_pred, color='red', label='Regression Line')

    # Create second line of best fit
    mask=df['Year']>=2000
    df=df[mask]
    res=linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope=res[0]
    intercept=res[1]
    x_pred=pd.Series(range(df['Year'].min(), 2051))
    y_pred=intercept+slope*x_pred
    plt.plot(x_pred, y_pred, color='green', label='Regression Line')

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
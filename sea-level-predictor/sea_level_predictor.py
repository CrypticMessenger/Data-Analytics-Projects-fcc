import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")

    
    # Create scatter plot and Create second line of best fit
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
    regression=linregress([df['Year'],df['CSIRO Adjusted Sea Level']])
    x=np.array([x for x in range(1880,2051)])
    y=regression[0]*x+regression[1]
    plt.plot(x,y) 
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
    df1=df[df['Year']>=2000]
    regression1=linregress(df1['Year'],df1['CSIRO Adjusted Sea Level'])
    x=x=np.array([x for x in range(2000,2051)])
    y=regression1[0]*x+regression1[1]
    plt.plot(x,y,'b-') 
    
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")  



    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
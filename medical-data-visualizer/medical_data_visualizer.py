import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist.axislines import Subplot

# Import data
df=pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight']=((df['weight']/(df['height']/100)**2)>25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol']=(df['cholesterol']>1).astype(int)
df['gluc']=(df['gluc']>1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = pd.melt(frame=df, value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],id_vars=['cardio']
  )

  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
  
  # @BeauCarnes conversation on github helped me with using pd.melt function.
  df_cat = pd.DataFrame(df_cat.groupby(['variable', 'value', 'cardio'])['value'].count()).rename(columns={'value': 'total'}).reset_index()

  # Set up the matplotlib figure and draw the catplot
  sns.catplot(x='variable', y='total', hue='value',col='cardio', data=df_cat, kind='bar')

  plt.savefig('catplot.png')
  return plt.gcf()


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) & 
    (df['weight'] <= df['weight'].quantile(0.975))]
    # Calculate the correlation matrix
    corr = df_heat.corr()
    corr=round(corr,1)

    # Generate a mask for the upper triangle
    #masking snippet taken from gfg, now i know what it is.
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True



    # Set up the matplotlib figure
    fig,ax=plt.subplots() 

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot = True,fmt='.1f',mask=mask)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

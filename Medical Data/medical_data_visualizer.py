import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Importing the data used in the analysis

data_path='medical_examination.csv'
df = pd.read_csv(data_path)


# Creating the overweight column

#df['overweight']=((df['weight']/(df['height']/100)**2) >25).replace({True: 1, False: 0})
df['overweight']=((df['weight']/(df['height']/100)**2) >25)*1

# Normalizing the data by making 0 always good and 1 always bad

df['cholesterol']=(df['cholesterol']>1)*1
df['gluc']= (df['gluc']>1)*1

# Grouping and Plotting cholesterol, gluc, smoke, alco, active and overweight variables by cardio levels

def draw_cat_plot():
    
    var_to_plot=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    df_cat = pd.melt(df,id_vars='cardio',value_vars=var_to_plot)
    
    df_cat['total']=1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'],as_index=False).count()
    
    chart=sns.catplot(x='variable',y='total',data=df_cat,hue='value',kind='bar',col='cardio')

    fig = chart.fig

    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    # Data Cleaning: Keep only the records of patients with heights, weights between the 2.5th and 97.5th 
    # percentiles and with diastolic pressure less than systolic.

    height_filter=((df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)))
    weight_filter=((df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975)))
    diastolic_systolic=(df['ap_lo'] <= df['ap_hi'])
    df_heat = df.loc[height_filter & weight_filter & diastolic_systolic]

    # Calculate the correlation matrix

    corr = df_heat.corr()

    # Generate a mask for the upper triangle

    mask = np.triu(np.ones_like(corr, dtype=bool))



    # Plot the correlation matrix using seaborn

    fig, ax = plt.subplots()

    sns.heatmap(data=corr, vmin = -0.12, vmax = 0.3, center=0, annot=True, annot_kws={'size':9}, 
                cbar_kws={"shrink": 0.7}, fmt="0.1f", linewidths=0.5, mask=mask)
    
    fig.savefig('heatmap.png')
    return fig

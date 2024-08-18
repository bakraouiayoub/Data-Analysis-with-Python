import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data_path='epa-sea-level.csv'
    sea_level_df=pd.read_csv(data_path)

    scatter_plot=sea_level_df.plot(kind='scatter',x="Year",y='CSIRO Adjusted Sea Level',
                                   label='CSIRO Adjusted Sea Level Data',figsize=(10,6))
    scatter_plot.set_title('Rise in Sea Level')
    scatter_plot.set_ylabel('Sea Level (inches)')

    # Linear fit using all the data
    lin_fit_1880=linregress(sea_level_df['Year'],sea_level_df['CSIRO Adjusted Sea Level'])
    years_1880_to_2050=np.arange(sea_level_df['Year'].min(),2051)
    projected_CSIRO_1880=lin_fit_1880.intercept + lin_fit_1880.slope * years_1880_to_2050

    # Linear fit based only on the observations recorded after year 2000
    sea_level_df_2000=sea_level_df.loc[sea_level_df['Year']>=2000]
    lin_fit_2000=linregress(sea_level_df_2000['Year'],sea_level_df_2000['CSIRO Adjusted Sea Level'])
    years_2000_to_2050=np.arange(sea_level_df_2000['Year'].min(),2051)
    projected_CSIRO_2000=lin_fit_2000.intercept + lin_fit_2000.slope * years_2000_to_2050

    scatter_plot.plot(years_1880_to_2050,projected_CSIRO_1880,'r',
                  label=f'CSIRO 1880 - 2050 projection: y = {lin_fit_1880.slope:.2f}x - {-lin_fit_1880.intercept:.2f}')
    scatter_plot.plot(years_2000_to_2050,projected_CSIRO_2000,'g',
                  label=f'CSIRO 2000 - 2050 projection: y = {lin_fit_2000.slope:.2f}x - {-lin_fit_2000.intercept:.2f}')
    plt.legend(fontsize = 'medium')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()

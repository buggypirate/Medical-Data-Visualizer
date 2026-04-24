import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np

# 1. Import the data from medical_examination.csv and assign it to the df variable.
df = pd.read_csv('medical_examination.csv')

# 2. Add an overweight column to the data
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# 3. Normalize data by making 0 always good and 1 always bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# 4. Draw the Categorical Plot in the draw_cat_plot function
def draw_cat_plot():
    # 5. Create a DataFrame for the cat plot using pd.melt
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # 6. Group and reformat the data in df_cat to split it by cardio
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # 7. Convert the data into long format and create a chart
    fig = sns.catplot(data=df_cat, kind='bar', x='variable', y='total', hue='value', col='cardio')
    
    # 8. Get the figure for the output
    fig.fig.suptitle('Categorical Plots by Cardio')
    
    return fig.fig


# 9. Draw the Heat Map in the draw_heat_map function
def draw_heat_map():
    # 10. Clean the data in the df_heat variable
    df_heat = df.copy()
    df_heat = df_heat[
        (df_heat['ap_lo'] <= df_heat['ap_hi']) &
        (df_heat['height'] >= df_heat['height'].quantile(0.025)) &
        (df_heat['height'] <= df_heat['height'].quantile(0.975)) &
        (df_heat['weight'] >= df_heat['weight'].quantile(0.025)) &
        (df_heat['weight'] <= df_heat['weight'].quantile(0.975))
    ]
    
    # 11. Calculate the correlation matrix
    corr = df_heat.corr(numeric_only=True)
    
    # 12. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # 13. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 14. Plot the correlation matrix using seaborn
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', center=0, ax=ax, cbar_kws={'shrink': 0.8})
    
    return fig

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("Data_Analysis_with_Python\Medical_Data_Visualizer\medical_examination.csv")

# 2
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)
    #astype(int) makes that where everything is over 25 (true) it receives 1 as value, else 0

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)
    #astype(int) makes that where everything is over 1 (true) it receives 1 as value, else 0

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
        #NOTES
        #id_vars is to split dataset through category variables. More then one category variable can be used. Possible this would allow to create more graphs?
            # checked this but did not appear to work as expected.

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat = df_cat.rename(columns={0: 'total'})

    # 7
    catplot = sns.catplot(data=df_cat, kind="bar", x="variable", y="total", hue="value", col="cardio")

    # 8
    fig = catplot.fig

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=int))
        #NOTES
        # using np.tril will create a triangle in the opposite direction in final figure.
        # another example used 'bool' as dtype, but appears to not matter in this case. Not completely sure why. int still works fine

    # 14
    fig, ax = plt.subplots(figsize=(14, 9))

    # 15
    sns.heatmap(corr, mask=mask, square=True, annot=True, fmt="0.1f")

        #NOTES
        #adding 'f' in fmt="0.1f" will make the value fitted within square, no overflow.
        #higher decimal in fmt increases number of decimals in each box. 0.1 is one decimal, 0.2 is two decimals, etc.
        #annot=True will add value in each box.

    # 16
    fig.savefig('heatmap.png')
    return fig
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("Data_Analysis_with_Python\Page_View_Time_Series_Visualizer\download-fcc-forum-pageviews.csv",parse_dates=True)

df['datestamp'] = pd.to_datetime(df['date'])

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]

print(df.head())
print(df['date'].shape[0])
print(df.dtypes)

def draw_line_plot():

    df_line_plot = df.copy()

    fig = plt.figure(figsize=(16, 9))

    ax = plt.plot(df_line_plot['datestamp'], df_line_plot['value'])
    
    #setting label names and title
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar['year'] = df_bar['datestamp'].dt.year
    df_bar['month'] = df_bar['datestamp'].dt.month

    print(df_bar.head())
    # Draw bar plot


    plt.xlabel('Years')
    plt.ylabel('Average Page Views')


    # Save image and return fig (don't change this part)
    ###fig.savefig('bar_plot.png')
    ###return fig

draw_bar_plot()

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
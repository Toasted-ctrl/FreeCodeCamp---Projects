import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("Data_Analysis_with_Python\Page_View_Time_Series_Visualizer\download-fcc-forum-pageviews.csv",parse_dates=True)

df['date'] = pd.to_datetime(df['date'])

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]

print(df.head())

def draw_line_plot():

    df_line_plot = df.copy()

    fig = plt.figure(figsize=(16, 9))

    ax = plt.plot(df_line_plot['date'], df_line_plot['value'])
    
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

    df_bar['Years'] = df_bar['date'].dt.year
    df_bar['Months'] = df_bar['date'].dt.month_name()
    df_bar = pd.DataFrame(df_bar.groupby(['Years', 'Months'], sort=False)['value'].mean())

    # Draw bar plot

    fig, ax = plt.subplots(figsize=(14, 14))

    hue_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    chart = sns.barplot(data=df_bar, x='Years', y='value', hue='Months', palette='tab10', hue_order=hue_order)

    plt.ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, axes = plt.subplots(figsize=(18, 10), ncols=2)

    ax1 = sns.boxplot(data=df_box, x='year', y='value', ax=axes[0], hue='year', legend=False, palette='tab10')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')

    order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ax2 = sns.boxplot(data=df_box, x='month', y='value', ax=axes[1], order=order, hue='month', legend=False, palette='tab10')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_box_plot()
# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Define the function to perform the task
def draw_plot():
    # 1: Read data from the file
    df = pd.read_csv('epa-sea-level.csv')

    # 2: Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # 3: Perform linear regression on all data
    slope_all, intercept_all, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Generate x values for years from the start of the dataset to 2050
    years_extended = pd.Series(range(1880, 2051))

    # Calculate the corresponding y values (predicted sea levels) using the slope and intercept
    sea_levels_extended = intercept_all + slope_all * years_extended

    # Plot the first line of best fit
    plt.plot(years_extended, sea_levels_extended, 'r', label='Best Fit Line (1880-2050)', color='red')

    # 4: Perform linear regression using only data from the year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Generate x values from 2000 to 2050
    years_recent = pd.Series(range(2000, 2051))

    # Calculate the corresponding y values (predicted sea levels) using the slope and intercept from recent data
    sea_levels_recent = intercept_recent + slope_recent * years_recent

    # Plot the second line of best fit (2000 onwards)
    plt.plot(years_recent, sea_levels_recent, 'g', label='Best Fit Line (2000-2050)', color='green')

    # 5: Add labels, title, and legend
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return the image
    plt.savefig('sea_level_plot.png')
    return plt.gca()


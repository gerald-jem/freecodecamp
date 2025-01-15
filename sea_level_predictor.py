import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data", color="blue")

    # Line of best fit for all data
    slope_all, intercept_all, r_value_all, p_value_all, std_err_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = pd.Series(range(1880, 2051))
    line_all = slope_all * years_extended + intercept_all
    plt.plot(years_extended, line_all, label="Best Fit (All Data)", color="red")

    # Line of best fit for data from 2000
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = pd.Series(range(2000, 2051))
    line_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, line_recent, label="Best Fit (2000+)", color="green")

    # Add labels, title, and legend
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save and return the plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()

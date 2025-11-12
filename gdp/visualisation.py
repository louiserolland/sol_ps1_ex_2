import pandas as pd
import seaborn as sns
from matplotlib.axes import Axes


def plot_gdp(df: "pd.DataFrame") -> Axes:

    """
    Plot GDP by country over time.

    Parameters
    ----------
    df : pd.DataFrame
        Must contain columns: 'Year', 'GDP', 'Country Name'.

    Returnsg
    -------
    Axes
        The Matplotlib Axes with the line plot.
    """
    return sns.lineplot(data=df, x="Year", y="GDP", hue="Country Name")

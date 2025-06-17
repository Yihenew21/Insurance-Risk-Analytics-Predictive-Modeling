import os
import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Optional, Tuple

def calculate_metrics(df: pd.DataFrame) -> Dict:
    """Calculate claim frequency, severity, and margin."""
    claim_frequency = (df['TotalClaims'] > 0).mean()
    claim_severity = df[df['TotalClaims'] > 0]['TotalClaims'].mean()
    margin = df['TotalPremium'].sum() - df['TotalClaims'].sum()
    return {'claim_frequency': claim_frequency, 'claim_severity': claim_severity, 'margin': margin}

def segment_data(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Segment data by a given column with aggregated metrics."""
    return df.groupby(column).agg({
        'TotalClaims': ['mean', 'count', 'sum'],
        'TotalPremium': ['mean', 'sum']
    }).reset_index()

def test_hypothesis(df: pd.DataFrame, group_col: str, metric_col: str, is_categorical: bool = False, alpha: float = 0.05) -> Tuple[Dict, pd.DataFrame]:
    """Perform t-test, ANOVA, or chi-squared test based on data type and return results and modified DataFrame."""
    # If metric_col is a Series, create a temporary column and track it
    temp_col = None
    if isinstance(metric_col, pd.Series):
        temp_col = "temp_metric"
        df = df.copy()
        df[temp_col] = metric_col
        metric_col = temp_col
    
    if is_categorical:
        contingency = pd.crosstab(df[group_col], df['TotalClaims'] > 0)
        chi2, p, dof, expected = stats.chi2_contingency(contingency)
        return {'statistic': chi2, 'p_value': p, 'dof': dof}, df
    else:
        groups = [group[metric_col].dropna() for name, group in df.groupby(group_col, observed=True) if not group[metric_col].dropna().empty]
        if len(groups) == 2:
            t_stat, p_value = stats.ttest_ind(groups[0], groups[1])
            return {'statistic': t_stat, 'p_value': p_value}, df
        elif len(groups) > 2:
            anova = stats.f_oneway(*groups)
            tukey = pairwise_tukeyhsd(df[metric_col].dropna(), df[group_col].dropna())
            return {'anova_statistic': anova.statistic, 'p_value': anova.pvalue, 'tukey_results': tukey}, df
        return None, df

def visualize_results(df: pd.DataFrame, group_col: str, metric_col: str, title: str, plot_type: str = 'box'):
    """Visualize hypothesis test results with various plot types."""
    plt.figure(figsize=(12, 6))
    if plot_type == 'box':
        sns.boxplot(x=group_col, y=metric_col if isinstance(metric_col, str) else "temp_metric", data=df)
    elif plot_type == 'heatmap' and metric_col == 'TransactionMonth':
        pivot = df.pivot_table(values=metric_col if isinstance(metric_col, str) else "temp_metric", index=group_col, aggfunc='mean')
        sns.heatmap(pivot, annot=True, cmap='YlOrRd')
    plt.title(title)
    plt.xticks(rotation=45)
    os.makedirs('notebooks/plots', exist_ok=True)
    save_metric_col = "temp_metric" if isinstance(metric_col, pd.Series) else metric_col
    plt.savefig(f'notebooks/plots/{group_col}_vs_{save_metric_col}_{plot_type}.png')
    plt.close()
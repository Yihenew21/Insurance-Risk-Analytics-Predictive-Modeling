"""Visualization utilities for insurance data EDA."""

from typing import List, Optional
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def setup_plot_style():
    """Configure Seaborn and Matplotlib plot styles."""
    sns.set_style('whitegrid')
    plt.rcParams['figure.figsize'] = (10, 6)

def plot_numerical_distribution(df: pd.DataFrame, col: str, save_path: Optional[str] = None):
    """
    Plot histogram with KDE for a numerical column.

    Args:
        df (pd.DataFrame): Input dataset.
        col (str): Column name.
        save_path (str, optional): Path to save the plot.
    """
    plt.figure()
    sns.histplot(df[col].dropna(), kde=True)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
    plt.show()

def plot_categorical_distribution(df: pd.DataFrame, col: str, save_path: Optional[str] = None):
    """
    Plot bar chart for a categorical column.

    Args:
        df (pd.DataFrame): Input dataset.
        col (str): Column name.
        save_path (str, optional): Path to save the plot.
    """
    plt.figure()
    sns.countplot(y=col, data=df, order=df[col].value_counts().index)
    plt.title(f'Distribution of {col}')
    plt.xlabel('Count')
    plt.ylabel(col)
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
    plt.show()

def plot_loss_ratio_by_category(df: pd.DataFrame, category: str, save_path: Optional[str] = None):
    """
    Plot Loss Ratio by a categorical column.

    Args:
        df (pd.DataFrame): Input dataset with LossRatio column.
        category (str): Categorical column name.
        save_path (str, optional): Path to save the plot.
    """
    plt.figure()
    sns.barplot(x='LossRatio', y=category, data=df, errorbar='ci')
    plt.title(f'Loss Ratio by {category}')
    plt.xlabel('Loss Ratio (Claims/Premium)')
    plt.ylabel(category)
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
    plt.show()

def plot_temporal_trend(df: pd.DataFrame, date_col: str, save_path: Optional[str] = None):
    """
    Plot monthly claim frequency trend.

    Args:
        df (pd.DataFrame): Input dataset.
        date_col (str): Date column name.
        save_path (str, optional): Path to save the plot.
    """
    # Convert date column to datetime and handle NaT
    df = df.dropna(subset=[date_col])
    df['Month'] = pd.to_datetime(df[date_col]).dt.to_period('M').dt.to_timestamp()
    
    # Debug: Check data before grouping
    print("Data after datetime conversion:", df[[date_col, 'TotalClaims']].head())
    
    # Group by Month and count claims
    monthly_trends = df.groupby('Month').agg({'TotalClaims': 'count'}).reset_index()
    print("Monthly Trends:", monthly_trends)
    
    if monthly_trends.empty:
        print("Warning: No data available for plotting.")
        return
    
    monthly_trends.columns = ['Month', 'ClaimCount']

    plt.figure(figsize=(12, 6))
    plt.plot(monthly_trends['Month'], monthly_trends['ClaimCount'], label='Claim Frequency')
    plt.gcf().autofmt_xdate()  # Auto-format date labels
    plt.title('Monthly Claim Frequency')
    plt.xlabel('Month')
    plt.ylabel('Number of Claims')
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
    plt.show()

def plot_correlation_matrix(df: pd.DataFrame, cols: List[str], save_path: Optional[str] = None):
    """
    Plot correlation matrix heatmap.

    Args:
        df (pd.DataFrame): Input dataset.
        cols (List[str]): List of numerical columns.
        save_path (str, optional): Path to save the plot.
    """
    plt.figure(figsize=(8, 6))
    correlation_matrix = df[cols].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix of Numerical Features')
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
    plt.show()

def plot_creative_visualizations(df: pd.DataFrame, save_dir: str):
    """
    Generate three creative visualizations for EDA.

    Args:
        df (pd.DataFrame): Input dataset.
        save_dir (str): Directory to save plots.
    """
    os.makedirs(save_dir, exist_ok=True)

    # 1. Loss Ratio by Province and Gender (Stacked Bar Plot)
    plt.figure(figsize=(12, 8))
    sns.catplot(x='LossRatio', y='Province', hue='Gender', kind='bar', data=df, height=6, aspect=1.5)
    plt.title('Loss Ratio by Province and Gender', fontsize=14)
    plt.xlabel('Loss Ratio (Claims/Premium)', fontsize=12)
    plt.ylabel('Province', fontsize=12)
    plt.savefig(os.path.join(save_dir, 'loss_ratio_province_gender.png'))
    plt.show()

    # 2. Claim Severity by Vehicle Make (Violin Plot)
    top_makes = df['make'].value_counts().index[:10]  # Changed from 'Make' to 'make'
    plt.figure(figsize=(12, 6))
    sns.violinplot(x='make', y='TotalClaims', data=df[df['make'].isin(top_makes)], inner='quartile')  # Changed from 'Make' to 'make'
    plt.title('Claim Severity Distribution by Top Vehicle Makes', fontsize=14)
    plt.xlabel('Vehicle Make', fontsize=12)
    plt.ylabel('Total Claims (Rand)', fontsize=12)
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(save_dir, 'claim_severity_make_violin.png'))
    plt.show()

    # 3. Claim Frequency Heatmap
    df['Month'] = pd.to_datetime(df['TransactionMonth']).dt.month
    df['Year'] = pd.to_datetime(df['TransactionMonth']).dt.year
    claim_pivot = df.pivot_table(index='Month', columns='Year', values='TotalClaims', aggfunc='count')
    plt.figure(figsize=(10, 6))
    sns.heatmap(claim_pivot, annot=True, fmt='.0f', cmap='YlGnBu')
    plt.title('Claim Frequency by Month and Year', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Month', fontsize=12)
    plt.savefig(os.path.join(save_dir, 'claim_frequency_heatmap.png'))
    plt.show()
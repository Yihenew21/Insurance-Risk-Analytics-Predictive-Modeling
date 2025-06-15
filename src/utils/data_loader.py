"""Utilities for loading and preprocessing data."""

import os
from typing import Optional
import pandas as pd
from dotenv import load_dotenv

def load_insurance_data(data_path: Optional[str] = None) -> pd.DataFrame:
    """
    Load insurance dataset from a text file with pipe (|) delimiter.

    Args:
        data_path (str, optional): Path to the text file. If None, uses DATA_PATH from .env.

    Returns:
        pd.DataFrame: Loaded dataset with date columns parsed.

    Raises:
        FileNotFoundError: If the data file is not found.
        ValueError: If the dataset is empty or has invalid format.
    """
    load_dotenv()
    data_path = data_path or os.getenv('DATA_PATH', 'data/raw/insurance_data.txt')
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file not found at {data_path}")
    
    df = pd.read_csv(data_path, sep='|', parse_dates=['TransactionMonth'])
    
    if df.empty:
        raise ValueError("Loaded dataset is empty")
    
    numerical_cols = ['TotalPremium', 'TotalClaims', 'SumInsured', 'CustomValueEstimate', 'CalculatedPremiumPerTerm']
    for col in numerical_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df
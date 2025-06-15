"""Unit tests for eda module."""

import pytest
import pandas as pd
import numpy as np
from src.core.eda import InsuranceEDA

@pytest.fixture
def sample_df():
    """Create a sample DataFrame for testing."""
    return pd.DataFrame({
        'TotalPremium': [100, 200, 300, np.nan],
        'TotalClaims': [50, 0, 150, 100],
        'Province': ['A', 'B', 'A', 'B'],
        'TransactionMonth': pd.to_datetime(['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01'])
    })

def test_get_descriptive_stats(sample_df):
    """Test descriptive statistics calculation."""
    eda = InsuranceEDA(sample_df)
    stats = eda.get_descriptive_stats()
    assert 'TotalPremium' in stats.columns
    assert stats.loc['count', 'TotalPremium'] == 3

def test_calculate_loss_ratio(sample_df):
    """Test Loss Ratio calculation."""
    eda = InsuranceEDA(sample_df)
    df = eda.calculate_loss_ratio()
    assert 'LossRatio' in df.columns
    assert df['LossRatio'].iloc[0] == 0.5  # 50/100
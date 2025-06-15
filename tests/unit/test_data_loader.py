"""Unit tests for data_loader module."""

import pytest
import pandas as pd
from src.utils.data_loader import load_insurance_data

def test_load_insurance_data_missing_file():
    """Test loading a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        load_insurance_data("non_existent.csv")

def test_load_insurance_data_empty_file(tmp_path):
    """Test loading an empty file raises ValueError."""
    empty_file = tmp_path / "empty.csv"
    empty_file.write("")
    with pytest.raises(ValueError):
        load_insurance_data(str(empty_file))
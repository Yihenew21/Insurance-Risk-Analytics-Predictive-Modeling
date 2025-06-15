import pandas as pd
import numpy as np

class InsuranceEDA:
    def __init__(self, df):
        self.df = df
        self.numerical_cols = ['PolicyID', 'PostalCode', 'RegistrationYear', 'Cylinders', 'cubiccapacity', 'kilowatts', 'NumberOfDoors', 'CustomValueEstimate', 'NumberOfVehiclesInFleet', 'SumInsured', 'CalculatedPremiumPerTerm', 'TotalPremium', 'TotalClaims']
        self.categorical_cols = ['IsVATRegistered', 'Citizenship', 'LegalType', 'Title', 'Language', 'Bank', 'AccountType', 'MaritalStatus', 'Gender', 'Country', 'Province', 'MainCrestaZone', 'SubCrestaZone', 'ItemType', 'VehicleType', 'make', 'Model', 'bodytype', 'AlarmImmobiliser', 'TrackingDevice', 'NewVehicle', 'WrittenOff', 'Rebuilt', 'Converted', 'CrossBorder', 'TermFrequency', 'ExcessSelected', 'CoverCategory', 'CoverType', 'CoverGroup', 'Section', 'Product', 'StatutoryClass', 'StatutoryRiskType']

    def get_descriptive_stats(self) -> pd.DataFrame:
        """
        Calculate descriptive statistics for numerical columns.
        Returns:
            pd.DataFrame: Descriptive statistics.
        """
        available_cols = [col for col in self.numerical_cols if col in self.df.columns]
        return self.df[available_cols].describe()

    def check_missing_values(self) -> pd.Series:
        """
        Check for missing values in the DataFrame.
        Returns:
            pd.Series: Count of missing values per column.
        """
        return self.df.isnull().sum()

    def detect_outliers(self, column: str, method: str = 'iqr', threshold: float = 1.5) -> pd.Series:
        """
        Detect outliers in a specified column using IQR or Z-score method.
        Args:
            column (str): Column name to check for outliers.
            method (str): Method to use ('iqr' or 'zscore').
            threshold (float): Threshold for outlier detection.
        Returns:
            pd.Series: Boolean series indicating outliers.
        """
        if method.lower() == 'iqr':
            Q1 = self.df[column].quantile(0.25)
            Q3 = self.df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - threshold * IQR
            upper_bound = Q3 + threshold * IQR
            return (self.df[column] < lower_bound) | (self.df[column] > upper_bound)
        elif method.lower() == 'zscore':
            z_scores = np.abs((self.df[column] - self.df[column].mean()) / self.df[column].std())
            return z_scores > threshold
        else:
            raise ValueError("Method must be 'iqr' or 'zscore'")
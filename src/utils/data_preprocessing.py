import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

class DataPreprocessor:
    def __init__(self):
        # Define categorical columns (adjust based on your dataset)
        self.categorical_cols = ['Region', 'VehicleType', 'CoverageType', 'PolicyType']  # Example columns
        self.max_cardinality = 50  # Maximum unique values to one-hot encode

    def handle_missing_data(self, df):
        """Impute missing values with median for numerical and mode for categorical, with fallback."""
        for col in df.columns:
            if df[col].dtype in ['int64', 'float64']:
                # Use median for numerical, fallback to 0 if all NaN
                df[col] = df[col].fillna(df[col].median())
            else:
                # Use mode for categorical, fallback to 'Unknown' if no mode
                mode_value = df[col].mode()[0] if not df[col].mode().empty else 'Unknown'
                df[col] = df[col].fillna(mode_value)
        return df

    def feature_engineering(self, df):
        """Create new features like PolicyAge and PremiumToClaimsRatio."""
        df['PolicyAge'] = pd.to_datetime('2025-06-17') - pd.to_datetime(df['RegistrationYear'], errors='coerce')
        df['PolicyAge'] = df['PolicyAge'].dt.days // 365  # Approximate years
        df['PremiumToClaimsRatio'] = df['TotalPremium'] / (df['TotalClaims'] + 1)  # Avoid division by zero
        return df

    def encode_categorical(self, df, sparse=True):
        """Apply one-hot encoding to categorical variables with cardinality check."""
        encoded_df = df.copy()
        high_cardinality_cols = []

        # Identify high-cardinality columns
        for col in self.categorical_cols:
            if col in df.columns:
                unique_values = df[col].nunique()
                if unique_values > self.max_cardinality:
                    high_cardinality_cols.append(col)
                    print(f"Warning: {col} has {unique_values} unique values, exceeding max_cardinality {self.max_cardinality}. Using LabelEncoder instead.")
                    le = LabelEncoder()
                    encoded_df[col] = le.fit_transform(df[col].astype(str))
                else:
                    # One-hot encode low-cardinality columns
                    dummies = pd.get_dummies(df[col], prefix=col, drop_first=True, sparse=sparse)
                    encoded_df = pd.concat([encoded_df.drop(columns=[col]), dummies], axis=1)

        if high_cardinality_cols:
            print(f"High cardinality columns handled: {high_cardinality_cols}")

        return encoded_df

    def preprocess(self, df):
        """Full preprocessing pipeline."""
        df = self.handle_missing_data(df)
        df = self.feature_engineering(df)
        df = self.encode_categorical(df)
        return df
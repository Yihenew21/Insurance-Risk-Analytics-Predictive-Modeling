import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from xgboost import XGBRegressor, XGBClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

class ModelEvaluator:
    """Class to evaluate and train machine learning models for severity and probability prediction."""

    def __init__(self):
        """Initialize with model dictionaries for severity and probability."""
        self.severity_models = {
            'LinearRegression': LinearRegression(),
            'DecisionTree': DecisionTreeRegressor(random_state=42),
            'RandomForest': RandomForestRegressor(random_state=42),
            'XGBoost': XGBRegressor(random_state=42)
        }
        self.probability_models = {
            'LogisticRegression': LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42),
            'DecisionTree': DecisionTreeClassifier(max_depth=5, random_state=42),
            'RandomForest': RandomForestClassifier(n_estimators=50, max_depth=5, random_state=42),
            'XGBoost': XGBClassifier(n_estimators=50, max_depth=3, random_state=42)
        }

    def train_evaluate_severity(self, X_train, X_test, y_train, y_test, model_name):
        """Train and evaluate a severity model."""
        model = self.severity_models[model_name]
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)
        return rmse, r2, model

    def train_evaluate_probability(self, X_train, X_test, y_train, y_test, model_name):
        """Train and evaluate a probability model."""
        model = self.probability_models[model_name]
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        return accuracy, precision, recall, f1, model
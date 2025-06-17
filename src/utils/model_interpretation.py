import pandas as pd
import shap
import numpy as np

def shap_analysis(model, X_train, X_test):
      """Perform SHAP analysis to identify top features."""
      explainer = shap.Explainer(model, X_train)
      shap_values = explainer(X_test)
      shap_summary = shap.summary_plot(shap_values, X_test, plot_type="bar")
      return shap_values, shap_summary

def get_top_features(shap_values, feature_names, top_n=10):
      """Extract top N features based on mean absolute SHAP value."""
      vals = np.abs(shap_values.values).mean(0)
      feature_importance = pd.DataFrame(list(zip(feature_names, vals)), columns=['feature_name', 'mean_shap_value'])
      return feature_importance.sort_values('mean_shap_value', ascending=False).head(top_n)
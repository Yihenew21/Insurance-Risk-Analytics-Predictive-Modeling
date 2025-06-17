# Task 4 Analysis Report
## Model Performance
|    | Model              | Metric                    |
|---:|:-------------------|:--------------------------|
|  0 | LinearRegression   | RMSE: 59376.12, R²: -1.19 |
|  1 | DecisionTree       | RMSE: 11244.75, R²: 0.92  |
|  2 | RandomForest       | RMSE: 8877.22, R²: 0.95   |
|  3 | XGBoost            | RMSE: 7753.10, R²: 0.96   |
|  4 | LogisticRegression | Acc: 1.00, F1: 0.79       |
|  5 | DecisionTree       | Acc: 1.00, F1: 0.95       |
|  6 | RandomForest       | Acc: 1.00, F1: 0.92       |
|  7 | XGBoost            | Acc: 1.00, F1: 0.97       |
## Top Features
|      | feature_name                                                          |   mean_shap_value |
|-----:|:----------------------------------------------------------------------|------------------:|
|   15 | PremiumToClaimsRatio                                                  |         14668.8   |
|   12 | CalculatedPremiumPerTerm                                              |         11741     |
|   13 | TotalPremium                                                          |          9902.3   |
|   11 | SumInsured                                                            |          3959.5   |
| 2515 | CoverType_Windscreen                                                  |           456.202 |
|    6 | cubiccapacity                                                         |           289.036 |
| 2483 | ExcessSelected_Mobility - Taxi with value less than R100 000 - R3 000 |           231.446 |
| 1154 | UnderwrittenCoverID_110755                                            |           152.49  |
|    0 | PolicyID                                                              |           145.35  |
| 2154 | Bank_Nedbank                                                          |           138.571 |
## Recommendations
- Adjust premiums based on top features (e.g., PolicyAge).

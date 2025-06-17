# B5W3: End-to-End Insurance Risk Analytics & Predictive Modeling

This repository contains the code and documentation for the B5W3 challenge, focused on analyzing historical insurance claim data for AlphaCare Insurance Solutions (ACIS) to optimize marketing strategies and identify low-risk segments for premium adjustments.

## 📁 Project Structure

```
├── .github/                # GitHub Actions workflows
├── .vscode/                # VSCode settings
├── config/                 # Configuration files
├── data/                   # Raw and processed data (DVC-tracked)
├── docs/                   # Documentation
├── examples/               # Example scripts or outputs
├── notebooks/              # Jupyter notebooks for EDA and analysis
│   ├── task1_eda.ipynb     # Exploratory Data Analysis
│   ├── task4_predictive_modeling.ipynb  # Regression & classification models
│   └── eda/plots           # Visualizations: frequency, severity, loss ratio
├── scripts/                # Utility scripts (e.g., preprocessing)
├── src/                    # Source code modules
│   ├── core/
│       ├── eda.py          #
│   └── utils/
│       ├── data_loader.py
│       ├── data_preprocessing.py
│       ├── modeling_utils.py
│       └── model_interpretation.py
│       ├── visualization.py
│   └── stats/
│       ├── hypothesis_testing.py
├── tests/                  # Unit and integration tests
│   └── unit/
│       ├── test_data_loader.py
│       ├── test_eda.py
├── reports/                # Markdown or HTML reports
│   └── task3_analysis.md   # Comprehensive Hypothesis Testing Analysis summary
│   └── task4_analysis.md   # Final model evaluation summary
├── .env.example            # Sample environment variables
├── .gitignore              # Git ignore rules
├── dvc.yaml                # DVC pipeline file (if pipeline is added)
├── dvc.lock                # DVC pipeline lock file
├── requirements.txt        # Python dependencies
├── Makefile                # Automation tasks
├── pyproject.toml          # Project metadata and settings
└── README.md               # Project overview
```

## ⚙️ Setup Instructions

1. **Clone the Repository**:

```bash
git clone https://github.com/Yihenew21/Insurance-Risk-Analytics-Predictive-Modeling.git
cd Insurance-Risk-Analytics-Predictive-Modeling
```

2. **Set Up Python 3.13 Virtual Environment**:

```bash
python3.13 -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. **Configure Environment Variables**:

```bash
cp .env.example .env
```

4. **Run Jupyter Notebook for EDA or Modeling**:

```bash
jupyter notebook
```

## 📦 Data Version Control (DVC)

This project uses [DVC](https://dvc.org/) to track data and manage experiments.

### ✅ What’s included:

- Raw and processed data tracked with DVC
- Local remote storage configured for fast local caching
- Google Drive remote set up for cloud backup and team collaboration
- Data pushed to both remotes using `dvc push`

### 🔧 Common DVC Commands

- Track a file:

  ```bash
  dvc add data/raw/insurance_data.txt
  ```

- Push data to remote:

  ```bash
  dvc push
  ```

- Reproduce pipeline:

  ```bash
  dvc repro
  ```

### 📁 DVC Remotes

- **Local Remote**: for quick local access
- **Google Drive Remote**: for cloud backup and collaboration  
  _(Folder ID is stored in DVC config)_

## 📊 Tasks Overview

### ✅ Task 1: Git & EDA

- Initialized Git repository and structured project layout
- Created modular EDA workflow with reusable functions in `src/utils/`
- Generated plots for claim frequency, severity, loss ratio, and correlation

### ✅ Task 2: Data Version Control (DVC)

- Initialized DVC and tracked `insurance_data.txt`
- Configured `.gitignore` to allow `.dvc` files
- Set up local and Google Drive remotes for data storage
- Prepared for pipeline creation using `dvc run`

### 🧪 Task 3: A/B Hypothesis Testing (Upcoming)

- Planned for statistical testing to evaluate premium strategy differences

### ✅ Task 4: Predictive Modeling

- Built regression models (Linear, Decision Tree, Random Forest, XGBoost) to predict **claim severity**
- Built classification models (Logistic Regression, Decision Tree, Random Forest, XGBoost) to flag **high-risk policyholders**
- Used SHAP for feature importance analysis
- Exported plots: `probability_comparison.png`, `severity_comparison.png`
- Summary report: `task4_analysis.md`
- Top features: `PremiumToClaimsRatio`, `TotalPremium`, `CalculatedPremiumPerTerm`, etc.
- Recommendation: Adjust premiums based on top predictive features

## 📄 License

MIT License

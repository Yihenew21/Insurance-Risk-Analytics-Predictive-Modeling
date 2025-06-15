# B5W3: End-to-End Insurance Risk Analytics & Predictive Modeling

This repository contains the code and documentation for the B5W3 challenge, focused on analyzing historical insurance claim data for AlphaCare Insurance Solutions (ACIS) to optimize marketing strategies and identify low-risk segments for premium adjustments.

# B5W3: End-to-End Insurance Risk Analytics & Predictive Modeling

This repository contains the code and documentation for the B5W3 challenge, focused on analyzing historical insurance claim data for AlphaCare Insurance Solutions (ACIS) to optimize marketing strategies and identify low-risk segments for premium adjustments.

## Project Structure

├── .github/ # GitHub Actions workflows
├── .vscode/ # VSCode settings
├── config/ # Configuration files
├── data/ # Raw and processed data (managed by DVC)
├── docs/ # Documentation
├── examples/ # Example scripts or outputs
├── notebooks/ # Jupyter notebooks for EDA and analysis
│ └── tak1_eda.ipynb/ # Exploratory Data Analysis notebooks and plots
│ └── eda/plots # Generated plots for claim frequency, severity, loss ratio, and correlation matrix
├── scripts/ # Utility scripts
├── src/ # Source code (core, models, utils, services)
│ └── core/ # core modules
│ ├── visualization.py # Module with functions for temporal trends, categorical distributions, and creative plots
│ └── utils/ # Utility modules
│ ├── eda.py # Module with functions for exploratory data analysis and statistical computations
│ └── data_loader.py # Module with functions for loading and preprocessing insurance datasets
├── tests/ # Unit and integration tests
├── .env.example # Example environment variables
├── .gitignore # Git ignore rules
├── Makefile # Automation tasks
├── pyproject.toml # Project metadata and dependencies
├── README.md # Project overview
├── requirements.txt # Python dependencies

## Setup Instructions

1. **Clone the Repository**:

````bash
git clone https://github.com/Yihenew21/Insurance-Risk-Analytics-Predictive-Modeling.git
cd Insurance-Risk-Analytics-Predictive-Modeling


2. **Set Up Python 3.13 Virtual Environment**:

```bash
   python3.13 -m venv .venv
   source .venv/bin/activate # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
```

3. **Configure Environment Variables**:

```bash
  cp .env .env
```

4. **Run Jupyter Notebook for EDA**:

```bash
jupyter notebook
```

## Tasks

Task 1: Git setup, project planning, and Exploratory Data Analysis (EDA)
Completed initial Git setup and project structure.
Developed EDA notebook with data loading, preprocessing, visualization integration, and a comprehensive report including summary, recommendations, and findings.
Created modular components in src/utils/ for data handling, analysis, and visualization.
Generated plots stored in notebooks/eda/plots/ to visualize claim frequency, severity, loss ratio, and numerical feature correlations.
Task 2: Data Version Control (DVC) setup
Task 3: A/B hypothesis testing
Task 4: Predictive modeling for claim severity and premium optimization

## License

MIT License
````

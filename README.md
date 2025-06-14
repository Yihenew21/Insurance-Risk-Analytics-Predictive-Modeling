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
├── scripts/ # Utility scripts
├── src/ # Source code (core, models, utils, services)
├── tests/ # Unit and integration tests
├── .env.example # Example environment variables
├── .gitignore # Git ignore rules
├── Makefile # Automation tasks
├── pyproject.toml # Project metadata and dependencies
├── README.md # Project overview
├── requirements.txt # Python dependencies

## Setup Instructions

1. **Clone the Repository**:

```bash
   git clone https://github.com/your-username/b5w3-insurance-analytics.git
   cd b5w3-insurance-analytics
```

2. **Set Up Python 3.13 Virtual Environment**:

```bash
   python3.13 -m venv .venv
   source .venv/bin/activate # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
```

3. **Configure Environment Variables**:

```bash
  cp .env.example .env
```

4. **Run Jupyter Notebook for EDA**:

```bash
jupyter notebook
```

## Tasks

Task 1: Git setup, project planning, and Exploratory Data Analysis (EDA).
Task 2: Data Version Control (DVC) setup.
Task 3: A/B hypothesis testing.
Task 4: Predictive modeling for claim severity and premium optimization.

## License

MIT License

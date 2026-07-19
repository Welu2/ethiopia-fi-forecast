# Ethiopia Financial Inclusion Forecasting

## Project Overview

This project analyzes Ethiopia's financial inclusion ecosystem by integrating survey observations, policy events, infrastructure indicators, and impact relationships to support forecasting and impact modeling.

The project is divided into multiple tasks, beginning with data enrichment and exploratory analysis.

---

# Project Structure

```
ethiopia-fi-forecast/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── task1_data_exploration.ipynb
│   └── task2_eda.ipynb
├── src/
│   ├── data_loader.py
│   ├── explorer.py
│   ├── enrich.py
│   └── eda.py
├── tests/
├── dashboard/
├── models/
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
cd ethiopia-fi-forecast
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Task 1 — Data Exploration and Enrichment

## Objective

Understand the provided financial inclusion dataset, explore its structure, and enrich it with additional observations, events, and impact relationships collected from official sources.

---

## Work Completed

### Dataset Exploration

- Loaded the unified financial inclusion dataset
- Loaded reference codes
- Explored dataset schema
- Reviewed record types
- Examined pillars
- Identified source types
- Analyzed confidence levels
- Explored temporal coverage
- Reviewed indicators
- Reviewed existing events
- Explored impact relationships

---

### Dataset Enrichment

Added new records including

- Financial inclusion observations
- Digital finance events
- Infrastructure indicators
- Impact relationships

Each added record contains

- Source URL
- Original source text
- Confidence level
- Collector information
- Collection date
- Supporting notes

---

### Utilities Developed

- Data loading utilities
- Dataset exploration functions
- Dataset enrichment pipeline

---

### Deliverables

```
src/data_loader.py
src/explorer.py
src/enrich.py

notebooks/task1_data_exploration.ipynb

reports/data_enrichment_log.md

data/raw/ethiopia_fi_unified_data_enriched.csv
```

---

# Task 2 — Exploratory Data Analysis

## Objective

Perform exploratory data analysis to understand patterns, trends, and potential drivers of financial inclusion in Ethiopia.

---

## Analyses Performed

### Dataset Overview

- Record type distribution
- Pillar distribution
- Source type distribution
- Confidence distribution

---

### Temporal Analysis

- Temporal coverage visualization
- Indicator availability by year

---

### Data Quality Assessment

- Missing values
- Duplicate records
- Confidence assessment
- Coverage gaps

---

### Access Analysis

- Account ownership trend
- Growth rate analysis
- Gender comparison
- Urban vs Rural comparison

---

### Usage Analysis

- Mobile money adoption
- Digital payment indicators

---

### Infrastructure Analysis

Explored relationships between

- Mobile subscriptions
- Internet access
- Infrastructure indicators
- Financial inclusion outcomes

---

### Event Analysis

Created an event timeline including major milestones such as

- Digital Ethiopia 2025
- Telebirr launch
- Safaricom Ethiopia market entry
- M-PESA launch

---

### Correlation Analysis

Examined relationships between

- Access indicators
- Usage indicators
- Infrastructure variables

---

### Key Findings

The exploratory analysis indicates that

- Financial inclusion has improved over time.
- Mobile money adoption expanded rapidly following major digital finance initiatives.
- Infrastructure development appears positively associated with financial inclusion.
- Several indicators have limited historical observations.
- Major policy and market events align with changes in financial inclusion trends.

---

## Deliverables

```
src/eda.py

notebooks/task2_eda.ipynb

reports/task2_summary.md

reports/data_quality_assessment.md

reports/figures/
```

---

# Running the Project

Launch Jupyter

```bash
jupyter notebook
```

or

```bash
jupyter lab
```

Run

```
notebooks/task1_data_exploration.ipynb
```

followed by

```
notebooks/task2_eda.ipynb
```

---

# Running Tests

```bash
pytest
```

---

# Technologies Used

- Python
- Pandas
- Matplotlib
- NumPy
- Jupyter Notebook
- Pytest

---

# Repository Workflow

Task development follows a feature-branch workflow.

```
main
│
├── task-1
│     Data Exploration & Enrichment
│
├── task-2
│     Exploratory Data Analysis
│
└── future tasks
```

Each task is developed in its own branch, reviewed through a Pull Request, and merged into `main`.

---

# Future Work

The next phases of the project will focus on

- Feature engineering
- Forecasting models
- Impact modeling
- Dashboard development
- Financial inclusion prediction
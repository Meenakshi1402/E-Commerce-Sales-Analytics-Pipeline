# E‑Commerce Sales Analytics Pipeline

A self‑contained data pipeline that ingests raw e‑commerce sales data, stores it in SQLite, transforms it with Python (Pandas & NumPy), and generates analytical reports and visualizations. Ideal for demonstrating end‑to‑end ETL, analysis, and reproducible workflows.

## Features

- Relational Schema: Defines `products` and `sales` tables in `sales.db` via `schema.sql`.
- ETL Pipeline: Uses `run_schema.py` to initialize the database and `load_data.py` to ingest CSV exports into the database with Pandas and SQLAlchemy.
- **Analysis Module**: Executes `analysis.py` to join tables, calculate monthly revenue, category summaries, and detect anomalies, exporting results as CSV reports.
- **Interactive Visualization**: Jupyter Notebook for plotting time‑series revenue and category breakdowns with Matplotlib.
- **Reproducibility**: Isolated Python virtual environment (`venv`), version control (`.gitignore`), and clear setup steps.

## Prerequisites

- Python 3.7 or higher
- Git (for version control)

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/ecommerce-analytics-pipeline.git
   cd ecommerce-analytics-pipeline
   ```
2. **Create and activate a Python virtual environment**
   ```bash
   python -m venv venv            # Create env
   source venv/bin/activate       # macOS/Linux
   venv\Scripts\activate        # Windows PowerShell
   ```
3. **Install dependencies**
   ```bash
   pip install pandas numpy sqlalchemy matplotlib jupyter
   ```

## Database Initialization

1. **Review the schema** in `schema.sql` which creates the `products` and `sales` tables.
2. **Run**:
   ```bash
   python run_schema.py
   ```
   This creates `sales.db` and sets up the tables.

## ETL: Loading Data

1. **Place your data files** in the project root:
   - `products.csv` (columns: `product_id,name,category,unit_price`)
   - `sales_raw.csv` (columns: `sale_date,product_id,quantity,unit_price`)
2. **Execute**:
   ```bash
   python load_data.py
   ```
   This ingests your CSVs into the SQLite database and computes `total_amount`.

## Analysis & Reporting

Run the analysis script:
```bash
python analysis.py
```
- Outputs CSVs in the `reports/` folder:
  - `monthly_revenue.csv`
  - `category_summary.csv`
  - `daily_anomalies.csv`

## Visualization

1. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```
2. **Open** the provided notebook, then **run** cells to view:
   - Monthly revenue line chart
   - Category breakdown bar chart

## Folder Structure

```
├── schema.sql           # SQL schema for tables
├── run_schema.py        # Initializes SQLite database
├── products.csv         # Product catalog data
├── sales_raw.csv        # Raw sales transactions
├── load_data.py         # ETL script to load CSVs into DB
├── analysis.py          # Data analysis and reporting
├── reports/             # Output CSV reports
├── notebook.ipynb       # Visualization notebook
├── venv/                # Python virtual environment
└── .gitignore           # Ignore venv, DB, and cache files
```

## Contributing & License

Contributions welcome—please open an issue or pull request. This project is released under the MIT License. Feel free to clone, modify, and share!


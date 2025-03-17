# Optimized Field Visits and Preventive Maintenance Scheduling

## Overview

This project demonstrates the use of **Time Series Forecasting** and **Mixed-Integer Linear Programming (MILP)** to optimize field visits and plan preventive maintenance. The notebook forecasts critical KPIs such as **Drop Call Rate** and **Call Setup Success Rate** using **Prophet**. Based on the forecasted values, the **MILP model** optimizes the allocation of resources to visit sites requiring maintenance.

## Key Features

- **KPI Forecasting**: Forecasts KPIs using Prophet for the next 5 days.
- **Maintenance Identification**: Identifies sites that require preventive maintenance based on forecasted KPIs.
- **Field Visit Optimization**: Uses MILP to optimize field visits with limited resources.

## How It Works

1. **Forecast KPIs**: The `forecast_kpi.py` script uses **Prophet** to predict future values for KPIs like **Drop Call Rate**.
2. **Identify Maintenance Needs**: The forecasted values are used to identify sites that require preventive maintenance.
3. **Optimize Field Visits**: The `milp_optimization.py` script uses **MILP** to plan optimized field visits based on available resources.

## Requirements

- Python 3.x
- Libraries:
  - `prophet`
  - `pandas`
  - `scipy`
  - `matplotlib`

You can install the required libraries using:

```bash
pip install -r requirements.txt
```

## Running the Code
1. Clone the repository:
```bash
git clone https://github.com/your-username/optimized-field-visits.git
```

2. Navigate to the project directory:
```bash
cd optimized-field-visits
```
3. Run the notebook to execute the forecasting and optimization:
```bash
jupyter notebook optimized_field_visits.ipynb
```

## License
This project is licensed under the MIT License. See the LICENSE[https://opensource.org/license/mit] file for more information.

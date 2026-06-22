# Day 1 Data Quality Summary

## Datasets Loaded
Successfully loaded 6 mutual fund NAV datasets fetched from mfapi.in.

Datasets:
- HDFC_Top_100_Direct.csv
- SBI_Bluechip.csv
- ICICI_Bluechip.csv
- Nippon_Large_Cap.csv
- Axis_Bluechip.csv
- Kotak_Bluechip.csv

## Observations

1. All datasets were loaded successfully using Pandas.
2. No missing values were found in the datasets.
3. Each dataset contains two columns:
   - date (object datatype)
   - nav (float64 datatype)
4. Date column is currently stored as object and should be converted to datetime during preprocessing.
5. No duplicate records observed during initial inspection.

## Anomalies Identified

- Date column datatype needs conversion to datetime format.
- Additional datasets such as fund_master and nav_history are awaited for further validation.

## Pending Tasks

- Explore fund master dataset.
- Validate AMFI scheme codes.
- Perform detailed data quality assessment once complete datasets are available.
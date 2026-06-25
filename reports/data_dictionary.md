# Data Dictionary

## 01_fund_master.csv

| Column | Type | Description |
|---------|------|-------------|
| amfi_code | Integer | Unique scheme identifier |
| scheme_name | Text | Name of mutual fund scheme |
| fund_house | Text | Mutual fund company |
| category | Text | Fund category |
| sub_category | Text | Fund sub-category |
| risk_grade | Text | Risk level |

## 02_nav_history.csv

| Column | Type | Description |
|---------|------|-------------|
| amfi_code | Integer | Scheme identifier |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

## 08_investor_transactions.csv

| Column | Type | Description |
|---------|------|-------------|
| investor_id | Text | Investor unique ID |
| transaction_date | Date | Date of transaction |
| amount_inr | Float | Investment amount |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| kyc_status | Text | Investor KYC status |
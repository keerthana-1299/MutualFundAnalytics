import pandas as pd
import os

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# ==========================================
# 1. CLEAN NAV HISTORY
# ==========================================

nav_df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", nav_df.shape)

# Convert date column to datetime
nav_df['date'] = pd.to_datetime(nav_df['date'])

# Sort by AMFI code and date
nav_df = nav_df.sort_values(by=['amfi_code', 'date'])

# Forward fill missing NAV values
nav_df['nav'] = nav_df.groupby('amfi_code')['nav'].ffill()

# Remove duplicates
nav_df = nav_df.drop_duplicates()

# Keep only valid NAV values
nav_df = nav_df[nav_df['nav'] > 0]

print("Cleaned Shape:", nav_df.shape)

# Save cleaned file
nav_df.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

print("nav_history cleaned successfully!\n")


# ==========================================
# 2. CLEAN INVESTOR TRANSACTIONS
# ==========================================

txn_df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Investor Transactions Original Shape:",
      txn_df.shape)

# Convert transaction date to datetime
txn_df['transaction_date'] = pd.to_datetime(
    txn_df['transaction_date']
)

# Standardize transaction types
txn_df['transaction_type'] = (
    txn_df['transaction_type']
    .str.strip()
    .str.upper()
)

# Keep only positive amounts
txn_df = txn_df[txn_df['amount_inr'] > 0]

# Remove duplicates
txn_df = txn_df.drop_duplicates()

# Standardize KYC status
txn_df['kyc_status'] = (
    txn_df['kyc_status']
    .str.strip()
    .str.upper()
)

valid_kyc = ['VERIFIED', 'PENDING', 'REJECTED']

invalid_kyc = txn_df[
    ~txn_df['kyc_status'].isin(valid_kyc)
]

print("Invalid KYC Records:",
      invalid_kyc.shape[0])

# Save cleaned file
txn_df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("investor_transactions cleaned successfully!\n")


# ==========================================
# 3. CLEAN SCHEME PERFORMANCE
# ==========================================

perf_df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("\nScheme Performance Original Shape:",
      perf_df.shape)

print("\nColumns in Scheme Performance:")
print(perf_df.columns)

# Convert all return columns to numeric
for col in perf_df.columns:
    if 'return' in col.lower():
        perf_df[col] = pd.to_numeric(
            perf_df[col],
            errors='coerce'
        )

# Check expense ratio anomalies
if 'expense_ratio' in perf_df.columns:

    anomalies = perf_df[
        (perf_df['expense_ratio'] < 0.1) |
        (perf_df['expense_ratio'] > 2.5)
    ]

    print("\nExpense Ratio Anomalies:",
          anomalies.shape[0])

# Remove duplicates
perf_df = perf_df.drop_duplicates()

# Save cleaned file
perf_df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("scheme_performance cleaned successfully!")
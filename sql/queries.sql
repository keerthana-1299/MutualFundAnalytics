-- 1. Top 5 funds by AUM

SELECT scheme_name, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV

SELECT AVG(nav)
FROM nav_history;

-- 3. Transactions by State

SELECT state, COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 4. Funds with Expense Ratio < 1%

SELECT scheme_name, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 5. Count transactions by type

SELECT transaction_type, COUNT(*)
FROM investor_transactions
GROUP BY transaction_type;

-- 6. Average return by fund house

SELECT fund_house,
AVG(return_1yr_pct)
FROM scheme_performance
GROUP BY fund_house;

-- 7. Top performing schemes

SELECT scheme_name, return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 8. KYC status distribution

SELECT kyc_status, COUNT(*)
FROM investor_transactions
GROUP BY kyc_status;

-- 9. Average investment amount

SELECT AVG(amount_inr)
FROM investor_transactions;

-- 10. Total investors

SELECT COUNT(DISTINCT investor_id)
FROM investor_transactions;
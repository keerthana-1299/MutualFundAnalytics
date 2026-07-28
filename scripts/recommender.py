import pandas as pd

# Load scheme performance dataset
performance = pd.read_csv("data/raw/07_scheme_performance.csv")

# Function to recommend funds
def recommend_funds(risk_appetite):
    """
    Recommend Top 3 Mutual Funds based on risk appetite.

    Parameters:
        risk_appetite (str): Low, Moderate, High, Very High

    Returns:
        DataFrame containing top 3 recommended funds.
    """

    risk_appetite = risk_appetite.title()

    # Filter by risk grade
    funds = performance[performance["risk_grade"] == risk_appetite].copy()

    if funds.empty:
        print(f"No funds found for Risk Grade: {risk_appetite}")
        return

    # Sort by Sharpe Ratio (higher is better)
    top3 = funds.sort_values(
        by="sharpe_ratio",
        ascending=False
    ).head(3)

    print("\n======================================")
    print(f"Top 3 Recommended Funds ({risk_appetite} Risk)")
    print("======================================")

    print(
        top3[
            [
                "scheme_name",
                "fund_house",
                "category",
                "return_3yr_pct",
                "sharpe_ratio",
                "risk_grade",
            ]
        ].to_string(index=False)
    )

    return top3


if __name__ == "__main__":

    print("\nMutual Fund Recommendation System\n")

    risk = input("Enter Risk Appetite (Low / Moderate / High / Very High): ")

    recommend_funds(risk)
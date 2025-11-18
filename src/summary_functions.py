import pandas as pd
from typing import Dict

# Default path to your dataset inside the repo
DATA_PATH = "data/financial_transactions.csv"


def load_transactions(path: str = DATA_PATH) -> pd.DataFrame:
    """
    Load the financial transactions dataset from CSV.
    """
    df = pd.read_csv(path)
    return df


def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and prepare the transactions DataFrame.
    - Convert date to datetime
    - Ensure amount is numeric
    - Drop rows with invalid date or amount
    """
    df = df.copy()

    # Convert date column
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Make sure amount is numeric
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    # Drop rows where critical fields are missing
    df = df.dropna(subset=["date", "amount"])

    # Normalize type values (e.g. 'Credit', 'credit ' → 'credit')
    df["type"] = df["type"].str.strip().str.lower()

    return df


def total_by_type(df: pd.DataFrame) -> Dict[str, float]:
    """
    Return total amounts grouped by transaction type (credit / debit).
    """
    return df.groupby("type")["amount"].sum().to_dict()


def total_by_customer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return total transaction amount per customer.
    """
    return (
        df.groupby("customer_id")["amount"]
        .sum()
        .reset_index(name="total_amount")
        .sort_values("total_amount", ascending=False)
    )


def monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return total transaction amount per month (YYYY-MM).
    """
    df = df.copy()
    df["year_month"] = df["date"].dt.to_period("M").astype(str)

    return (
        df.groupby("year_month")["amount"]
        .sum()
        .reset_index(name="total_amount")
        .sort_values("year_month")
    )


def overall_summary(df: pd.DataFrame) -> Dict[str, float]:
    """
    Compute simple overall summary metrics.
    """
    totals = total_by_type(df)
    total_credit = totals.get("credit", 0.0)
    total_debit = totals.get("debit", 0.0)
    net_flow = total_credit - total_debit

    return {
        "total_credit": float(total_credit),
        "total_debit": float(total_debit),
        "net_flow": float(net_flow),
    }


if __name__ == "__main__":
    # Simple manual test when running the file directly
    data = load_transactions()
    data = clean_transactions(data)

    print("=== Overall Summary ===")
    print(overall_summary(data))

    print("\n=== Totals by Type ===")
    print(total_by_type(data))

    print("\n=== Monthly Summary (first 5 rows) ===")
    print(monthly_summary(data).head())

import pandas as pd
from typing import Dict

# Path to your dataset inside the repo
DATA_PATH = "data/financial_transactions.csv"


def load_transactions(path: str = DATA_PATH) -> pd.DataFrame:
    """
    Load the financial transactions dataset from CSV.
    """
    df = pd.read_csv(path)
    return df


def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the dataset:
    - Convert date column to datetime
    - Convert amount column to numeric
    - Remove rows with missing required values
    - Normalize text formatting
    """
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    df = df.dropna(subset=["date", "amount"])

    df["type"] = df["type"].str.strip().str.lower()

    return df


def total_by_type(df: pd.DataFrame) -> Dict[str, float]:
    """
    Calculate the total credit and debit amounts.
    """
    return df.groupby("type")["amount"].sum().to_dict()


def total_by_customer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total transactions per customer.
    """
    return (
        df.groupby("customer_id")["amount"]
        .sum()
        .reset_index(name="total_amount")
        .sort_values("total_amount", ascending=False)
    )


def monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the total transaction amount per month.
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
    Compute overall summary metrics:
    - total credit
    - total debit
    - net transaction flow
    """
    totals = total_by_type(df)
    credit = totals.get("credit", 0.0)
    debit = totals.get("debit", 0.0)

    return {
        "total_credit": float(credit),
        "total_debit": float(debit),
        "net_flow": float(credit - debit),
    }


if __name__ == "__main__":
    # Manual test for demo purposes
    df = load_transactions()
    df = clean_transactions(df)

    print("=== Overall Summary ===")
    print(overall_summary(df))

    print("\n=== Totals by Type ===")
    print(total_by_type(df))

    print("\n=== Monthly Summary (first 5 rows) ===")
    print(monthly_summary(df).head())


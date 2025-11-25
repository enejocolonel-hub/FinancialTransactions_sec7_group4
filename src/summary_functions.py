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

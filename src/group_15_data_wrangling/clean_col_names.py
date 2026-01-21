"""
A module that cleans column names for the Adult Census Income dataset.

The goal is to standardize column name, make it meaningful and improve readability.
"""

import pandas as pd

def clean_col_name(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename columns for consistency and readability and return the new dataframe.

    - Replace '.' with '_'
    - Rename 'fnlwgt' to a more meaningful name

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe including the Adult Census Income dataset.

    Returns
    -------
    df : pd.DataFrame
        The dataframe with new, meaningful column names.

    Examples
    --------
    >>> clean_col_name(df)

    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Wrong Input: must be a dataframe.")
    
    if "fnlwgt" not in df.columns:
        raise ValueError("Expected column 'fnlwgt' not found in dataframe.")
    
    out = df.copy()
    out.columns = out.columns.str.replace(".", "_", regex=False)
    out = out.rename(columns={"fnlwgt": "final_weight"})
    return out
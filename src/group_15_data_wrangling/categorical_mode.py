"""
A module that performing cleaning and mode-based imputation for categorical data.
"""

import pandas as pd

def cat_mode_impute(data, columns=None, sign="?"):
    """
    Performs cleaning and mode-based imputation for categorical data.

    This function identifies missing values (e.g. "?"),
    and replaces them with the most frequent (mode) category observed
    in that column. The imputation is performed independently for each
    targeted column.
    If `columns` is None, the function automatically targets all columns
    in the DataFrame that contain at least one occurrence of `sign`.
    If multiple categories are tied for the mode, the imputed value is
    chosen deterministically as the lexicographically smallest category.

    Parameters
    ----------
    data : pd.DataFrame
        The raw input DataFrame (e.g., Adult Census Income data).
    columns : list of str, optional
        The specific columns to clean and impute. If None, all columns that contain the missing
        value indicator `sign` are targeted.
    sign : str, default "?"
        The specific string used in the dataset to denote missing values.

        
    Returns
    -------
    pd.DataFrame
        A cleaned DataFrame, where the signs have been replaced by the column mode.

    Raises
    ------
    TypeError
        If `data` is not a pandas DataFrame.
    ValueError
        If `sign` is not found in any of the targeted columns, or if a
        targeted column contains only missing values.
    KeyError
        If a column in `columns` is missing from the DataFrame.

    Examples
    --------
    >>> cat_mode_impute(adult_census_df)    
        
    """

    if not isinstance(data, pd.DataFrame):
        raise TypeError("`data` must be a pandas DataFrame.")

    if columns is not None:
        if not isinstance(columns, list) or not all(isinstance(c, str) for c in columns):
            raise TypeError("`columns` must be a list of strings or None.")
        missing = [c for c in columns if c not in data.columns]
        if missing:
            raise KeyError(f"Column(s) not found in DataFrame: {missing}")
        target_cols = columns
        if not any((data[c] == sign).any() for c in target_cols):
            raise ValueError("`sign` was not found in any of the targeted columns.")
    else:
        target_cols = [c for c in data.columns if (data[c] == sign).any()]

    if len(target_cols) == 0:
        raise ValueError("`sign` was not found in any of the targeted columns.")

    df= data.copy()

    for c in target_cols:
        mask = df[c] == sign
        observed = df.loc[~mask, c].dropna()
        if observed.empty:
            raise ValueError(f"Column '{c}' cannot be imputed because all values are missing.")
        counts = observed.astype(str).value_counts()
        max_count = counts.max()
        mode_value = sorted(counts[counts == max_count].index)[0]
        df.loc[mask, c] = mode_value
    return df
import pandas as pd

def cat_mode_impute(data, columns=None, sign="?"):
    """
    Performs cleaning and mode-based imputation for categorical data.

    This function identifies missing values (e.g. "?"),
    and replaces them with the most frequent (mode) category observed
    in that column. The imputation is performed independently for each
    targeted column.
    If multiple categories are tied for the mode, the imputed value is
    chosen deterministically as the lexicographically smallest category.

    Parameters
    ----------
    data : pd.DataFrame
        The raw input DataFrame (e.g., Adult Census Income data).
    columns : list of str, optional
        The specific columns to clean and impute. If a column is None, the function 
        targets all categorical columns.
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

    """


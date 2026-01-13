import pandas as pd

def cat_knn_impute(data, columns=None, sign="?", n_neighbors=5):
    """
    Performs cleaning and KNN-based imputation for categorical data.

    This function identifies missing values (e.g. "?"),
    and uses a K-Nearest Neighbors to predict and fill those missing values
    based on the most similar rows. 
    It specifically solves the limitation of scikit-learn's KNNImputer
    by handling categorical string data.

    Parameters
    ----------
    data : pd.DataFrame
        The raw input DataFrame (e.g., Adult Census Income data).
    columns : list of str
        The specific columns to clean and impute. If a column is None, the function 
        targets all categorical columns.
    sign : str, default "?"
        The specific string used in the dataset to denote missing values.
    n_neighbors : int, default 5
        The number of similar neighbors.

    Returns
    -------
    pd.DataFrame
        A cleaned DataFrame, where the signs have been replaced by likely categories.

    Raises
    ------
    TypeError
        If `data` is not a pandas DataFrame.
    ValueError
        If `n_neighbors` is less than 1 or if the `sign` is not found 
        in the specified columns.
    KeyError
        If a column in `columns` is missing from the DataFrame.

    """


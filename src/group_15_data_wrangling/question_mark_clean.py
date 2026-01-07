import pandas as pd

def clean_question(data, sign="?"):
    """
    Identifies and handles missing values in the dataset.

    This function targets an issue in the Adult Census Income dataset where 
    missing values are recorded as '?'.
    It transforms these question marks into standard Python NaN values to 
    enable compatibility with pandas methods.

    Parameters
    ----------
    data : pd.DataFrame
        The input DataFrame containing the Adult Census Income data.
    sign : str, default "?"
        The string character used in the dataset to represent missing values.

    Returns
    -------
    pd.DataFrame
        A copy of the DataFrame with the sign replaced by np.nan.

    Raises
    ------
    TypeError
        If `data` is not a pandas DataFrame.
    ValueError
        If `sign` is not a string or if the DataFrame is empty.
    """
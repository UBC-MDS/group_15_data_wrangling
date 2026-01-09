"""
A module that sets the data type for the Adult Census Income dataset.

The purpose of this is to increase memory and compute efficiency
"""

import pandas as pd

def set_dtype(df: pd.DataFrame) -> pd.DataFrame:
    """
    Update the data types for each columns to increase efficiency.

    Sets the follow dtypes:
    age             int8
    workclass       category
    fnlwgt          int32
    education       category
    education.num   int8
    marital.status  category
    occupation      category
    relationship    category
    race            category
    sex             category
    capital.gain    int32
    capital.loss    int32
    hours.per.week  int8
    native.country  category
    income          category

    Parameters
    ----------
    df : pd.Dataframe
        The adult census income dataset found here: 
        https://www.kaggle.com/datasets/uciml/adult-census-income

    Returns
    -------
    pd.Dataframe
        The adult census imcome dataframe with updated data types.

    Examples
    --------
    >>> set_dtype(adult_census_df)

    """

    return None

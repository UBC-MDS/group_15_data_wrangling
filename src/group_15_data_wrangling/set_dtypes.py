"""
A module that sets the data type for the Adult Census Income dataset.

The purpose of this is to increase memory and compute efficiency.
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

    Raises
    ------
    TypeError
        If `df` is not a pandas DataFrame.
    ValueError
        If columns do not match the columns of the adult census income dataset 
        from kaggle. See Parameters.   

    Examples
    --------
    >>> set_dtype(adult_census_df)

    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError(f"Expected input to be pandas DataFrame, got {type(df)}")
    
    expected_columns1 = {
        'occupation', 'capital.loss', 'race', 'age', 'education', 
        'native.country', 'marital.status', 'income', 'capital.gain', 
        'workclass', 'fnlwgt', 'relationship', 'sex', 'hours.per.week', 
        'education.num'
    }

    expected_columns2 = {'capital-gain', 'race', 'sex', 'education', 
     'age', 'fnlwgt', 'education-num', 'native-country', 
     'occupation', 'capital-loss', 'marital-status', 'relationship', 
     'income', 'workclass', 'hours-per-week'}

    actual_columns = set(df.columns)
    if not (actual_columns == expected_columns1 or actual_columns == expected_columns2):
        raise ValueError(f"Expected input DataFrame to have these columns: {expected_columns1}, got: {actual_columns}")

    df = df.astype({
        "age": "int8",
        "workclass": "category",
        "fnlwgt": "int32",
        "education": "category",
        "education.num": "int8",
        "marital.status": "category",
        "occupation": "category",
        "relationship": "category",
        "race": "category",
        "sex": "category",
        "capital.gain": "int32",
        "capital.loss": "int32",
        "hours.per.week": "int8",
        "native.country": "category",
        "income": "category",
    })

    return df

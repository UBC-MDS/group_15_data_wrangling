"""
A module that encodes the target income column

The goal is to convert the target variable into a binary numeric representation. Our target
varibale is currently categorical, so encoding this column into a binary representation 
(0's and 1's) will allow for our dataset to be used in machine learning models. 
"""
import pandas as pd

def encode_income_binary(df: pd.DataFrame, target_column: str = "income", output_column: str = "income_binary") -> pd.DataFrame:
    """
    Encode the income column of the Adult Census Income dataset into a binary target.

    This function creates a binary target column where:
        - '<=50K' is encoded as 0
        - '>50K' is encoded as 1
    
    Parameters
    ----------
    df : pd.Dataframe
        The adult census income dataset found here: 
        https://www.kaggle.com/datasets/uciml/adult-census-income
    target_column : str, default 'income'
        Name of the income column to encode.
    output_column : str, default 'income_binary'
        Name of the new binary target column to create.

    Returns
    -------
    pd.DataFrame
        A dataframe with an additional binary income column.

    Examples
    --------
    - encode_income_binary(adult_census_df)
    - encode_income_binary(adult_census_df, output_column= "income_encoded")
"""

return None
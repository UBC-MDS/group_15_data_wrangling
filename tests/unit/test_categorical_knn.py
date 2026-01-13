import pandas as pd
import pytest

from group_15_data_wrangling import categorical_mode

def test_cat_mode_impute_type_error():
    with pytest.raises(TypeError, match="pandas DataFrame"):
        cat_knn_impute(["not", "a", "df"])

def test_cat_mode_impute_value_error():
    df = pd.DataFrame({"a": ["x", "y", "z"]})
    with pytest.raises(ValueError, match="sign.*not found"):
        cat_mode_impute(df, columns=["a"], sign="?")

def test_cat_mode_impute_key_error():
    df = pd.DataFrame({"a": ["x", "?", "y"]})
    with pytest.raises(KeyError):
        cat_mode_impute(df, columns=["does_not_exist"])

import pandas as pd
import pytest

from group_15_data_wrangling import categorical_knn

def test_cat_knn_impute_type_error():
    with pytest.raises(TypeError, match="pandas DataFrame"):
        cat_knn_impute(["not", "a", "df"])

def test_cat_knn_impute_value_error():
    df = pd.DataFrame({"a": ["x", "?", "y"]})
    with pytest.raises(ValueError, match="n_neighbors"):
        cat_knn_impute(df, columns=["a"], n_neighbors=0)

def test_cat_knn_impute_key_error():
    df = pd.DataFrame({"a": ["x", "?", "y"]})
    with pytest.raises(KeyError):
        cat_knn_impute(df, columns=["does_not_exist"])

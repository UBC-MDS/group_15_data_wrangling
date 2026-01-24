from group_15_data_wrangling.encode_income import encode_income_binary
import pytest
import pandas as pd

@pytest.fixture
def adult_df():
    """Loading a small copy of our actual dataset for testing."""
    return pd.read_csv("tests/unit/data_sample.csv")

def test_encode_income_binary_correct_col_name(adult_df): 
    """Check that the function adds an 'income_binary' column to the output DataFrame."""
    result = encode_income_binary(adult_df)
    assert "income_binary" in result.columns

def test_encode_income_binary_correct_values(adult_df):
    """Verify that the encoded income values are binary (0 and 1)."""
    result= encode_income_binary(adult_df)
    vals=result["income_binary"].unique()
    assert set(vals) == {0, 1}

def test_encode_income_binary_raises_error_if_missing_income_column():
    """Ensure a ValueError is raised when the income column is missing."""
    wrong_df = pd.DataFrame({"other": ["<=50K", ">50K"]})
    with pytest.raises(ValueError):
        encode_income_binary(wrong_df)

def test_encode_income_binary_raises_error_if_wrong_input_type():
    """Ensure a TypeError is raised when the input is not a pandas DataFrame."""
    wrong_input= {"canucks_rule_lol": "unfourtunately not true sad face" }
    with pytest.raises(TypeError):
        encode_income_binary(wrong_input)

def test_encode_income_binary_correct_vals_in_income(adult_df): 
    """Making sure that the values in the income column are only <=50K and >50K"""
    df_test=adult_df
    vals=df_test["income"].unique()
    assert set(vals) =={"<=50K", ">50K"}



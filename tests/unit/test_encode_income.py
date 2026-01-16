from group_15_data_wrangling.encode_income import encode_income_binary
import pytest
import pandas as pd

@pytest.fixture
def adult_df():
    return pd.read_csv("tests/unit/data_sample.csv")

def test_encode_income_binary_correct_col_name(adult_df): 
    result = encode_income_binary(adult_df)
    assert "income_binary" in result.columns

def test_encode_income_binary_correct_values(adult_df):
    result= encode_income_binary(adult_df)
    vals=result["income_binary"].unique()
    assert set(vals) == {0, 1}

def test_encode_income_binary_raises_error_if_missing_income_column():
    wrong_df = pd.DataFrame({"other": ["<=50K", ">50K"]})
    with pytest.raises(ValueError):
        encode_income_binary(wrong_df)

def test_encode_income_binary_raises_error_if_wrong_input_type():
    wrong_input= {"canucks_rule_lol": "unfourtunately not true sad face" }
    with pytest.raises(TypeError):
        encode_income_binary(wrong_input)




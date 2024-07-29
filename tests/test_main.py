import pytest
import pandas as pd
from my_code.main import transform

def test_transform():
    # Create a sample DataFrame
    data = {'value': [1, 2, 3, None]}
    df = pd.DataFrame(data)

    # Apply transformation
    transformed_df = transform(df)

    # Debug prints
    print("Original DataFrame:")
    print(df)
    print("Transformed DataFrame:")
    print(transformed_df)

    # Check if the 'processed' column is added
    assert 'processed' in transformed_df.columns, "The 'processed' column was not added."

    # Check if the 'processed' column values are correctly computed
    assert transformed_df['processed'].iloc[0] == 2, "First value in 'processed' column is incorrect."
    assert transformed_df['processed'].iloc[1] == 4, "Second value in 'processed' column is incorrect."

    # Check if the number of rows is as expected (one row should be dropped)
    assert len(transformed_df) == 3, "The number of rows in the transformed DataFrame is incorrect."

    # Check if the NaN value was removed
    assert df['value'].isna().sum() == 1, "The number of NaN values in the original DataFrame is incorrect."

import pytest
import pandas as pd
from main import transform

def test_transform():
    # Create a sample DataFrame
    data = {'value': [1, 2, 3, None]}
    df = pd.DataFrame(data)

    # Apply transformation
    transformed_df = transform(df)

    # Check if the 'processed' column is added and correctly computed
    assert 'processed' in transformed_df.columns
    assert transformed_df['processed'].iloc[0] == 2  # 1 * 2
    assert transformed_df['processed'].iloc[1] == 4  # 2 * 2
    assert len(transformed_df) == 3  # One row should be dropped
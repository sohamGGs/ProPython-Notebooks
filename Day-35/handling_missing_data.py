import pandas as pd
import numpy as np

# In Data Science, we often deal with 'NaN' (Not a Number)
data = {
    'Product': ['A', 'B', 'C', 'D'],
    'Sales': [100, np.nan, 150, np.nan]
}

df = pd.DataFrame(data)

# Fill missing values with the average
df['Sales_Cleaned'] = df['Sales'].fillna(df['Sales'].mean())

print("Missing Data Handling:")
print(df)
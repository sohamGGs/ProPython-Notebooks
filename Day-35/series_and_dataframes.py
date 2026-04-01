import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Soham', 'Vedant', 'Rahul'],
    'Score': [95, 89, 72],
    'Passed': [True, True, False]
}

df = pd.DataFrame(data)
print("--- Full DataFrame ---")
print(df)
print(f"\nAverage Score: {df['Score'].mean()}")
import pandas as pd

df = pd.DataFrame({
    'Name': ['Soham', 'Vanshika', 'Rahul', 'Alice'],
    'Branch': ['CSE', 'AI-ML', 'CSE', 'IT'],
    'CGPA': [9.2, 8.8, 7.5, 8.5]
})

# Filter: Show only CSE students with CGPA > 8
top_cse = df[(df['Branch'] == 'CSE') & (df['CGPA'] > 8)]

print("Top CSE Students:")
print(top_cse)
import pandas as pd

def generate_report():
    # Create a dummy CSV for the project
    raw_data = {
        'Date': ['2026-03-01', '2026-03-01', '2026-03-02'],
        'Item': ['Laptop', 'Mouse', 'Laptop'],
        'Revenue': [60000, 1500, 62000]
    }
    df = pd.DataFrame(raw_data)
    
    # Group by Item and sum revenue
    summary = df.groupby('Item')['Revenue'].sum().reset_index()
    
    print("--- Monthly Sales Summary ---")
    print(summary)
    summary.to_csv("summary_report.csv", index=False)
    print("\nReport saved to summary_report.csv")

if __name__ == "__main__":
    generate_report()
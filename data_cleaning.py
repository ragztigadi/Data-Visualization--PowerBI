import pandas as pd

# Load dataset
file_path = "data/VG_Sales.csv"  # Update the file path as needed
df = pd.read_csv(file_path)

# Basic data cleaning
df.dropna(inplace=True)  # Remove rows with missing values
df.drop_duplicates(inplace=True)  # Remove duplicate rows

# Convert column names to lowercase
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Convert year column to integer type (if it exists)
if 'year' in df.columns:
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df.dropna(subset=['year'], inplace=True)
    df['year'] = df['year'].astype(int)

# Save cleaned data
df.to_csv("data/cleaned_VG_Sales.csv", index=False)

print("✅ Data cleaning complete. Cleaned file saved as 'cleaned_VG_Sales.csv'")
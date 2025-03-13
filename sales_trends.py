import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv('../data/cleaned_VG_Sales.csv')

# Sales by Genre
genre_sales = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)

# Plot Sales by Genre
plt.figure(figsize=(12, 6))
sns.barplot(x=genre_sales.index, y=genre_sales.values, palette='coolwarm')
plt.xticks(rotation=45)
plt.title("🎮 Sales by Genre")
plt.xlabel("Genre")
plt.ylabel("Global Sales (millions)")
plt.show()

# Print Top Selling Genre
print("🔥 Best-Selling Genre:", genre_sales.idxmax(), "with", round(genre_sales.max(), 2), "million sales.")

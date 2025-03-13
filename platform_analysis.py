import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv('../data/cleaned_VG_Sales.csv')

# Sales by Platform
platform_sales = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False)

# Plot Sales by Platform
plt.figure(figsize=(14, 6))
sns.barplot(x=platform_sales.index, y=platform_sales.values, palette='viridis')
plt.xticks(rotation=45)
plt.title("🎮 Sales by Platform")
plt.xlabel("Platform")
plt.ylabel("Global Sales (millions)")
plt.show()

# Print Top Selling Platform
print("🔥 Best-Selling Platform:", platform_sales.idxmax(), "with", round(platform_sales.max(), 2), "million sales.")

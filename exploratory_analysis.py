import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv('../data/cleaned_VG_Sales.csv')

# Top 10 best-selling games
top_games = df.groupby('Name')['Global_Sales'].sum().nlargest(10)
print("Top 10 Best-Selling Games:\n", top_games)

# Sales distribution by platform
plt.figure(figsize=(12, 6))
sns.boxplot(x='Platform', y='Global_Sales', data=df)
plt.xticks(rotation=90)
plt.title("Sales Distribution by Platform")
plt.show()

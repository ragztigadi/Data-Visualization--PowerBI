import pandas as pd
from fbprophet import Prophet

# Load cleaned dataset
df = pd.read_csv('../data/cleaned_VG_Sales.csv')

# Prepare data for forecasting
sales_by_year = df.groupby('Year')['Global_Sales'].sum().reset_index()
sales_by_year.columns = ['ds', 'y']

# Train forecasting model
model = Prophet()
model.fit(sales_by_year)

# Make future predictions
future = model.make_future_dataframe(periods=5, freq='Y')
forecast = model.predict(future)

# Plot forecast
model.plot(forecast)
plt.title("Global Sales Forecast for Next 5 Years")
plt.show()

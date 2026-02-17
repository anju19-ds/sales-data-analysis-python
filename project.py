import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("SampleSuperstore.csv")

# Basic info
print(df.head())
print(df.info())

# Total Sales
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

# Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.show()

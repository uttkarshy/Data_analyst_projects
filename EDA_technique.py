import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# Make a request to the Open Brewery DB API to get sales data
response = requests.get("https://api.openbrewerydb.org/breweries")

# Load the response data into a pandas DataFrame
data = pd.DataFrame(response.json())

# View the first 5 rows of the data
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Replace missing values with zeros
data = data.fillna(0)

# Check for duplicate values
print(data.duplicated().sum())

# Drop duplicate values
data = data.drop_duplicates()

# Convert the sales column to a numeric data type
data['sales'] = pd.to_numeric(data['sales'])

# Plot a histogram of the sales data
sns.histplot(data['sales'])
plt.show()

# Plot a scatter plot of sales versus number of employees
sns.scatterplot(x=data['employees'], y=data['sales'])
plt.show()

# Plot a bar chart of the average sales by state
sns.barplot(x='state', y='sales', data=data.groupby('state')['sales'].mean().reset_index())
plt.show()

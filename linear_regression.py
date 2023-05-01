import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('C:/Users/uttka/Desktop/data science/Data_analyst_projects/student_data.csv')
X = df[['School ID', 'Gender', 'Age', 'Size of Family', 'Father Education', 'Mother Education', 'Occupation of Father and Mother', 'Family Relation', 'Health']]
y = df['Grades']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean squared error: ", mse)
print("R-squared value: ", r2)

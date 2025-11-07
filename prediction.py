import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

filepath = "data/air_pollution/2025-09-01_2025-10-01.csv"


# Preparing data
data = pd.read_csv(filepath, sep = ";") 

# Getting aqi values
#X = data.drop('aqi', axis=1) 
X = data["dt"]
y = data['aqi']

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Using Linear Regression model
model = LinearRegression()

# Training the model
X_train_adapted = pd.DataFrame(X_train)
model.fit(X_train_adapted, y_train)

# Predicting on the test set
X_test_adapted = pd.DataFrame(X_test)
predictions = model.predict(X_test_adapted)

# Evaluating the model's performance
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}") 

#model.predict()


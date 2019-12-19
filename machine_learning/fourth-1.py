import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import  mean_absolute_error

# Load data
melbourne_file_path = '../input/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
# Filter rows with missing price values
filtered_melbourne_data = melbourne_data.dropna(axis=0)
# Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea',
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
print(melbourne_model.fit(X, y))
predicted_home_prices = melbourne_model.predict(X)
print(mean_absolute_error(y,predicted_home_prices))

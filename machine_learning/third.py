import pandas as pd
from sklearn.tree import DecisionTreeRegressor

melbourne_file_path = '../input/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
print(melbourne_data.columns)
melbourne_data = melbourne_data.dropna(axis=0)
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
x = melbourne_data[melbourne_features]
print(x.describe())
print(x.head())
melbourne_model = DecisionTreeRegressor(random_state=1)
print(melbourne_model.fit(x, y))
print("Making predictions for the following 5 houses:")
print(melbourne_model.predict(x.head()))
print(y.head())
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error as rmse
from sklearn.model_selection import cross_val_score

# 1. load the dataset
housing = pd.read_csv("housing.csv")

# 2. create a stratified test set
housing['income_cat'] = pd.cut(housing["median_income"],
                                bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
                                labels=[1,2,3,4,5])

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

for train_index, test_index in split.split(housing, housing['income_cat']):
    strat_train_set = housing.loc[train_index].drop("income_cat", axis=1)
    strat_test_set = housing.loc[test_index].drop("income_cat", axis=1)

# work on a copy of training date set

housing = strat_train_set.copy()

# 3. Separate features (or predictors) and labels
housing_labels = housing["median_house_value"].copy()
housing = housing.drop("median_house_value", axis=1)

print(housing, housing_labels)

#4. Separate numerical and columns
num_attribs= housing.drop("ocean_proximity", axis=1).columns.tolist()
cat_attribs = ["ocean_proximity"]

#5. Lets create a pipeline for numerical attributes

# for numerical columns
num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# for categorical columns
cat_pipeline = Pipeline([
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

# construct full pipeline

full_pipeline = ColumnTransformer([
    ("num", num_pipeline, num_attribs),
    ("cat", cat_pipeline, cat_attribs)  
])

# 6. Transform the data
housing_prepared = full_pipeline.fit_transform(housing)
print(housing_prepared)
print(housing_prepared.shape) # (16512, 13)

# (base) C:\DataScience\Project-Housingprice>python main.py
#        longitude  latitude  housing_median_age  total_rooms  ...  population  households  median_income  ocean_proximity
# 12655    -121.46     38.52                29.0       3873.0  ...      2237.0       706.0         2.1736           INLAND
# 15502    -117.23     33.09                 7.0       5320.0  ...      2015.0       768.0         6.3373       NEAR OCEAN
# 2908     -119.04     35.37                44.0       1618.0  ...       667.0       300.0         2.8750           INLAND
# 14053    -117.13     32.75                24.0       1877.0  ...       898.0       483.0         2.2264       NEAR OCEAN
# 20496    -118.70     34.28                27.0       3536.0  ...      1837.0       580.0         4.4964        <1H OCEAN
# ...          ...       ...                 ...          ...  ...         ...         ...            ...              ...
# 15174    -117.07     33.03                14.0       6665.0  ...      2026.0      1001.0         5.0900        <1H OCEAN
# 12661    -121.42     38.51                15.0       7901.0  ...      4769.0      1418.0         2.8139           INLAND
# 19263    -122.72     38.44                48.0        707.0  ...       458.0       172.0         3.1797        <1H OCEAN
# 19140    -122.70     38.31                14.0       3155.0  ...      1208.0       501.0         4.1964        <1H OCEAN
# 19773    -122.14     39.97                27.0       1079.0  ...       625.0       197.0         3.1319           INLAND

# [16512 rows x 9 columns] 12655     72100.0
# 15502    279600.0
# 2908      82700.0
# 14053    112500.0
# 20496    238300.0
#            ...
# 15174    268500.0
# 12661     90400.0
# 19263    140400.0
# 19140    258100.0
# 19773     62700.0
# Name: median_house_value, Length: 16512, dtype: float64
# [[-0.94135046  1.34743822  0.02756357 ...  0.          0.
#    0.        ]
#  [ 1.17178212 -1.19243966 -1.72201763 ...  0.          0.
#    1.        ]
#  [ 0.26758118 -0.1259716   1.22045984 ...  0.          0.
#    0.        ]
#  ...
#  [-1.5707942   1.31001828  1.53856552 ...  0.          0.
#    0.        ]
#  [-1.56080303  1.2492109  -1.1653327  ...  0.          0.
#    0.        ]
#  [-1.28105026  2.02567448 -0.13148926 ...  0.          0.
#    0.        ]]

# Day 93

# 7. Train the model

# Linear Regression Model
lin_reg = LinearRegression()
lin_reg.fit(housing_prepared, housing_labels)
lin_preds = lin_reg.predict(housing_prepared)
#lin_rmse = rmse(housing_labels, lin_preds)
lin_rmses = -cross_val_score(lin_reg, housing_prepared, housing_labels,
                            scoring="neg_root_mean_squared_error", cv=10)
#print("Linear Regression RMSE:", lin_rmse)
#print(f"The root mean squared error for Linear Regression is {lin_rmse:.2f}")
print(pd.Series(lin_rmses).describe())

# Decision Tree Model
dec_reg = LinearRegression()
dec_reg.fit(housing_prepared, housing_labels)
dec_preds = dec_reg.predict(housing_prepared)
# dec_rmse = rmse(housing_labels, dec_preds)
dec_rmses = -cross_val_score(dec_reg, housing_prepared, housing_labels,
                            scoring="neg_root_mean_squared_error", cv=10)
#print("Linear Regression RMSE:", lin_rmse)
#print(f"The root mean squared error for Decision Tree is {dec_rmse:.2f}")
print(pd.Series(dec_rmses).describe())


# Random Forest Model
random_forest_reg = RandomForestRegressor()
random_forest_reg.fit(housing_prepared, housing_labels)
random_forest_preds = random_forest_reg.predict(housing_prepared)
#random_forest_rmse = rmse(housing_labels, random_forest_preds)
random_forest_rmses = -cross_val_score(random_forest_reg, housing_prepared, housing_labels,
                            scoring="neg_root_mean_squared_error", cv=10)
#print("Linear Regression RMSE:", lin_rmse)
#print(f"The root mean squared error for Random Forest is {random_forest_rmse:.2f}")
print(pd.Series(random_forest_rmses).describe())

# output of cross validation

# count       10.000000
# mean     69204.322755
# std       2500.382157
# min      65318.224029
# 25%      67124.346106
# 50%      69404.658178
# 75%      70697.800632
# max      73003.752739
# dtype: float64
# count       10.000000
# mean     69204.322755
# std       2500.382157
# min      65318.224029
# 25%      67124.346106
# 50%      69404.658178
# 75%      70697.800632
# max      73003.752739
# dtype: float64
# count       10.000000
# mean     49312.110131
# std       2117.289375
# min      46087.049598
# 25%      47616.183280
# 50%      49175.746776
# 75%      50546.638172
# max      52921.255492
# dtype: float64
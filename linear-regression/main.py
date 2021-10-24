import pandas as pd
from coefficient import slr_slope_coef

pd.set_option('mode.chained_assignment', None)

with open("../data/titanic.csv") as file:
    titanic_df = pd.read_csv(file)
age_fare = titanic_df[["Age", "Fare"]]
age_fare.dropna(subset = ["Age", "Fare"], inplace=True)

m = slr_slope_coef(age_fare["Age"], age_fare["Fare"])
print(m)
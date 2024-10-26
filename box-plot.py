import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# loading the dataset
titanic = pd.read_csv("titanic.csv")

# survival rate by passanger class
sns.barplot(x="pclass", y="survived", data=titanic, estimator=lambda x: x.mean()) #estimator function will be applies to the y-axis i.e. survived
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.title("Survival Rate by Passenger Class")
plt.show()

import os
print("Current working directory:", os.getcwd())


import numpy as np 
import pandas as pd
import matplotlip.pyplot as plt

# membuat data sederhana
data ={ 
    "Name" : ["Alice", "Bob", "Charlie", " Diana", " Ethan"],
    "Age" : [24, 30, 18, 22, 29],
    "Score": [90, 85, 75, 90, 80]
}
df = pd.DataFrame(data)
print("DataFrame:\n",df)

#Analisis sederhana: mencari rata rata age dan score
mean_age = df["Age"].mean()
mean_score = df["Score"].mean()
print(f"\nRata-rata Age : {mean_age}")
print(f"\nRata - rata Score : {mean_score}")

#Visualisasi sederhana
plt.bar (df["Name"],df["Score"])
plt.title("Bar Plot Score")
plt.xlabel("Name")
plt.ylabel("Score")
plt.show()
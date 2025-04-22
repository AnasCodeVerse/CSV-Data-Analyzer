import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path=r"D:\Python projects\student_grades.csv"
df=pd.read_csv(file_path)
print("Basic information about the dataset:")
print("Rows:{df.shape[0]},Columns:{df.shape[1]}")
print("Colums Names:",list(df.columns))

print("Summary Statistics:")
print(df.describe())

df.hist(figsize=(10, 8), bins=20, color='blue', alpha=0.7)
plt.suptitle("Histogram for grades:")
plt.show()

# Plotting: Bar chart for categorical columns
for column in df.select_dtypes(include=['object']).columns:
    plt.figure(figsize=(10, 6))
    df[column].value_counts().plot(kind='bar', color='skyblue')
    plt.title(f'Bar chart for {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()
    plt.savefig()

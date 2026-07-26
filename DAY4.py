import pandas as pd

df = pd.read_csv("student_scores.csv")

print(df.head())
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Column Names:", df.columns.tolist())
print(df.info())
print(df.describe())

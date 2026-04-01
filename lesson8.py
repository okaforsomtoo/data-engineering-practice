import pandas as pd

data = {
    "name":["Somtoo", "Lilian", "James", "Amaka"],
    "age": [25, 23, 30, 27],
    "city": ["London", "Norwich", "Manchester", "Lagos"]
}
df = pd.DataFrame(data)
# print(df)

print(df.columns)
print(df.shape)
print(df["name"])
print(df.describe())

young = df[df["age"] < 27]
print(young)

df["senior"] = df['age'] > 26
print(df)
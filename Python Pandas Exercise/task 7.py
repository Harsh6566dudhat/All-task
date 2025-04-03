import pandas as pd


df = pd.read_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")


df['average-mileage'] = pd.to_numeric(df['average-mileage'], errors='coerce')


mileageDf = df.groupby('company')['average-mileage'].mean()

print(mileageDf)

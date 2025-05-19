import pandas as pd

fin = pd.read_csv('1.5.1.csv')
fin.Date = pd.to_datetime(fin.Date, format='%Y-%m-%d')

print(fin[(fin.Region == 'South') & (fin['Date'].dt.year == 2022) & (fin.Product == 'Product A')]['SalesCount'].sum())
print(fin[(fin.Region == 'South') & (fin['Date'].dt.year == 2022) & (fin.Product == 'Product B')]['SalesCount'].sum())
print(fin[(fin.Region == 'South') & (fin['Date'].dt.year == 2022) & (fin.Product == 'Product C')]['SalesCount'].sum())

def weekday(x):
    return x.weekday()
fin['week'] = fin['Date'].apply(weekday)

print(fin.groupby('week')['SalesCount'].sum())

print(fin.sort_values(['SalesCount']).iloc[0])

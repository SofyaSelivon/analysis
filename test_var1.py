import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def weekday(val):
    return val.strftime(("%A"))

data = pd.read_csv('Копия Аналитик — тестовое задание - data.csv')
data.event_date = pd.to_datetime(data.event_date, format='%Y-%m-%d')

data['weekday'] = data['event_date'].apply(weekday)

data_new = data.groupby('weekday')[['is_attend']].sum()
data_new = data_new.sort_values(['is_attend'])

sns.barplot(x='weekday', y = 'is_attend', data=data_new, color='green')
plt.title('Посещаемость учеников по дням недели')
plt.xlabel('День недели')
plt.ylabel('Количество учеников')
plt.show()
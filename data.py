import pandas as pd

csv_data = pd.read_csv("samp.csv")

json_data = pd.read_json("sample.json")

csv_data = csv_data.fillna(value="Unknown")
json_data = json_data.fillna(value="Unknown")

csv_data['age'] = pd.to_numeric(csv_data['age'])

filtered_data = csv_data[csv_data['age'] > 10]
sorted_data = csv_data.sort_values(by='age')
grouped_data = csv_data.groupby('city')['name'].agg(lambda x: ', '.join(x))

print(f"CSV Data: {csv_data}\nJSON Data: {json_data}\nFiltered Data: {filtered_data}\nSorted Data: {sorted_data}\n Grouped Data: {grouped_data}")

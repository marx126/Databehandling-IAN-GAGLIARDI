# Cities in Sweden - create dataset
import pandas as pd

cities = {"Kommun": ["Malmö", "Stockholm", "Uppsala", "Göteborg"],
          "Population": [347949, 975551, 233839, 583056]}
df = pd.DataFrame(cities)
print(f"{df}\n")

filt = df['Kommun'] == 'Göteborg'
print(f"{df[filt]}\n")

print(f"{df.sort_values('Population', ascending=False)}\n")

print(f"{df.sort_values('Population', ascending=False).head(3)}\n")

sweden_population = 10379295

df['Population (%)'] = (df['Population'] / sweden_population) * 100
print(f"{df.sort_values('Population', ascending=False)}\n")
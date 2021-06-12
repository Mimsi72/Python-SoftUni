country = input().split(', ')
capital = input().split(', ')
pairs = {country: capital for country, capital in zip(country, capital)}
print('\n'. join([f'{country} -> {capital}' for country, capital in pairs.items()]))


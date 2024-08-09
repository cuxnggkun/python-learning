country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
}

country_templete = "{name} {population} {capital} {currency}"

print(country_templete.format(**country))
# print(name="Germany", population="83 million", capital="Berlin", currency="Euro")

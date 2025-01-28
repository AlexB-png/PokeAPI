import requests


url = "https://pokeapi.co/api/v2/pokemon"

pokemon = input("What pokemon")

url = url + "/" + pokemon

response = requests.get(url)
print(response.status_code)

articles = response.json().get("sprites", []).get("back_shiny", [])
print(articles)

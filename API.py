import requests
import tkinter as tk

window = tk.Tk()
window.geometry("900x800")

label = tk.Label(text="Pikachu")
label.pack()

url = "https://pokeapi.co/api/v2/pokemon"

#pokemon = input("What pokemon")
pokemon = "pikachu"

url = url + "/" + pokemon

response = requests.get(url)


articles = response.json().get("sprites", []).get("back_shiny", [])
print(articles)

window.mainloop()
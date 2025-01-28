from tkinter import *
import requests

window = Tk()


url = "https://pokeapi.co/api/v2/pokemon"

# pokemon = input("What pokemon")
pokemon = "pikachu"
url = url + "/" + pokemon
response = requests.get(url)


canvas = Canvas(window, width = 300, height = 300)
canvas.pack()
img = PhotoImage(file="25.png")
canvas.create_image(50,50, anchor=NW, image=img)

articles = response.json().get("sprites", []).get("back_shiny", [])
print(articles)

frame = Frame(window, width=500, height=500)


window.mainloop()

import tkinter as tk
import requests

# Global variable to store the input value
PokemonValue = ""

# Input pokemon button
def InputPokemon():
    global PokemonValue  # Declare that we're using the global variable
    PokemonValue = PokemonInput.get()  # Store the input value in the global variable
    print(PokemonValue)  # Print the value to the terminal (for debugging)
    PokemonInput.delete(0,'end')  # Clear the input box

# Window
window = tk.Tk()
window.geometry("1000x500")

# Defines the items
PokemonInput = tk.Entry(width=30)
button1 = tk.Button(cursor="hand2", width=15, height=2, text="Input Pokemon", command=InputPokemon, activebackground="lime")

# Places the Items
PokemonInput.grid(row=0, column=0)
button1.grid(row=0, column=1)

# Displays The Window
window.mainloop()

# After the window is closed, you can use the stored value in PokemonValue
print("The Pokémon entered was:", PokemonValue)

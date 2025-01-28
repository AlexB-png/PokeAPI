import tkinter as tk

# Input pokemon button
def InputPokemon():
    Input = PokemonInput.get()
    PokemonInput.delete(0,'end')
    print( Input)

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


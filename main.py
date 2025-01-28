import tkinter as tk
import pandas as pd
import requests
import json

# Requests


def PokeAPI():
    url = "https://pokeapi.co/api/v2/pokemon"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        print("Failed to fetch data from PokeAPI")
        return None


# Global variables
success = False
register = False
UserName = ""
PokemonValue = ""
full = False
PokemonSelected = ""

# Register function


def register_account():
    root.destroy()
    global register
    register = True


# Login function
def login():
    global UserName
    userValue = user.get()
    passwordValue = password.get()
    UserName = userValue

    # Check if username or password fields are empty
    if userValue == "" or passwordValue == "":
        print("Please fill in all fields")
    else:
        # Clear the input fields
        user.delete(0, 'end')
        password.delete(0, 'end')

        try:

            with open("users.csv") as csv_file:
                df = pd.read_csv(csv_file)

                # Find the user row
                user_row = df[df['username'] == userValue]
                print(user_row)

                # Check if user exists
                if not user_row.empty:
                    stored_password = user_row['password'].values[0]

                    # Check if the entered password matches the stored password
                    if passwordValue == stored_password:
                        print("Login Successful")
                        root.destroy()
                        global success
                        success = True
                    else:
                        print("Invalid password")
                else:
                    print("Username not found")

        except FileNotFoundError:
            print("User database not found")

        except Exception as e:
            print(f"An error occurred: {str(e)}")


# Input Pokemon
def InputPokemon():
    global PokemonValue
    PokemonValue = PokemonInput.get()
    PokemonInput.delete(0, 'end')
    global PokemonSelected
    PokemonSelected = PokemonValue
    url = PokeAPI()
    url = url + "/" + PokemonValue
    print(url)

    # Update the DataFrame
    if PokemonValue != "":
        try:
            # Open users.csv
            df = pd.read_csv("users.csv")
            user_row_index = df[df['username'] == UserName].index

            if not user_row_index.empty:
                # Check if all slots are filled
                all_slots_filled = True
                for i in range(1, 7):
                    if pd.isna(df.loc[user_row_index,
                               f"pokemon{i}"]).values[0]:
                        all_slots_filled = False
                        break

                if all_slots_filled:
                    print("All 6 Pokemon slots are filled!")
                    global full
                    full = True
                    window.destroy()
                    return

                # Update the Pokemon values
                for i in range(1, 7):
                    if pd.isna(df.loc[user_row_index,
                                      f'pokemon{i}']).values[0]:

                        df.loc[user_row_index, f'pokemon{i}'] = PokemonValue
                        break

                # Save the updated DataFrame back to users.csv
                df.to_csv('users.csv', index=False)
                print(f"Pokemon {PokemonValue}"
                      "added successfully for {UserName}!")
            else:
                print("User not found in the CSV file.")

        except FileNotFoundError:
            print("User database not found.")
        except Exception as e:
            print(f"An error occurred while updating Pokemon: {str(e)}")


# Root setup for login
root = tk.Tk()
root.geometry("500x300")

# Modules for root
UserLabel = tk.Label(text="Username:")
PassLabel = tk.Label(text="Password:")
user = tk.Entry(width=30)
password = tk.Entry(width=30)
empty = tk.Canvas(height=1)
RegisterAcc = tk.Button(text="Register", command=register_account)

# Login Button
EnterLoginPage = tk.Button(text="Enter", command=login)

# Apply the modules to root
UserLabel.pack()
user.pack()
PassLabel.pack()
password.pack()
EnterLoginPage.pack()
RegisterAcc.pack()

root.mainloop()

# If login is successful, prompt user to enter Pokemon
if success:
    # Pokemon entry window
    window = tk.Tk()
    window.geometry("400x100")

    # Define the modules for Pokemon input
    PokemonInput = tk.Entry(width=30)
    Button1 = tk.Button(cursor="hand2", width=15, height=2,
                        text="Input Pokemon", command=InputPokemon,
                        activebackground="lime")

    # Display current user's Pokemon
    with open("users.csv", "r") as csv:
        df = pd.read_csv(csv, usecols=['username', 'pokemon1', 'pokemon2',
                                       'pokemon3', 'pokemon4',
                                       'pokemon5', 'pokemon6'])
        df = df.loc[df['username'] == UserName]
        print(UserName)
        print(df)
        poke1 = tk.Label(text=df['pokemon1'].values[0] if
                         pd.notna(df['pokemon1'].values[0]) else "None")
        poke2 = tk.Label(text=df['pokemon2'].values[0] if
                         pd.notna(df['pokemon2'].values[0]) else "None")
        poke3 = tk.Label(text=df['pokemon3'].values[0] if
                         pd.notna(df['pokemon3'].values[0]) else "None")
        poke4 = tk.Label(text=df['pokemon4'].values[0] if
                         pd.notna(df['pokemon4'].values[0]) else "None")
        poke5 = tk.Label(text=df['pokemon5'].values[0] if
                         pd.notna(df['pokemon5'].values[0]) else "None")
        poke6 = tk.Label(text=df['pokemon6'].values[0] if
                         pd.notna(df['pokemon6'].values[0]) else "None")

    # Places the modules to the window
    PokemonInput.grid(row=0, column=0)
    Button1.grid(row=1, column=0)
    poke1.grid(row=1, column=2)
    poke2.grid(row=1, column=3)
    poke3.grid(row=1, column=4)
    poke4.grid(row=1, column=5)
    poke5.grid(row=1, column=6)
    poke6.grid(row=1, column=7)

    # Display the window
    window.mainloop()

# If registering, create the registration page
elif register:
    def register_user():
        try:
            CSV = pd.read_csv("users.csv")
            print("File Exists!")
        except FileNotFoundError:
            print("File does not exist. Creating a new one.")
            CSV = pd.DataFrame(columns=['username', 'password', 'pokemon1',
                                        'pokemon2', 'pokemon3', 'pokemon4',
                                        'pokemon5', 'pokemon6'])
            CSV.to_csv("users.csv", index=False)

        user = RegisterUserInput.get()
        password = RegisterPassInput.get()

        if user == "" or password == "":
            print("Please fill in all fields")
        else:
            if CSV['username'].isin([user]).any():
                print("Username already exists")
            else:
                new_data = {'username': user, 'password': password,
                            'pokemon1': "", 'pokemon2': "", 'pokemon3': "",
                            'pokemon4': "", 'pokemon5': "", 'pokemon6': ""}
                new_row = pd.DataFrame([new_data])
                new_row.to_csv('users.csv', mode='a',
                               header=False, index=False)
                print(f"User {user} registered successfully!")

    RegisterWindow = tk.Tk()
    RegisterWindow.geometry("500x300")

    # Modules for Register
    RegisterUserLabel = tk.Label(text="Username:")
    RegisterPassLabel = tk.Label(text="Password:")
    RegisterUserInput = tk.Entry(width=30)
    RegisterPassInput = tk.Entry(width=30)
    RegisterEnterButton = tk.Button(text="Register", command=register_user)

    # Pack the modules
    RegisterUserLabel.pack()
    RegisterUserInput.pack()
    RegisterPassLabel.pack()
    RegisterPassInput.pack()
    RegisterEnterButton.pack()

    RegisterWindow.mainloop()

if full is True:
    def PokeReplace():
        num = Replace1.get()
        try:
            num = int(num)
        except TypeError:
            print("Invalid input. Please enter a number.")
        if num > 6 or num < 1:
            print("Fail")
        else:
            print(PokemonSelected)
            with open("users.csv", "r") as csv:
                index = "pokemon" + str(num)
                df = pd.read_csv(csv)
                print(index)
                df.loc[df['username'] == UserName, index] = PokemonSelected
                print(df)
                df.to_csv('users.csv', index=False)
                Replace.destroy()

    print("All 6 slots are full")

    # Defines the replace window for pokemon
    Replace = tk.Tk()
    Replace.geometry("300x300")

    # Modules for replace
    Label = tk.Label(text="Choose a slot to replace")
    Replace1 = tk.Entry()
    InputButton = tk.Button(text="Input", command=PokeReplace,
                            activebackground="lime")
    with open("users.csv", "r") as csv:
        df = pd.read_csv(csv, usecols=['username', 'pokemon1',
                                       'pokemon2', 'pokemon3', 'pokemon4',
                                       'pokemon5', 'pokemon6'])
        df = df.loc[df['username'] == UserName]
        print(UserName)
        print(df)
        poke1 = tk.Label(text=df['pokemon1'].values[0] if
                         pd.notna(df['pokemon1'].values[0]) else "None")
        poke2 = tk.Label(text=df['pokemon2'].values[0] if
                         pd.notna(df['pokemon2'].values[0]) else "None")
        poke3 = tk.Label(text=df['pokemon3'].values[0] if
                         pd.notna(df['pokemon3'].values[0]) else "None")
        poke4 = tk.Label(text=df['pokemon4'].values[0] if
                         pd.notna(df['pokemon4'].values[0]) else "None")
        poke5 = tk.Label(text=df['pokemon5'].values[0] if
                         pd.notna(df['pokemon5'].values[0]) else "None")
        poke6 = tk.Label(text=df['pokemon6'].values[0] if
                         pd.notna(df['pokemon6'].values[0]) else "None")

    # Places the modules to the window
    Label.grid(row=1, column=1)
    poke1.grid(row=0, column=0)
    poke2.grid(row=1, column=0)
    poke3.grid(row=2, column=0)
    poke4.grid(row=3, column=0)
    poke5.grid(row=4, column=0)
    poke6.grid(row=5, column=0)
    Replace1.grid(row=0, column=1)
    InputButton.grid(row=3, column=1)

    Replace.mainloop()

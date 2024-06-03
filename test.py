# Description: This is a program that load a pokjemon from a third party library and print it's name and it's abilities and show the image of the pokemon

# Importing the requests library

import requests
import random

# Defining the URL of the API
pokemon_id = random.randint(1, 151)
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"

# Making a request to the API

response = requests.get(url)

# Getting the JSON data from the response

data = response.json()

# Getting the name of the pokemon

name = data["name"]

# Getting the abilities of the pokemon

abilities = data["abilities"]

# Printing the name of the pokemon

print("Name: " + name)

# Printing the abilities of the pokemon

print("Abilities: ")

for ability in abilities:

    print(ability["ability"]["name"])

# Getting the image of the pokemon

image_url = data["sprites"]["front_default"]

# Importing the Image library

from PIL import ImageTk, Image

import requests

from io import BytesIO
import tkinter as tk
import pygame

# Making a request to the image URL

response = requests.get(image_url)

# Getting the image data from the response
image_data = response.content

# Creating an image object from the image data
image = Image.open(BytesIO(image_data))

# Convert the image to 'RGB'
image = image.convert('RGB')

# Resizing the window to fit the image
image_width, image_height = image.size
window_width = image_width + 20
window_height = image_height + 20

# Displaying the image
image.show()

# Initialize the pygame mixer
pygame.mixer.init()


# Function to play the pokemon cry
def play_pokemon_cry():
    # Get the sound URL from the API response
    sound_url = data["species"]["url"]
    
    # Make a request to the sound URL
    response = requests.get(sound_url)
    sound_data = response.json()
    
    # Get the sound file URL
    sound_file_url = sound_data["flavor_text_entries"][0]["sound"]["url"]
    
    # Make a request to the sound file URL
    response = requests.get(sound_file_url)
    sound_data = response.content
    
    # Save the sound file locally
    with open("pokemon_cry.wav", "wb+") as file:
        file.write(sound_data)
    
    # Load and play the sound file
    pygame.mixer.music.load("pokemon_cry.wav")
    pygame.mixer.music.play()


# Function to randomize the pokemon sprite
def randomize_sprite2():
    # Generate a new random pokemon ID
    pokemon_id = random.randint(1, 151)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    
    # Make a request to the API
    response = requests.get(url)
    data = response.json()
    
    # Get the new image URL
    image_url = data["sprites"]["front_default"]
    sound_url = data['cries']['latest']
    # Make a request to the new image URL
    response = requests.get(image_url)
    image_data = response.content
    
    # Create a new image object from the image data
    image = Image.open(BytesIO(image_data))
    image = image.convert('RGB')
    
    # Convert the PIL Image object to a Tkinter PhotoImage object
    tk_image = ImageTk.PhotoImage(image)

    # Update the displayed image
    image_label.configure(image=tk_image)
    image_label.image = tk_image

    # Play the pokemon cry
    response = requests.get(sound_url)
    sound_data = response.content

    # Get the moves of the pokemon
    moves = data["moves"]
    
    # Get the updated name of the pokemon
    name = data["name"]

    # Create a label to display the name of the pokemon
    name_label = tk.Label(window, text="Name: " + name)
    name_label.pack()
    # Display only the first 4 moves
    for move in moves[:4]:
        move_name = move["move"]["name"]
        move_label = tk.Label(window, text=move_name)
        move_label.pack()
    # Create a label to display the moves of the pokemon
    #moves_label = tk.Label(window, text="Moves: ")
    #moves_label.pack()

    
    
    # Save the sound file locally
    with open(f"pokemon_cry{pokemon_id}.ogg", "wb+") as file:
        file.write(sound_data)
    
    # Load and play the sound file
    pygame.mixer.music.load(f"pokemon_cry{pokemon_id}.ogg")
    pygame.mixer.music.play()

# Create a list to store the labels
labels = []


# Function to randomize the pokemon sprite
def randomize_sprite():
    # Clear the previous labels
    for label in labels:
        label.destroy()
    labels.clear()

    # Your existing code
    pokemon_id = random.randint(1, 151)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    data = response.json()
    image_url = data["sprites"]["front_default"]
    sound_url = data['cries']['latest']
    response = requests.get(image_url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    image = image.convert('RGB')
    tk_image = ImageTk.PhotoImage(image)
    image_label.configure(image=tk_image)
    image_label.image = tk_image

    # Get the updated name of the pokemon
    name = data["name"]

    # Create a label to display the name of the pokemon
    name_label = tk.Label(window, text="Name: " + name)
    name_label.pack()
    labels.append(name_label)

    # Get the moves of the pokemon
    moves = data["moves"]

    # Create buttons for each move
    for move in moves[:4]:
        move_name = move["move"]["name"]
        move_button = tk.Button(window, text=move_name, command=lambda move_name=move_name: use_move(move_name))
        move_button.pack()
        labels.append(move_button)


    # Display only the first 4 moves
    """ for move in moves[:4]:
        move_name = move["move"]["name"]
        move_label = tk.Label(window, text=move_name)
        move_label.pack()
        labels.append(move_label)
 """
    # Your existing code
    response = requests.get(sound_url)
    sound_data = response.content
    with open(f"pokemon_cry{pokemon_id}.ogg", "wb+") as file:
        file.write(sound_data)
    pygame.mixer.music.load(f"pokemon_cry{pokemon_id}.ogg")
    pygame.mixer.music.play()


# Create a new tkinter window
window = tk.Tk()

# Create a button to randomize the pokemon sprite
randomize_button = tk.Button(window, text="Randomize Sprite", command=randomize_sprite)
randomize_button.pack()

# Create a label to display the image
image_label = tk.Label(window)
image_label.pack()

# Run the tkinter event loop
window.mainloop()


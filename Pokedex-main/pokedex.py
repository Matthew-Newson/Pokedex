import requests
import sys
import urllib.request
from PIL import Image
from matplotlib import pyplot as plot
from deep_translator import GoogleTranslator

api = ("https://pokeapi.co/api/v2/pokemon/pikachu")
x = requests.get(api).ok
if(x):
    print("Valid Name")
else:
    print("Invalid Name")

def menu():
    print (""" .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
| |   ______     | | |     ____     | | |  ___  ____   | | |  _________   | | |  ________    | | |  _________   | | |  ____  ____  | |
| |  |_   __ \   | | |   .'    `.   | | | |_  ||_  _|  | | | |_   ___  |  | | | |_   ___ `.  | | | |_   ___  |  | | | |_  _||_  _| | |
| |    | |__) |  | | |  /  .--.  \  | | |   | |_/ /    | | |   | |_  \_|  | | |   | |   `. \ | | |   | |_  \_|  | | |   \ \  / /   | |
| |    |  ___/   | | |  | |    | |  | | |   |  __'.    | | |   |  _|  _   | | |   | |    | | | | |   |  _|  _   | | |    > `' <    | |
| |   _| |_      | | |  \  `--'  /  | | |  _| |  \ \_  | | |  _| |___/ |  | | |  _| |___.' / | | |  _| |___/ |  | | |  _/ /'`\ \_  | |
| |  |_____|     | | |   `.____.'   | | | |____||____| | | | |_________|  | | | |________.'  | | | |_________|  | | | |____||____| | |
| |              | | |              | | |              | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
'----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' """)
    Choice = input("""
        A: Login
        B: Register
        C: Show pokemon team
        D: Search pokemon
                   
    Please enter your choice: """)

    if Choice.lower() == "a": 
        login()
    elif Choice.lower() == "b" :
        register()
    elif Choice.lower() == "c" :
        pokiteam()
    elif Choice.lower() == "d" :
        pokisearch()
    else:
        print("Invalid option shutting down") 
        sys.exit()

def login():
    pass

def register():
    pass

def pokiteam():
    pass

def pokeimg(pokimane):
    pokipik = pokimane["sprites"]["front_default"]
    urllib.request.urlretrieve( f'{pokipik}', f"{pokimane['name']}.png") 
    img = Image.open(f"{pokimane['name']}.png")
    plot.imshow(img)
    plot.axis ("off") 
    plot.show()

def pokeabilities(poki,abilities):
    print(f"{poki}'s abilities are:")
    for i, ability in enumerate(abilities):
        print(f"{i}: {ability["ability"]["name"]}")
        url = ability["ability"]["url"]
        effects = requests.get(url).json()
        indiv_effect = effects["effect_entries"]
        effect_short = indiv_effect[0]["short_effect"]
        effectdes = GoogleTranslator(source="auto", target="english").translate(effect_short) 
        print(effectdes)

# def pokimove():
#     pass


def pokisearch():
    poki = input("Enter Pokemon name: ").lower()
    pokimane = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poki}").ok
    if (pokimane):
         pokimane = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poki}").json()
         abilities = pokimane["abilities"]
         pokeimg(pokimane)
         pokeabilities(poki,abilities)
        #  pokimoves()
    else:
        print("Invalid pokemon name")
        pokisearch()
    
menu()


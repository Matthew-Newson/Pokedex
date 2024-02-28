import json

import requests
api = ("https://pokeapi.co/api/v2/pokemon/pikachu")
x = requests.get(api).ok
if(x):
   print("Valid Name")
else:
   print("Invalid Name")


def loginmenu():
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
                 
   Please enter your choice: """)

   if Choice.lower() == "a":
       login()
   elif Choice.lower() == "b" :
       register()
   else:
       print("Invalid option shutting down")
       import sys
       sys.exit()

    
def searchmenu():
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
   SearchChoice = input("""
       A: Visit Your pokimon team
       B: Search for pokimon
                 
   Please enter your choice: """)
      
   if SearchChoice.lower() == "a" :
       pokiteam()
   elif SearchChoice.lower() == "b" :
       pokisearch()
   else:
       print("Invalid option shutting down")
       import sys
       sys.exit()


def register():
   Username = input("What is your username: ")
   Password = input("What do you want your password to be: ")
   Passwordcheck = input("Please enter your password again: ")
   if Username in texts:
    while Username in texts:
       Username = input("Username already in use please try again: ")
   if Password != Passwordcheck:
      while Password != Passwordcheck:
         Password = input("Your passwords did not match please try again: ")
         Passwordcheck = input("Please enter your password again: ")
   with open("login.json", "w")as f:
    texts[Username] = {"Username": Username, "Password": Password}
    json.dump(texts,f)
    stop = input("Please press enter to continue")
   loginmenu() 
        
      


def login():
   user = input("Enter your username: ")
   password = input("Enter your pass: ")
   if user in texts:
       if user == (texts[user]["Username"]) and password == (texts[user]["Password"]):
           print(f"Welcome {user}")
           stop = input("Please press enter to continue")
           searchmenu()
       else:
           print("Username or password incorrect")
           login() 
   else:
       print("Username or password incorrect")
       login()



def pokiteam():
   pass


def pokeimg(pokimane):
   from PIL import Image
   from matplotlib import pyplot as plot
   pokipik = pokimane["sprites"]["front_default"]
   resp = requests.get(pokipik, verify=False)
   with open(f"{pokimane['name']}.png", 'wb') as f:
       for chunk in resp:
           f.write(chunk)
   img = Image.open(f"{pokimane['name']}.png")
   plot.imshow(img)
   plot.axis ("off")
   plot.show()


def pokeabilities(poki,abilities):
   from deep_translator import GoogleTranslator
   print(f"{poki}'s abilities are:")
   for i, ability in enumerate(abilities):
       print(f"{i}: {ability['ability']['name']}")
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
       #pokimoves()
   else:
       print("Invalid pokemon name")
       pokisearch()


texts = dict()
with open("login.json", "r") as f:
    texts = json.load(f)

loginmenu()


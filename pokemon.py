import requests
import pandas as pd

url="https://pokeapi.co/api/v2/"

def get_details(name):
    res=requests.get(f"{url}/pokemon/{name}")
    if res.status_code==200:
        #df=pd.json_normalize(res.json())
        #df.to_csv("pokemon.csv", index=False)
        #print(res.json())
        return res.json()
    else:
        print(f" pokemon details not found {res.status_code}")

while True:
    pokemon=input("Enter a Pokemon Name or stop to end:")
    if pokemon=='stop':
        break
    out=get_details(pokemon)
    if out:
        print(f"Name:{out['name'].capitalize()}")
        print(f"ID:{out['id']}")
        print(f"Abilities:{out['abilities'][1]['ability']['name']}")
        print(f"Height:{out['height']}")
        print(f"Weight:{out['weight']}")


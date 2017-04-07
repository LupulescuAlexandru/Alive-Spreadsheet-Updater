#Colin Mcrae
import pandas as pd

df = pd.read_csv("example.csv")


STEAMID = {0: 76561198064646048, 1: 76561198032032720, 2: 76561198131077689,
            3: 76561198292504915, 4: 76561198067346802, 5: 76561198182490079,
            6: 754, 7: 76561198070115844, 8:2, 9:1, 10:3}

def return_total_kills(list=None):
    return {df['Name'][i]: {"Kills": df['Kills'][i], "SteamID": df['SteamID'][i]} for i in list}

names = [(i) for i, n in enumerate([name for name in df['Name']])]

def print_dict_component(dict_key, dictt=None):

    new_values = dict()
    for key, values in dictt.items():
        for i, std in enumerate([player_id for player_id in STEAMID.values()]):
            if (values[dict_key]) == STEAMID[i]:
                new_values[key] = values['Kills']
    return (new_values)



diccct = return_total_kills(names)
namenkills = print_dict_component("SteamID", diccct)

namesalive = list(namenkills.keys())
killsalive = list(namenkills.values())

newdf = pd.DataFrame({
                    'Name': namesalive,
                    'Kills' : killsalive})



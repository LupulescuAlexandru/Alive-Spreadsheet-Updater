#Colin Mcrae
import os
import pandas as pd
from openpyxl import load_workbook
import xlsx2csv

files = []
def identifymatch():
    cwd = os.getcwd()
    for file in os.listdir(cwd):
        if file.startswith("match"):
            return file

df = pd.read_csv(identifymatch())


STEAMID = {0: 76561198064646048, 1: 76561198032032720, 2: 76561198131077689,
            3: 76561198292504915, 4: 76561198067346802, 5: 76561198182490079,
            6: 754, 7: 76561198070115844, 8:2, 9:1, 10:3}

def return_total_kills(list=None):
    return {df['Name'][i]: {"Kills": df['Kills'][i], "SteamID": df['SteamID'][i], "Deaths": df['Deaths'][i], "Assists": df['Assists'][i], 'MVP': df['MVP'][i]} for i in list}

names = [(i) for i, n in enumerate([name for name in df['Name']])]

def print_dict_component(dict_key, dictt=None, valuetypee=None):

    new_values = dict()
    for key, values in dictt.items():
        for i, std in enumerate([player_id for player_id in STEAMID.values()]):
            if (values[dict_key]) == STEAMID[i]:
                new_values[key] = values[valuetypee]
    return (new_values)


diccct = return_total_kills(names)
namenkills = print_dict_component("SteamID", diccct, 'Kills')
deaths = print_dict_component("SteamID", diccct, 'Deaths')
assists = print_dict_component("SteamID", diccct, 'Assists')
mvps = print_dict_component("SteamID", diccct, 'MVP')

namesalive = list(namenkills.keys())
killsalive = list(namenkills.values())
deaths = list(deaths.values())
assists = list(assists.values())
mvps = list(mvps.values())


newdf = pd.DataFrame({
                    'Name': namesalive,
                    'Kills' : killsalive,
                    'Deaths' : deaths,
                    'Assists' : assists,
                    'MVPs': mvps})

outbackex = pd.ExcelFile("output.xlsx")
outback = outbackex.parse("Data")

book = load_workbook('output.xlsx')
writer = pd.ExcelWriter('output.xlsx', engine='openpyxl')
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

newdf.to_excel(writer, "Data", startrow=outback.shape[0]+2, index=False, header=False)

writer.save()








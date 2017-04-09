import os

def convert():
    cwd = os.getcwd()
    for file in os.listdir(cwd):
        if file.startswith("match"):
            os.system('python xlsx2csv.py -n Players ' +  file + ' ' + file + '.csv')

    for file in os.listdir(cwd):
        if file.endswith(".xlsx"):
            os.remove(file)

convert()
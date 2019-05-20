# pip install kaggle
# kaggle datasets download -d karangdiya/fifa19 --unzip --force

import csv
import matplotlib.pyplot as plt

playersData = []

# open the downloaded csv file and append the player data into the created list
with open('data.csv', 'r', encoding='utf-8') as fifa:
    reader = csv.DictReader(fifa)
    for i in reader:
       playersData.append(dict(i))

# creating each list for the categories
playerAge = []
playerOverall = []
usiaTuaBagus = []
usiaTuaJelek = []
usiaMudaBagus = []
usiaMudaJelek = []
overallTuaBagus = []
overallTuaJelek = []
overallMudaBagus = []
overallMudaJelek = []

i = 0

# categorize on which category each player belong to
while i < len(playersData):
    playerAge.append(int(playersData[i]['Age']))
    playerOverall.append(int(playersData[i]['Overall']))

    if playerAge[i] >= 25 and playerOverall[i] >= 85:
        usiaTuaBagus.append(playerAge[i])
        overallTuaBagus.append(playerOverall[i])
    elif playerAge[i] >= 25 and playerOverall[i] < 85:
        usiaTuaJelek.append(playerAge[i])
        overallTuaJelek.append(playerOverall[i])
    elif playerAge[i] < 25 and playerOverall[i] >= 85:
        usiaMudaBagus.append(playerAge[i])
        overallMudaBagus.append(playerOverall[i])
    elif playerAge[i] < 25 and playerOverall[i] < 85:
        usiaMudaJelek.append(playerAge[i])
        overallMudaJelek.append(playerOverall[i])
    i+=1

# plotting the graph
plt.scatter(usiaMudaBagus, overallMudaBagus, color='b')
plt.scatter(usiaMudaJelek, overallMudaJelek, color='r')
plt.scatter(usiaTuaBagus, overallTuaBagus, color='y')
plt.scatter(usiaTuaJelek, overallTuaJelek, color='k')
plt.xlabel('Age')
plt.ylabel('Overall Performance')
plt.legend(['Muda Bagus', 'Muda Jelek', 'Tua Bagus', 'Tua Jelek'])
plt.grid(True)

plt.show()
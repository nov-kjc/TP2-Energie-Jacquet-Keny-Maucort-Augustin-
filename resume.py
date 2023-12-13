import csv
table=[]
with open("RTE_2020.csv",newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=",")
    for row in reader:
        table.append(row)

energie = ["Fioul","Charbon","Gaz", "Nucleaire", "Eolien", "Solaire", "Hydraulique","Bioenergies"]
production = []


#On charche à avoir la production total avec le programme qui va suivre
for i in range(len(table[0])):
    if table[0][i] in energie: 
        for k in range(1,len(table)):
            production.append(table[k][i])

production_tot = 0
liste = []

for i in production: 
    if i == "":
        continue
    else:
        i = int(i)
        production_tot += i



print("la production totale est de :",production_tot, "kw")



#On cherche à avoir le rapport entre l'énergie nucléaire et la production totale


production1 = []

for i in range(len(table[0])):
    if table[0][i] == "Nucleaire": 
        for k in range(1,len(table)):
            production1.append(table[k][i])

production_tot1 = 0


for i in production1: 
    if i == "":
        continue
    else:
        i = int(i)
        production_tot1 += i
        


print("la production nuleair est de : ",production_tot1, "kw")

#On cherche la production du Fioul

production2 = []

for i in range(len(table[0])):
    if table[0][i] == "Fioul": 
        for k in range(1,len(table)):
            production2.append(table[k][i])

production_tot2 = 0

for i in production2: 
    if i == "":
        continue
    else:
        i = int(i)
        production_tot2 += i


print("la production Fioul est de : ",production_tot2, "kw")


#On cherche maintenant le Gaz
production3 = []

for i in range(len(table[0])):
    if table[0][i] == "Gaz": 
        for k in range(1,len(table)):
            production3.append(table[k][i])

production_tot3 = 0

for i in production3: 
    if i == "":
        continue
    else:
        i = int(i)
        production_tot3 += i

print("la production Gaz est de : ",production_tot3, "kw")

#On cherche maintenant l'Eolien

production4 = []

for i in range(len(table[0])):
    if table[0][i] == "Eolien": 
        for k in range(1,len(table)):
            production4.append(table[k][i])

production_tot4 = 0

for i in production4: 
    if i == "":
        continue
    else:
        i = int(i)
        production_tot4 += i

print("la production Eolien est de : ",production_tot4, "kw")

#On cherche maintenant Solaire

production5 = []

for i in range(len(table[0])):
    if table[0][i] == "Solaire": 
        for k in range(1,len(table)):
            production5.append(table[k][i])

production_tot5 = 0

for i in production5: 
    if i == "":
        continue
    else:
        i = int(i)
        production_tot5 += i

print("la production Solaire est de : ",production_tot5, "kw")

#On cherche maintenant Hydrolique

production6 = []

for i in range(len(table[0])):
    if table[0][i] == "Hydraulique": 
        for k in range(1,len(table)):
            production6.append(table[k][i])

production_tot6 = 0

for i in production6: 
    if i == "":
        continue
    else:
        i = int(i)
        production_tot6 += i

print("la production Hydrolique est de : ",production_tot6, "kw")

#On cherche maintenant Charbon

production7 = []

for i in range(len(table[0])):
    if table[0][i] == "Charbon": 
        for k in range(1,len(table)):
            production7.append(table[k][i])

production_tot7 = 0

for i in production7: 
    if i == "":
        continue
    else:
        i = int(i)
        production_tot7 += i

print("la production Charbon est de : ",production_tot7, "kw")

#On cherche maintenant Bioenergies

production7 = []

for i in range(len(table[0])):
    if table[0][i] == "Bioenergies": 
        for k in range(1,len(table)):
            production7.append(table[k][i])

production_tot7 = 0

for i in production7: 
    if i == "":
        continue
    else:
        i = int(i)
        production_tot7 += i

print("la production Bioenergies est de : ",production_tot7, "kw")

renouvelable = production_tot7+ production_tot6 + production_tot5 + production_tot4
non_renouvelable = production_tot7 + production_tot1 + production_tot2 + production_tot1 + production_tot3
print("l'énergie reouvelable représente:" ,renouvelable," kw ")
print("l'énergie non reouvelable représente:" ,non_renouvelable, "kw")




import os

path = os.path.join("/home", "pi", "Documents", "text.txt")

with open(path, 'r+') as f:
    print(f.read())
    f.write(input("Type what you would like to add to the file."))


import csv

mylist = [["Top Gun", "Risky Buisness", "Minority Report"],
          ["Titanic", "The Revenant", "Inception"],
          ["Training Day", "Man on Fire", "Flight"]]

with open("st.csv", 'w') as f:
    r = csv.writer(f, delimiter=',')
    for i in range(0,3):
        r.writerow(mylist[i])

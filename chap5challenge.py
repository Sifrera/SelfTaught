favs = ["Jimi", "Ozzy", "Black Keys", "Kendrick"]

locales = [ (70.0234, 12.3456),
            (34.5678, 09.8765),
            (40.1823, 120.4123) ]
me = { "height": "6'",
       "weight": "145",
       "Favorite Author": "Orwell",
       "Favorite Color": "purple" }
query = input("What would you like to know about me?")
if query in me:
    response = me[query]
    print(response)
else:
    print("No Data.")



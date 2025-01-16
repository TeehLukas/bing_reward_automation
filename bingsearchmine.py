import webbrowser
import time
import pyautogui
import random
# Liste der Suchanfragen
search_queries = ['apple','banana','orange','grape','watermelon','pineapple','blueberry','strawberry','kiwi','mango','peach','pear','plum','cherry','apricot','nectarine','raspberry','blackberry','fig','pomegranate','lemon','lime','coconut','papaya','guava','persimmon','lychee','dragonfruit','passionfruit','cranberry','cucumber','tomato','potato','onion','garlic','ginger','carrot','broccoli','spinach','kale','lettuce','celery','parsley','coriander','basil','thyme','rosemary','oregano','dill','chive','sage','mint','lavender','bayleaf','artichoke','asparagus','beetroot','cauliflower','zucchini','squash','eggplant','pepper','chili','radish','turnip','parsnip','cabbage','brusselsprout','leek','scallion','mushroom','peanut','almond','cashew','pistachio','walnut','hazelnut','pecan','chestnut','macadamia','brazilnut','sunflower','pumpkinseed','sesameseed','chia','flaxseed','quinoa','barley','oat','wheat','corn','rice','millet','buckwheat','amaranth','teff','soybean','lentil','chickpea','bean','peas'
]

# Anzahl der Suchanfragen
num_searches = 30

# Bing-Such-URL
bing_url = "https://www.bing.com"

# Schleife, um die Suchanfragen auszuführen
for i in range(num_searches):
    eins = search_queries[i+random.randint(1,len(search_queries))]
    zwei = search_queries[i+random.randint(1,len(search_queries))]
    query = eins + " " + zwei
    print(query)
    webbrowser.open_new_tab(bing_url)
    time.sleep(3)  # Wartezeit, um sicherzustellen, dass der Tab geöffnet istpea
    pyautogui.write(query, interval=0.1)  # Zeichen für Zeichen eingeben
    pyautogui.press('enter')
    time.sleep(2)  # Wartezeit zwischen den Suchanfragen (in Sekunden)

#print("Suchanfragen abgeschlossen!")

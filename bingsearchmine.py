import webbrowser
import time
import pyautogui
import random

search_queries = ['apple','banana','orange','grape','watermelon','pineapple','blueberry','strawberry','kiwi','mango','peach','pear',
                  'plum','cherry','apricot','nectarine','raspberry','blackberry','fig','pomegranate','lemon','lime','coconut','papaya',
                  'guava','persimmon','lychee','dragonfruit','passionfruit','cranberry','cucumber','tomato','potato','onion','garlic',
                  'ginger','carrot','broccoli','spinach','kale','lettuce','celery','parsley','coriander','basil','thyme','rosemary',
                  'oregano','dill','chive','sage','mint','lavender','bayleaf','artichoke','asparagus','beetroot','cauliflower','zucchini',
                  'squash','eggplant','pepper','chili','radish','turnip','parsnip','cabbage','brusselsprout','leek','scallion','mushroom',
                  'peanut','almond','cashew','pistachio','walnut','hazelnut','pecan','chestnut','macadamia','brazilnut','sunflower','pumpkinseed',
                  'sesameseed','chia','flaxseed','quinoa','barley','oat','wheat','corn','rice','millet','buckwheat','amaranth','teff',
                  'soybean','lentil','chickpea','bean','peas']

bing = "https://www.bing.com"
num_searches = 30

for i in range(num_searches):
    eins_index = (i + random.randint(1, len(search_queries) - 1)) % len(search_queries)
    zwei_index = (i + random.randint(1, len(search_queries) - 1)) % len(search_queries)
    eins = search_queries[eins_index]
    zwei = search_queries[zwei_index]
    query = eins + " " + zwei
    webbrowser.open_new_tab(bing)
    time.sleep(3)  
    pyautogui.write(query, interval=0.1) 
    pyautogui.press('enter')
    time.sleep(2)  

print("Search requests finished!")

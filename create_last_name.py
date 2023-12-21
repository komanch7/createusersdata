import random
import json
import os
from unicodedata import combining, normalize

def get_list(path):
    if path != "":
        path = os.path.dirname(__file__) + "/" + path
        return json.load(open(path))
# 



# nationality = ['en', 'de', 'us', 'ru', 'ua']
def last_name_selection(names=[], nationality='en'):
    if names != None and type(names) == dict and nationality != '':
        return random.choice(names[nationality])
    elif names != None and type(names) == dict and nationality == '':
        nationality = 'en'
        return random.choice(names[nationality])
    else:
        return "Enter variable \"names\"!"
# 


# 
if __name__ == "__main__":
    print ("Start programm play!\n")
    last_name = get_list("last_names.json")
    # print(last_name)

    res_last_name = last_name_selection(last_name, nationality='de')
    print(res_last_name)
    print ("\nEnd programm play!")
else: 
    print ("An error has occurred! Unable to start")
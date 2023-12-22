import json
import os

# 
def get_list(path):
    if path != "":
        path = os.path.dirname(__file__) + "/" + path
        return json.load(open(path))

# 
if __name__ == "__main__":
    print ("Start programm play!\n")

    fisrt_name = get_list("first_names.json")
    print(fisrt_name)
    
    print ("\nEnd programm play!")
else: 
    print ("An error has occurred! Unable to start")
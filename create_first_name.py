import random
import get_list

# 
# gender = ['male', 'female']
# nationality = ['en', '']
def first_name_selection(names=[], gender='male', nationality='en'):
    if names != None and type(names) == dict:
        return random.choice(names[gender][nationality]) #+ " : male"
    elif names != None and type(names) == dict and gender == 'female':
        gender = 'female'
        nationality = 'de'
        return random.choice(names[gender][nationality]) #+ " : female"
    else:
        return "Enter variable \"names\"!"

# 
if __name__ == "__main__":
    print ("Start programm play!\n")
    fisrt_name = get_list.get_list("first_names.json")
    # print(fisrt_name)

    res_first_name = first_name_selection(fisrt_name, gender='male', nationality='us')
    print(res_first_name)
    print ("\nEnd programm play!")
else: 
    print ("An error has occurred! Unable to start")
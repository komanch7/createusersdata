from datetime import datetime, timedelta
import random

def get_year_ago(age):
    current_year = datetime.now().year
    random_year = current_year - age
    random_month = random.randint(1, 12)
    random_day = random.randint(1, 28)  # Assuming all months have 28 days for simplicity

    random_date = datetime(random_year, random_month, random_day)
    return random_date

# 
if __name__ == "__main__":
    print ("Start programm play!\n")
    age = 18
    random_date = get_year_ago(age)
    # print(f"дата {years_ago} лет назад: {random_date.strftime('%Y-%m-%d')}")
    print(random_date.strftime('%Y-%m-%d'))
    print ("\nEnd programm play!")
else: 
    print ("An error has occurred! Unable to start")



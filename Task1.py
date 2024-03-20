from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    
     #data Preparation
    birthday_dict = defaultdict(list)

     # retrieval of the current date
    today = datetime.today().date()

     # Adjust current date to the start of the next week (Monday)
    monday_of_next_week = today + timedelta(days=(7 - today.weekday()))

     # sorting users
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

     # date type converting (sets the year of birth to the current year)
        birthday_this_year = birthday.replace(year=today.year)

     # evaluating the date for this year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

     # comparision with the current date
        delta_days = (birthday_this_year - today).days

     # determining the day of the week
        birthday_weekday = birthday_this_year.weekday()

     # check for weekends
        if birthday_weekday >= 5:
            birthday_weekday = 0  # Monday
            
     # determining the day of the week, storing the result
        if delta_days < 7 : #If we want to take first monday from today we need to add this line before ":"===>   +today.weekday() 
            birthday_weekday_name = (monday_of_next_week + timedelta(days=birthday_weekday)).strftime("%A")
            birthday_dict[birthday_weekday_name].append(name)
            
    # print the result
    for day, birthdays in birthday_dict.items():
        print(f"{day}: {', '.join(birthdays)}")

# Example usage:
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 3, 12)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 3, 17)},
    {"name": "Jan Nowak", "birthday": datetime(1976, 3, 22)},
]
print(get_birthdays_per_week(users))
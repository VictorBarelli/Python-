from datetime import date


def calculate_age(day, month, year):
    
    today = date.today()
    
    birthdate = date(year, month, day)
    
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    return age


try:
    
    day = input('Enter day:')
    month = input('Enter month:')
    year = input('Enter year:')
   
    age_result = calculate_age(int(day), int(month), int(year))
    print(f'You are {age_result} years old')


except:
    print(f'Failed to calculate age, either day or month or year is invalid')


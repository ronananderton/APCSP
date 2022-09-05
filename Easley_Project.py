from datetime import datetime

month = datetime.now().month
year = datetime.now().year

days_in_year = 365.2425
months_in_year = 12

planet_data = {
    'Mercury': [58.6, 0.241],
    'Venus': [243, 0.615],
    'Mars': [1.03, 1.88]
}

age = input("When is your birthday? (MM/DD/YYYY) \n ")
age = age.split("/")

birth_month = int(age[0][1]) if age[0][0] == '0' else int(age[0])
birth_day   = int(age[1][1]) if age[1][0] == '0' else int(age[1])
birth_year  = int(age[2])

earth_years = year - birth_year + (month - birth_month) / months_in_year

for planet, data in planet_data.items():
    years = round(earth_years / data[1], 2)
    print(f"Your age on {planet} is approximately {years} years.")

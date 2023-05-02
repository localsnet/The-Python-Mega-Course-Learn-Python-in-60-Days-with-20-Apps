def age_calc(year_of_birth, current_year=2023):
    calculated = current_year - int(year_of_birth)
    if calculated > 120:
        calculated = f"You are not the man"
    return calculated


date_birth = input("What is your year of birth? ")
print(age_calc(date_birth))
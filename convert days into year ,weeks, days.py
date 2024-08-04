def convert_days(total_days):
    days_in_year = 365
    days_in_week = 7
    years = total_days // days_in_year
    remaining_days = total_days % days_in_year
    weeks = remaining_days // days_in_week
    days = remaining_days % days_in_week
    return years, weeks, days
total_days = 900
years, weeks, days = convert_days(total_days)
print(f"{total_days} days is equivalent to {years} years, {weeks} weeks, and {days} days.")

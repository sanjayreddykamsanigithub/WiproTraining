from datetime import datetime

now = datetime.now()
print("Current Date and Time:", now)

date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 1, 10)

difference = date2 - date1
print("Number of days between dates:", difference.days)

formatted_date = now.strftime("%d-%m-%Y")
print("Formatted Date:", formatted_date)
from datetime import datetime

# Define two dates
date1 = datetime(2023, 12, 25, 12, 0, 0)
date2 = datetime(2023, 12, 26, 14, 30, 0)

# Calculate the difference in seconds
time_difference = (date2 - date1).total_seconds()

print("Date 1:", date1)
print("Date 2:", date2)
print("Difference in seconds:", time_difference)
from datetime import datetime, timedelta

# Current date
current_date = datetime.now()

# Subtract 5 days
new_date = current_date - timedelta(days=5)

print("Current Date:", current_date)
print("Date 5 days ago:", new_date)
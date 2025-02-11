from datetime import datetime

# Current datetime with microseconds
current_datetime = datetime.now()

# Drop microseconds
datetime_no_microseconds = current_datetime.replace(microsecond=0)

print("Original datetime:", current_datetime)
print("Without microseconds:", datetime_no_microseconds)
import re

with open("/Users/akkuermankyzy/Desktop/akosi.cpp/lab5/row.txt", "r", encoding="utf-8") as file:
    data = file.read()
    print(data) 

pattern = re.compile(r"(\d+)\.\n?(.*?)\n?(\d+,\d{3}|\d+)\s*x\s*(\d+,\d{3}|\d+)\n?(\d+,\d{3}|\d+)")

items = []

for line in data:
    match = pattern.search(line)
    if match:
        item_number = match.group(1) 
        name = match.group(2).strip() 
        quantity = match.group(3) 
        price_per_unit = match.group(4) 
        total_price = match.group(5) 
        items.append({
            "Номер": item_number,
            "Название": name,
            "Количество": quantity,
            "Цена за единицу": price_per_unit,
            "Общая стоимость": total_price
        })

for item in items:
    print(item)

# abc… Letters
#123…Digits
#\d Any Digit
#\D Any Non-digit character
#.Any Character

#\. Period

#[abc] Only a, b, or c

#[^abc] Not a, b, nor c

# [a-z]Characters a to z

# [0-9]
# Numbers 0 to 9

# \w
# Any Alphanumeric character

# \W
# Any Non-alphanumeric character

# {m}
# m Repetitions

# {m,n}
# m to n Repetitions

# *
# Zero or more repetitions

# +
# One or more repetitions

# ?
# Optional character

# \s
# Any Whitespace

# \S
# Any Non-whitespace character

# ^…$
# Starts and ends

# (…)
# Capture Group

# (a(bc))
# Capture Sub-group

# (.*)
# Capture all

# (abc|def)
# Matches abc or def
import json
from datetime import date
try:
    with open("daily_listings.json", "r") as file:
        daily_listings = json.load(file)

except FileNotFoundError:
    daily_listings = []
    

today = date.today()
print(today)

entry_exists = False

for record in daily_listings:
    if record["date"] == today.isoformat():
        entry_exists = True
        
if entry_exists:
    
    new_handbag_count = input("How many bags were listed today?")    
    for record in daily_listings:
        if record["date"] == today.isoformat() and record["category"] == "Handbag":
            record["quantity"] = int(new_handbag_count)
            
    new_accessories_count = input("How many accessories were listed today?")
    for record in daily_listings:
        if record["date"] == today.isoformat() and record["category"] == "Accessories":
            record["quantity"] = int(new_accessories_count)
    
    new_shoes_count = input("How many shoes were listed today?")        
    for record in daily_listings:
        if record["date"] == today.isoformat() and record["category"] == "Shoes":
            record["quantity"] = int(new_shoes_count)
else:
    todays_handbags_count = input ("How many bags were listed today?" )
    daily_listings.append({
        "date": today.isoformat(),
        "category": "Handbag",
        "quantity": int(todays_handbags_count),
        })

    todays_accessories_count = input ("How many accessoires were listed today?")
    daily_listings.append({
        "date": today.isoformat(),
        "category": "Accessories",
        "quantity": int(todays_accessories_count),
        })
    
    todays_shoes_count = input("How many shoes were listed today?")
    daily_listings.append({
        "date": today.isoformat(),
        "category": "Shoes",
        "quantity": int(todays_shoes_count),
        })

with open("daily_listings.json", "w") as file:
    json.dump(daily_listings, file)
handbag_total = 0
    
for record in daily_listings:
    if record["category"] == "Handbag":
        handbag_total += record["quantity"]
            
print (handbag_total)
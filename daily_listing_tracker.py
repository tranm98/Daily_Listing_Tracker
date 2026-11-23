import json
from datetime import date
try:
    with open("daily_listings.json", "r") as file:
        daily_listings = json.load(file)

except FileNotFoundError:
    daily_listings = []
    

today = date.today()
print(today)
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
handbag_total = 0
    
for record in daily_listings:
    if record["category"] == "Handbag":
        handbag_total += record["quantity"]
            
print (handbag_total)
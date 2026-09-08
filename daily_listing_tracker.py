import math

handbag_count = []
accessories_count = []

for i in range (6):
    todays_handbags_listings = input ("How many bags/wallets were listed today?" )
    handbag_count.append(int(todays_handbags_listings))
    print(handbag_count)

    todays_accessories_count = input ("How many accessoires were listed today?")
    accessories_count.append(int(todays_accessories_count))
    print(accessories_count)

    handbag_total = sum(handbag_count)
    accessories_total = sum(accessories_count)
    overall_total = handbag_total + accessories_total
    print (f"Weekly overall total is: ", {overall_total} , "\nWeekly Hanbags+Wallets Total is: " , {handbag_total} , "\nWeekly Accessories Total is: " , {accessories_total})
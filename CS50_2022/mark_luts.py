# from hello import hello, main

# main()


number_shares = 2000
price_for_stock = 40
percent_for_buy_stock = 0.03

# Buy process
total_buy_stock = number_shares * price_for_stock 
commision_stock = total_buy_stock * percent_for_buy_stock
total_and_commision_buy = total_buy_stock + commision_stock

print(total_buy_stock, commision_stock, total_and_commision_buy)

# Sell process

number_sell_stock = 2000
price_for_sale = 42.75
percent_for_brokker = 0.03

total_sell_stock = number_sell_stock * price_for_sale
commision_sell = total_sell_stock * percent_for_brokker
total_and_commision_sell = total_sell_stock + commision_sell

print(total_and_commision_sell)
profit = total_and_commision_sell - total_and_commision_buy 
print(profit)
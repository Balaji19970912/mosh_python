has_good_credit = True
price = 1000000

if has_good_credit:
    down_payment_price = 0.1 * price
else:
    down_payment_price = 0.2 * price
print("Amount payable: ",down_payment_price)
def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100


orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}")


# Practise 

def interest_rate_calculate(amount, rate):
    return amount * (1 + rate/100)

cost = [100, 200, 300]

for c in cost:
    interest_rate_calculate(c, 5)
    print(f"Original: {c}, Final with Interest Rate: {interest_rate_calculate(c, 5)}") 



    
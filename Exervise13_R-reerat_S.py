toalPrice = int(input("Enter Toal price :"))

def vatCalculate(toalPrice):
    result = toalPrice + (toalPrice * 7 / 100)
    return result

print("Vat :",vatCalculate(toalPrice))

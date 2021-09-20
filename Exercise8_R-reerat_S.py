usn = input("Username :")
psw = input("Password :")

if usn =="mild" and psw =="11111":
    print("!!Welcome!!")
    if True:
        print("-----Mild's Gadget-----")
        print("1. Smart Watch  : 10,000฿")
        print("2. Smart TV     : 20,000฿")
        print("3. Smartphone   : 30,000฿")
        print("-----------------------")

        choose = input("Enter number gadget (Ex:2) :")
        if choose =="1":
            print("-----------------------")
            print("Smart Watch : 10,000฿")

            priceWatch = int(10000)
            amountWatch = int(input("How much to buy :"))
            totalPriceWch = int(priceWatch) * int(amountWatch)

            print("-----------------------")
            print("Your order is Smart Watch : 10,000฿","X",amountWatch)
            print("-----------------------")
            print("total price :",totalPriceWch,"฿")
            print("Thank you for using the service")

        elif choose =="2":
            print("-----------------------")
            print("Smart TV  : 20,000฿")

            priceTV = int(20000)
            amountTV = int(input("How much to buy :"))
            totalPriceTV = int(priceTV) * int(amountTV)

            print("-----------------------")
            print("Your order is Smart TV : 20,000฿","X",amountTV)
            print("-----------------------")
            print("total price :",totalPriceTV,"฿")
            print("Thank you for using the service")

        elif choose =="3":
            print("-----------------------")
            print("Smartphone  : 30,000฿")

            pricePhone = int(30000)
            amountPhone = int(input("How much to buy :"))
            totalPricePhone = int(pricePhone) * int(amountPhone)

            print("-----------------------")
            print("Your order is SmartPhone : 30,000฿","X",amountPhone)
            print("-----------------------")
            print("total price :",totalPricePhone,"฿")
            print("Thank you for using the service")
else:
    print("---End---")

